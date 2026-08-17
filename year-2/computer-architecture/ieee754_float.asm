.data
	inputStr: .space 2
	intValue: .word 0
	ask: .asciiz "Enter a real number [xxx.yyy]: "
	sign: .asciiz "\nThe sign bit of your number is: "
	exponent: .asciiz "\nThe exponent of your number is: "
	fraction: .asciiz "\nThe fraction of your number is: "
	point: .asciiz "."

.text
.globl main
main:
	la $a0, ask
	li $v0, 4
	syscall
	
	### collect xxx ###
	li $v0, 8
	la $a0, inputStr
	li $a1, 2
	syscall				#collect first digit before point
	lw $t0, 0($a0)
	
	li $v0, 8
	la $a0, inputStr
	syscall				#collect second digit before point
	lw $t1, 0($a0)
	
	li $v0, 8
	la $a0, inputStr
	syscall				#collect third digit before point
	lw $t2, 0($a0)
	
	la $a0, point			#prints point between numbers
	li $v0, 4			#load syscall for printing string
	syscall
	
	### collect yyy ###
	li $v0, 8
	la $a0, inputStr
	syscall				#collect first digit after point
	lw $t3, 0($a0)
	
	li $v0, 8
	la $a0, inputStr
	syscall				#collect second digit after point
	lw $t4, 0($a0)
	
	li $v0, 8
	la $a0, inputStr
	syscall				#collect third digit after point
	lw $t5, 0($a0)
	
	### get int value of xxx ###
	addi $t0, $t0, -48
	mul $t0, $t0, 100
	
	addi $t1, $t1, -48
	mul $t1, $t1, 10
	
	addi $t2, $t2, -48
	
	add $t0, $t0, $t1
	add $t0, $t0, $t2		#int value of xxx ready
	
	### get int value of yyy ###
	addi $t3, $t3, -48
	mul $t3, $t3, 100
	
	addi $t4, $t4, -48
	mul $t4, $t4, 10
	
	addi $t5, $t5, -48
	
	add $t1, $t3, $t4
	add $t1, $t1, $t5		#whole int value of yyy ready
	
	### get whole float and store in $f0 ###
	mtc1 $t0, $f0
	cvt.s.w $f0, $f0		#xxx to float
	
	mtc1 $t1, $f2
	cvt.s.w $f2, $f2		#yyy to float
	
	li $t2, 1000			#get divisor to combine floats to get full number
	mtc1 $t2, $f4
	cvt.s.w $f4, $f4		#divisor is now a float

	div.s $f12, $f2, $f4		#divide yyy by 1000 to get numbers after decimal
	add.s $f12, $f2, $f12		#get the value of the double, store in $f12
	# str2float ready # 
	
	### prepare registers for comparing ###
	li $t0, 0			#counter register
	li $t2, 256		        #clear for usage
	mfc1 $t7, $f12			#move input back from coprocessor to regular register
	
	la $a0, sign
	li $v0, 4
	syscall				#print sign ans
	
	srl $t5, $t7, 31
	
	and $t5, $t5, $t1		#check if the bit = 1
	beq $t1, $t5, printOne		#if bit = 1, print 1
	bne $t5, $t1, printZero		#if bit = 0, print 0
	
printHexExponent:
	la $a0, exponent		#function for printing hex exponent answer
	li $v0, 4
	syscall
	
	li $t5, 0			#prepare register for comparing
	srl $t5, $t7, 23		#access exponent bits
	
	j hexExponent
	
printHexFraction:
	la $a0, fraction		#function for printing hex fraction answer
	li $v0, 4
	syscall
	
	li $t2, 4194304			#load for comparing fraction bits
	li $t3, 0			#prepare registers for comparing
	li $t5, 0
	
	srl $t5, $t7, 0
	addi $t0, $t0, 1		#increment counter
	j hexFraction

hexExponent:
	addi $t0, $t0, 1		#increment counter
	beq $t0, 9, printHexFraction	#when counter = 9, start printing hex fraction answer
	
	and $t3, $t5, $t2		#and the shifting register and comparing register, store in $t3
	
	beq $t2, $t3, printOne		#if bits are both 1, print one
	bne $t2, $t3, printZero		#if not print 0
	
hexFraction:
	addi $t0, $t0, 1		#increment counter
	
	and $t4, $t5, $t2		#and the shifting register and comparing register, store in $t4
	
	beq $t2, $t4, printOne		#if bits are both 1, print one
	bne $t2, $t4, printZero		#if not print 0
	
	
printZero:
	beq $t0, 1, printHexExponent	#if counter = 1, start printing hex exponent answer
	move $a0, $zero			
	li $v0, 1			#load syscall for printing integer
	syscall
	beq $t0, 9, printHexFraction	#if counter = 9, and bit = 0, start printing fraction answer
	
	beq $t0, 33, exit		#if counter = 33, and bit = 0, exit
	srl $t2, $t2, 1			#shift comparing bit
	bne $t0, 33, hexFraction	#basic while loop, while counter != 33, go to hexFraction
	
	j hexExponent			#jump back to compare
	
printOne:	
	beq $t0, 1, printHexExponent	
	li $v0, 1			#load syscall for printing integer
	li $t4, 1			
	move $a0, $t4
	syscall
	beq $t0, 9, printHexFraction	#if counter = 9, and bit = 1, start printing fraction answer
	
	beq $t0, 33, exit		#if counter = 33, and bit = 1, exit
	srl $t2, $t2, 1			#shift comparing bit
	bne $t0, 33, hexFraction	#basic while loop, while counter != 33, go to hexFraction
	
	j hexExponent			#jump back to compare

	

exit:
	li $v0, 9			#syscall for exiting program
	syscall