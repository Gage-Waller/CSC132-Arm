// Finger.cpp

#include "Finger.h"

#define SERVOMIN  95 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  520 // this is the 'maximum' pulse length count (out of 4096)

Finger::Finger(int pin){
  servoPin = pin;
  sHome = 0;
  // this is the initialization for the servo controller
  pwm = Adafruit_PWMServoDriver();
}

// general setup for the finger (only needs to be run once in setup)
void Finger::fingerSetup(){

  pwm.begin();
  pwm.setPWMFreq(60);

}

// just moves the finger
void Finger::moveToDeg(int deg){
  pwm.setPWM(servoPin, 0, map(deg,0, 180, SERVOMIN,SERVOMAX)); // map had to used because servo is upposed to go 1-180 but using PWM
  // library makes changes the numbers

}  


// sets the servo to 0
void Finger::setHome(){
  moveToDeg(sHome);
}

