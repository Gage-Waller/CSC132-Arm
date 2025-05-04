#include "Finger.h"
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Finger thumb(0); //number is for the port of servo
Finger index(1);
Finger middle(2);
Finger ring(3);
Finger pinky(4);



void setup() {

  Serial.begin(115200); // keeping this number is better for the myoware sensor

  // these two things are for the genral setup for the servo controller
  thumb.fingerSetup(); //runs a function that only needs to be called once therefor just the thumb is used


}

void loop() {
  // put your main code here, to run repeatedly: 

  int myo = analogRead(A0);


  if(Serial.available() > 0){ // checks if there is any integer value in the seril monitor is greater than 0

    int piValue = Serial.read();

    if(piValue == 1){
      thumb.moveToDeg(170);
    } else{
      thumb.moveToDeg(0);
    }

  }

 //Serial.println(myo);

}



// runs all the motors to a specified degrees
void setMotors(int thumbDeg, int indexDeg, int middleDeg, int ringDeg, int pinkyDeg){
  thumb.moveToDeg(thumbDeg);
  index.moveToDeg(indexDeg);
  middle.moveToDeg(middleDeg);
  ring.moveToDeg(ringDeg);
  pinky.moveToDeg(pinkyDeg);
}



