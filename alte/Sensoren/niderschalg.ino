/*
 GUNDIDEEE NIEDERSCHALAG
*/

int rainsenpin = A5; //der pin vom regensensor 
int ventpin = 5; //der pin wo das relais mit angesprochen wird
int anwert = 900 ; // werte wenn es schalten soll 
int zaehler = 0;   // zählt wie oft es an war

void setup() {
  pinMode(rainsenpin,INPUT); // PULLUP ?
  pinMode(ventpin,OUTPUT);
}

void loop (){
    if (analogRead(rainsenpin) <= anwert ){ //wann 
      digitalWrite(ventpin,1);//vent auf
      zaehler++;
    }
    else{
      digitalWrite(ventpin,0);//vent zu
    } 
}
int getwindanzal(){
  return zaehler ;
}

