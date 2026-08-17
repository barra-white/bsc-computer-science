.data
	inputStr: .space 2
	intValue: .word 0
	ask: .asciiz "Enter a two digit integer [00-99]: "
	ans: .asciiz "\nThe binary representation of the integer is: "
	space: .asciiz " "

.text
.globl main
main:
	la $a0, ask
	li $v0, 4
	syscall

	li $v0, 8
	la $a0, inputStr
	li $a1, 2
	syscall				#collect first digit
	lw $t0, 0($a0)
	
	li $v0, 8
	la $a0, inputStr
	li $a2, 2
	syscall				#collect second digit
	lw $t1, 0($a0)	
	### inputStr Ready ###
	
	addi $t0, $t0, -48
	mul $t0, $t0, 10
	
	addi $t1, $t1, -48
	add $t0, $t0, $t1		#combine the two digits to get your integer value
	### intValue Ready ###
	
	la $a0, ans
	li $v0, 4
	syscall				#print the answer string
	
	# prepare registers for loop
	
	li $t1, 9			#register for counter
	li $t2, 128			#register for comparreing
	li $t5, 5			#register for printing space
	
	j compare			#restart loop
	
compare:
	beq $t1, $zero, exit		#jump to exit if loop is finished
	and $t7, $t2, $t0		#check if the bit = 1
	
	beq $t1, $t5, printSpace
	beq $t2, $t7, printOne		#jump to print bit if = 1
	bne $t7, $t2, printZero		#jump to print zero
	
printZero:
	move $a0, $zero			
	li $v0, 1			#load syscall for printing integer
	syscall
	
	addi $t1, $t1, -1		#decrement counter
	srl $t2, $t2, 1			#shift bit
	
	j compare			#jump back to compare
	
printOne:		
	li $v0, 1			#load syscall for printing integer
	li $t4, 1			
	move $a0, $t4
	syscall
	
	addi $t1, $t1, -1		#decrement counter
	srl $t2, $t2, 1			#shift bit
	
	j compare			#jump back to compare
	
printSpace:
	la $a0, space			#prints ident
	li $v0, 4			#load syscall for printing string
	syscall
	
	addi $t1, $t1, -1		#decrement counter
	
	j compare			#jump back to compare
	
exit:
	li $v0, 10			#syscall for exiting program
	syscall
	
	
	
	
	
	
	
	
	
