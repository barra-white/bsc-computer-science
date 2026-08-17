#define GREEN 12
#define RED 13

void setup() {
  // set 13 and 12 to output
  pinMode(GREEN, OUTPUT);
  pinMode(RED, OUTPUT);
}

void loop() {
  // assign the compliment of pinD
  uint8_t notD = ~PIND;
  // check if there is any two consecutive HIGH pins
  if (PIND & (PIND << 1)) {
    digitalWrite(RED, HIGH);
  }
  else {digitalWrite(RED, LOW);}

  // check if there is any two consecutive LOW pins
  if (notD & (notD << 1)) {
    digitalWrite(GREEN, HIGH);
  }
  else {digitalWrite(GREEN, LOW);}
}