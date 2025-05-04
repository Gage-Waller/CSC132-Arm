// Finger.h 
// the header file for the finger class
#ifndef Finger_h
#define Finger_h

#include <Adafruit_PWMServoDriver.h> // PCA 965 (the servo controller that we are using)

class Finger {
  public:
    int servoPin;
    int sHome;
    Adafruit_PWMServoDriver pwm; // the servo controller



  public:
    Finger(int pin);
    void fingerSetup();
    void moveToDeg(int deg);
    void setHome(); // home preset (all 0)
  
};


#endif 