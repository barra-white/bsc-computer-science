// OUT (PORT B)
#define P1_GREEN 12
#define P1_RED 13
#define P2_GREEN 11
#define P2_RED 10

#define WAIT_LED 9
#define BUZZER 8

// IN (PORT D)
#define P1_BUTTON 3
#define P2_BUTTON 2
#define START_BUTTON 7

// for attaching intterupts
volatile unsigned long P1_PressTime = 0;
volatile unsigned long P2_PressTime = 0;

volatile bool P1_Pressed = false;
volatile bool P2_Pressed = false;

// flags for game conditions
bool buzzing = false;
bool roundOver = false;

// volatile as handled by ISR
volatile uint8_t buttonState;

// get time buzzer starts going off
unsigned long buzzTime;

// define string values for printing results
char *outValues[] = {"Player 1", "Player 2", "Draw"};

char *player1STR = outValues[0];
char *player2STR = outValues[1];
char *drawSTR = outValues[2];

// win counters
int player1Wins = 0;
int player2Wins = 0;

void setup() {
  // sets pins 13, 12, 11, 10, 9, 8 to output pins (0x00111111)
  DDRB = 0x3F;
  // sets pins 5, 3, 2 to input pins (0x11010011)
  DDRD = 0xD3; 
  //begin serial
  Serial.begin(9600);
  // for the use of random() later
  randomSeed(analogRead(A0));
  // activate interrupt for port D
  PCICR |= B00000100;
  // enable pin change interrupt for player buttons
  PCMSK2 |= (1 << PCINT18) | (1 << PCINT19);
}

void loop() {
  // if start button is pressed -> begin game
  if (PIND & (1 << START_BUTTON)) {
    // counter for round
    int roundCounter = 0;
    // stores winner of each round
    char *winners[3];
    unsigned long time[3];
    unsigned long difference[3];

    // main loop for 3 rounds
    while (roundCounter < 3) {
      roundStart();
      resetButtonStates();
      unsigned long start = millis();
      buzzTime = waitForBuzzer();
      while (!roundOver) {
        buttonPressHandler();
      }
      digitalWrite(BUZZER, LOW);
      getWinner(buzzTime, roundCounter, winners, time, difference);
      resetButtonStates();
      roundCounter++;
    }
    printWinner(winners, time, difference);
  }
  
}

/*
  ISR to read button state on interrupt from pins 2 or 3
*/
ISR(PCINT2_vect) {
  // changes button state to read current value of PIND
  buttonState = PIND;
}

/*
  The following function is called at the start of each round
  Wait LED (blue) is on for 5 secs and buzzer plays 3 quick times
  When led turns off, round has started
*/
void roundStart() {
  // set led to on
  PORTB = B00000010;
  delay(500);
  // led and buzzer on
  PORTB = B00000011;
  delay(250);
  PORTB = B00000010;
  delay(250);
  PORTB = B00000011;
  delay(250);
  PORTB = B00000010;
  delay(250);
  PORTB = B00000011;
  delay(250);
  PORTB = B00000010;
  delay(250);
  delay(1500);
  // everything off + round has started
  PORTB = B00000000;
}

/*
  Function waits X seconds before sounding buzzer
*/
unsigned long waitForBuzzer() {
  // set time for when buzzer starts going off
  unsigned long buzzerTime = 0;
  // get random number for X secs (0 < X < 10)
  int X = (random(1, 10) * 1000);
  // set start time so function will only run for as long as X
  unsigned long startTime = millis();
  // the loop to wait as long as X ms
  while(millis() - startTime < X) {
    // if a button is pressed exit
    if (P1_Pressed || P2_Pressed) {
      roundOver = true;
      return buzzerTime;
    }
    // continously check for input
    buttonPressHandler();
  }
  // else play buzzer
  digitalWrite(BUZZER, HIGH);
  buzzerTime = millis();
  // flag buzzing as true
  buzzing = true;
  return buzzerTime;
}

/*
  Handles button presses
  Using micros as to get exact time button is clicked -> this is more accurate than
  using if statements as they would (although very small) still introduce a slight bias
  in the case of a draw
*/
void buttonPressHandler() {
  // if button state is showing both 2 and 3 as HIGH
  if (buttonState & ((1 << P1_BUTTON) & (1 << P2_BUTTON))) {
    onClick_P1();
    onClick_P2();
    return;
  }
  // if just P1 is high
  if (buttonState & (1 << P1_BUTTON)) {
    onClick_P1();
    return;
  }
  // if just P2 is high
  if (buttonState & (1 << P2_BUTTON)) {
    onClick_P2();
    return;
  }
  return;
}

