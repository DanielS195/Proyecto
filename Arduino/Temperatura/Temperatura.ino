int analog_Input = A0;


void setup() {
  pinMode(analog_Input, INPUT);
  Serial.begin(9600);
}


void loop() {
  float analog_Value = 0;

  analog_Value = analogRead(analog_Input) * (5.0/1023.0);
  Serial.println(analog_Value, 4);
  delay(200);
}