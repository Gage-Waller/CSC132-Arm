import json

class Preset:

    RESTING_POSITION = 0
    MINIMUM_SERVO_DEGREE = 0
    MAXIMUM_SERVO_DEGREE = 180

    def __init__(self,a1=RESTING_POSITION,a2=RESTING_POSITION,b1=RESTING_POSITION,
                 b2=RESTING_POSITION,c1=RESTING_POSITION,c2= RESTING_POSITION,d1 = RESTING_POSITION,
                 d2=RESTING_POSITION,e1=RESTING_POSITION,e2=RESTING_POSITION,e3=RESTING_POSITION,
                 f1=RESTING_POSITION):
        

        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        self.d1 = d1
        self.d2 = d2
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.f1 = f1

    @property
    def a1(self):
        return self._a1
        
    @a1.setter
    def a1(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <=Preset.MAXIMUM_SERVO_DEGREE :
            self._a1 = value
        else:
            self._a1 = Preset.RESTING_POSITION

    @property
    def a2(self):
        return self._a2
        
    @a2.setter
    def a2(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._a2 = value
        else:
            self._a2 = Preset.RESTING_POSITION

    @property
    def b1(self):
       return self._b1
        
    @b1.setter
    def b1(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._b1 = value
        else:
            self._b1 = Preset.RESTING_POSITION

    @property
    def b2(self):
        return self._b2
        
    @b2.setter
    def b2(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._b2 = value
        else:
            self._b2 = Preset.RESTING_POSITION

    @property
    def c1(self):
        return self._c1
        
    @c1.setter
    def c1(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._c1 = value
        else:
            self._c1 = Preset.RESTING_POSITION

    @property
    def c2(self):
        return self._c2
        
    @c2.setter
    def c2(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._c2 = value
        else:
            self._c2 = Preset.RESTING_POSITION

    @property
    def d1(self):
        return self._d1
        
    @d1.setter
    def d1(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._d1 = value
        else:
            self._d1 = Preset.RESTING_POSITION

    @property
    def d2(self):
        return self._d2
        
    @d2.setter
    def d2(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._d2 = value
        else:
            self._d2 = Preset.RESTING_POSITION


    @property
    def e1(self):
        return self._e1
        
    @e1.setter
    def e1(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._e1 = value
        else:
            self._e1 = Preset.RESTING_POSITION

    @property
    def e2(self):
        return self._e2
        
    @e2.setter
    def e2(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._e2 = value
        else:
            self._e2 = Preset.RESTING_POSITION

    @property
    def e3(self):
        return self._e3
        
    @e3.setter
    def e3(self,value):
        if value >= Preset.MINIMUM_SERVO_DEGREE and value <= Preset.MAXIMUM_SERVO_DEGREE :
            self._e3 = value
        else:
            self._e3 = Preset.RESTING_POSITION

    @property
    def f1(self):
        return self._f1
        
    @f1.setter
    def f1(self,value):
        if value in range(Preset.MINIMUM_SERVO_DEGREE, Preset.MAXIMUM_SERVO_DEGREE + 1) :
            self._f1 = value
        else:
            self._f1 = Preset.RESTING_POSITION

    def __str__(self):
        return str(f"[{self.a1},{self.a2},{self.b1},{self.b2},{self.c1},{self.c2},{self.d1},{self.d2},{self.e1},{self.e2},{self.e3},{self.f1}]")
    
    def jsonconverter(self):
        pass
    
a = Preset(20,20,20,40,40,0,15,-15,34,34,21,190)
print(a)