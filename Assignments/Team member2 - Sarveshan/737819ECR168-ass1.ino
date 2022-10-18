int trigger_pin = 2;
int echo_pin = 3;
int buzzer_pin = 10; 
int time;
int distance; 
void setup() 
{
        Serial.begin (9600); 
        pinMode (trigger_pin, OUTPUT); 
        pinMode (echo_pin, INPUT);
        pinMode (buzzer_pin, OUTPUT);
}
void loop() 
{
    digitalWrite (trigger_pin, HIGH);
    delayMicroseconds (10);
    digitalWrite (trigger_pin, LOW);
    time = pulseIn (echo_pin, HIGH);
    distance = (time * 0.034) / 2;
	double a=analogRead(A0);
    double t=(((a/1024)*5)-0.5)*100;
  if (distance <= 30) 
        {
        Serial.println (" Door Open ");
        Serial.print (" Distance= ");              
        Serial.println (distance);        
        digitalWrite (buzzer_pin, HIGH);
    	if(t>100)
          Serial.println("ON AC");
        delay (500);
        }
  else {
        Serial.println (" Door closed ");
        Serial.print (" Distance= ");              
        Serial.println (distance);        
        digitalWrite (buzzer_pin, LOW);
        delay (500);        
       } 
}