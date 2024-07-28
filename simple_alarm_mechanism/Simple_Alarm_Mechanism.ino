
int frequency = 3000;
int alarmCount = 0;
bool flag = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT);
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = analogRead(A1);

  if (reading < 1020) {
    flag = true;
    alarmCount = 0;
  }
  
  
  while (flag) {
  //for (int frequency; frequency < 3000; frequency++) {
    frequency -= 1;
    tone(9, frequency);
    //Serial.println(frequency)
    if (frequency < 500) {
      frequency = 3000; 
      alarmCount += 1; 
    }
    if (alarmCount == 100) {
      flag = false;
      noTone(9);
    }
  }
}