// function to handle led upon win/lose/draw
/*
  Player 1 win led handler
*/
void player1LED() {
  // turn blue, player 2 green and player 1 red
  PORTB |= B00010110;
  delay(5000);
  // turn all off
  PORTB &= B11101001;
  // incremenet win counter
  player1Wins++;
}
/*
  Player 2 win led handler
*/
void player2LED() {
  // turn blue, player 2 green and player 1 red
  PORTB |= B00101010;
  delay(5000);
  // turn all off
  PORTB &= B11010101;
  // increment win counter
  player2Wins++;
}
/*
  Draw led handler
*/
void drawLED() {
  // turn all led on
  PORTB |= B00111110;
  delay(5000);
  // turn all off
  PORTB &= B11000001;
}
/*
  compares press times + determines winner
*/
void getWinner(unsigned long buzzTime, int roundNumber, char *winners[], unsigned long time[], unsigned long difference[]) {
  // if buzzer is not buzzing
  if (!buzzing) {
    // check to see if 2 has pressed
    if ((P1_PressTime == 0) && !(P2_PressTime == 0)) {
      winners[roundNumber] = player1STR;
      time[roundNumber] = 0;
      difference[roundNumber] = 0;
      player1LED();
      return;
    }
    // check to see if 1 has pressed
    if (!(P1_PressTime == 0) && (P2_PressTime == 0)) {
      winners[roundNumber] = player2STR;
      time[roundNumber] = 0;
      difference[roundNumber] = 0;
      player2LED();
      return;
    }  
  }
  // if after buzzer, main code
  // draw
  if (P1_PressTime == P2_PressTime) {
    winners[roundNumber] = drawSTR;
    time[roundNumber] = P1_PressTime - buzzTime;
    difference[roundNumber] = 0;
    drawLED();
    return;
  }
  // p1 win
  if (P1_PressTime < P2_PressTime) {
    winners[roundNumber] = player1STR;
    time[roundNumber] = P1_PressTime - buzzTime; // how long it took to press
    difference[roundNumber] = (P1_PressTime - P2_PressTime); // difference in times
    player1LED();
    return;
  }
  // p2 win
  if (P1_PressTime > P2_PressTime) {
    winners[roundNumber] = player2STR;
    time[roundNumber] = P2_PressTime - buzzTime;
    difference[roundNumber] = (P2_PressTime - P1_PressTime);
    player2LED();
    return;
  }
}

/*
  prints overall winner + winner (winner time, winner difference) of each round
*/ 
void printWinner(char *winners[], unsigned long time[], unsigned long difference[]) {
  if (!(player1Wins == player2Wins)) {
    if (player1Wins > player2Wins) {
      Serial.println("Player 1 wins overall!");
    }
    else if (player1Wins < player2Wins) {
      Serial.println("Player 2 wins overall!");
    }
    else {
      Serial.println("The result is a draw!");
    }
  }
  Serial.println("(ms) = microsecs");
  Serial.println("");
  Serial.println("          WINNER      TIME(ms)      DIFFERENCE(-ms)");
  for (int i = 0; i < 3; i++) {

    Serial.print("Game: ");
    Serial.print(i+1);
    Serial.print("  ");
    Serial.print(winners[i]);
    Serial.print("     ");
    Serial.print(time[i]);
    Serial.print("       ");
    Serial.print(difference[i]);
    Serial.println("");
    // delay as to not overload serial
    delay(1000);
  }
}

// onClick functions
/*
  Function to run each time Player 1 clicks button
*/
void onClick_P1() {
  P1_Pressed = true;
  P1_PressTime = micros();
  // if both buttons have recorded a time
  if (P1_Pressed && P2_Pressed) {
    roundOver = true;
  }
}
/*
  Function to run each time Player 2 clicks button
*/
void onClick_P2() {
  P2_Pressed = true;
  P2_PressTime = micros();
  // if both buttons have recorded a time
  if (P1_Pressed && P2_Pressed) {
    roundOver = true;
  }
}

/*
  function to reset button values -> easier readability
*/
void resetButtonStates() {
  P1_Pressed = false;
  P2_Pressed = false;
  P1_PressTime = 0.0;
  P2_PressTime = 0.0;
  roundOver = false;
  buzzing = false;
  buzzTime = 0;
}
