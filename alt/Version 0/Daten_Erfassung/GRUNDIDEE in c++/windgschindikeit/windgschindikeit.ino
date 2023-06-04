/*
 GUNDIDEEE windgeschindikeit
*/
int ledpin = 0; 
int fotopin = 10;
int anwert = 900;
int zahler = 0;   // zählt wie oft an war um es zu Rpm

void setup() {
  pinMode(fotopin,INPUT);
  pinMode(ledpin,OUTPUT);
}
void loop (){
  if (analogRead(fotopin) <= anwert ){ //wann ? 
      zahler++;
  }
  else{
  }
  digitalWrite(ledpin,1);
}

// die funktion um den wert auszulesen 
int getwindanzal(){
  return zahler ;
}