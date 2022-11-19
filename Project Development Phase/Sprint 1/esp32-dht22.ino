#include "DHTesp.h"
#include <cstdlib>
#include <time.h>

const int DHT_PIN = 15;

bool is_exhaust_fan_on = false;
bool is_sprinkler_on = false;

float temperature  = 0;

int gas_ppm = 0;
int flame = 0;
int flow = 0;

String flame_status = "";
String accident_status = "";
String sprinkler_status = "";

DHTesp dhtSensor;


void setup() {
  Serial.begin(99900);

  /**** sensor pin setups ****/
  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
  //if real gas sensor is used make sure the senor is heated up for acurate readings
  /*
    - Here random values for readings and stdout were used to show the 
      working  of the devices as physical or simulated devices are not 
      available.
  */
}

void loop() {

  TempAndHumidity  data = dhtSensor.getTempAndHumidity();

  //setting a random seed
  srand(time(0));

  //initial variable activities like declaring , assigning
  temperature  = data.temperature;
  gas_ppm = rand()%1000;
  int flamereading = rand()%1024;
  flame = map(flamereading,0,1024,0,1024);
  int flamerange = map(flamereading,0,1024,0,3);
  int flow = ((rand()%100)>50?1:0);

  //set a flame status based on how close it is.....
  switch (flamerange) {
  case 2:    // A fire closer than 1.5 feet away.
    flame_status = "Fire is Nearer";
    break;
  case 1:    // A fire between 1-3 feet away.
    flame_status = "Fire is getting closer";
    break;
  case 0:    // No fire detected.
    flame_status = "No Fire Detected";
    break;
  }

  //toggle the fan according to gas in ppm in the room
  if(gas_ppm > 100){
    is_exhaust_fan_on = true;
  }
  else{
    is_exhaust_fan_on = false;
  }

  //find the accident status 'cause fake alert may be caused by some mischief activities
  if(temperature < 42 && flamerange ==2){
    accident_status = "Requires Inspection";
    is_sprinkler_on = false;
  }
  else if(temperature < 40 && flamerange ==0){
    accident_status = "Nothing Discovered";
    is_sprinkler_on = false;
  }
  else if(temperature > 50 && flamerange == 1){
    is_sprinkler_on = true;
    accident_status = "Moderate Fire";
  }
  else if(temperature > 55 && flamerange == 2){
    is_sprinkler_on = true;
    accident_status = "Terrible Fire";
  }else{
    is_sprinkler_on = false;
    accident_status = "Nil";
  }


  //send the sprinkler status
  if(is_sprinkler_on){
    if(flow){
      sprinkler_status = "Functioning";
    }
    else{
      sprinkler_status = "Not Functioning";
    }
  }
  else if(is_sprinkler_on == false){
    sprinkler_status = "It shouldn't happen now";
  }
  else{
    sprinkler_status = "something's wrong";
  }

  //Obivously the output.It is like json format 'cause it will help us for future sprints
  String out = "\nSENSOR VALUES : ";
  out+="\n\tGas ppm : "+String(gas_ppm)+",";
  out+="\n\tTemperature : "+String(temperature,2)+",";
  out+="\n\tFlame : "+String(flame)+",";
  out+="\n\tFlow : "+String(flow)+",\n\t";
  out+="\n\tOUTPUT : ";
  out+="\n\tExhaust fan on : "+String((is_exhaust_fan_on)?"true":"false")+",";
  out+="\n\tSprinkler on : "+String((is_sprinkler_on)?"true":"false")+",";
  out+="\n\t";
  out+="\n\tMESSAGES : ";
  out+="\n\tStatus of Fire : "+flame_status+",";
  out+="\n\tSprinkler Status : "+sprinkler_status+",";
  out+="\n\tAccident Status : "+accident_status+",";
  out+="\n\t";
 
  Serial.println(out);
  delay(1000);
}
