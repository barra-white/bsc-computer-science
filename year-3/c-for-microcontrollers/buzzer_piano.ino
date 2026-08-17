#define BUZZER 8 // define buzzer pin
// define notes
#define C4 261.63
#define D4 293.66
#define E4 329.63
#define F4 349.23
#define G4 392.00
#define A4 440.00
#define B4 493.88
#define C5 523.25
#define SPACE 0.0 // input for blank period

float currNote = 0.0; // used for implementation 2 to play note
char note; // used to read char for implementation 2

void setup() {
  pinMode(BUZZER, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  // IMPLEMENTATION 1
  if (Serial.available() > 0) {
    playTune(readData(), 200, 100);
  }
  // IMPLETATION 2
  if (Serial.available() > 0) {
    note = Serial.read();
    handlePress(note);
  }

  if (currNote != 0.0) {
    playNote(currNote);
  }
  playNote(SPACE);
}


// IMPLEMENTATION 1: Input a string into serial, will then play the tune inputted
/*
  Plays note based on inputted frequency f for inputted (millisecs) duration
*/
void playNoteDuration(float f, int duration) {
  float t = 1 / f; // period in seconds
  t = t * 1000000; // convert t to microseconds
  int halfPeriod = t / 2; // half period for delay
  int cycles = 2 * (f * duration / 1000); // calculate in microseconds amount of times to cycle buzzer for note
  for (int i = 0; i < cycles; i++) {
    digitalWrite(BUZZER, HIGH); // turn the buzzer on
    delayMicroseconds(halfPeriod); // wait for half the period
    digitalWrite(BUZZER, LOW); // turn the buzzer off
    delayMicroseconds(halfPeriod); // wait for half the period
  }
}

/*
  Reads a string from serial until enter key is pressed
*/
String readData() {
  // if data is recieved
  if (Serial.available() > 0) {
    // read string until enter key is pressed (or new line)
    String inputtedString = Serial.readStringUntil('\n');
    return inputtedString; // return the string
  }
}

/*
  Dissects string recieved from readData() to figure out what note to play
  Plays note for duration milliseconds
*/
void playTune(String data, int duration, int blankPeriodDuration) {
  // change inputted string to lower to handle upper case letters
  data.toLowerCase();
  // iterate over each character at string
  for (int i = 0; i < data.length(); i++) {
    char note = data.charAt(i);
    // switch statement to decide which note to play based on what char inputted
    switch (note) {
      case 'a': // a == C4
        playNoteDuration(C4, duration);
        break;
      case 's': // s == D4
        playNoteDuration(D4, duration);
        break;
      case 'd': // d == E4
        playNoteDuration(E4, duration);
        break;
      case 'f': // f == F4
        playNoteDuration(F4, duration);
        break;
      case 'g': // g == G4
        playNoteDuration(G4, duration);
        break;
      case 'h': // h == A4
        playNoteDuration(A4, duration);
        break;
      case 'j': // j == B4
        playNoteDuration(B4, duration);
        break;
      case 'k': // k == C5
        playNoteDuration(C5, duration);
        break;
      case ' ': // plays blank period
        delay(blankPeriodDuration);
        break;
      default: // just skips if any invalid characters are pressed
        break;
    }
  }
}



// IMPLEMENTATION 2: Play notes like a keyboard (consistenly plays inputted note until another is pressed)
/*
  Function to play note
*/
void playNote(float f) {
  float t = 1 / f; // period in seconds
  t = t * 1000000; // convert t to microseconds
  int halfPeriod = t / 2; // half period for delay
  digitalWrite(BUZZER, HIGH); // turn the buzzer on
  delayMicroseconds(halfPeriod); // wait for half the period
  digitalWrite(BUZZER, LOW); // turn the buzzer off
  delayMicroseconds(halfPeriod); // wait for half the period
}

/*
  Function to handle what button is pressed
*/
void handlePress(char note) {
  // switch statement to decide which note to play based on what char inputted
  switch (note) {
    case 'a': // a == C4
      currNote = C4;
      break;
    case 's': // s == D4
      currNote = D4;
      break;
    case 'd': // d == E4
      currNote = E4;
      break;
    case 'f': // f == F4
      currNote = F4;
      break;
    case 'g': // g == G4
      currNote = G4;
      break;
    case 'h': // h == A4
      currNote = A4;
      break;
    case 'j': // j == B4
      currNote = B4;
      break;
    case 'k': // k == C5
      currNote = C5;
      break;
    case ' ':
      currNote = SPACE;
      break;
    default: // just skips if any invalid characters are pressed
      break;
  }
}
