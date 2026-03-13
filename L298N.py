from machine import Pin, PWM
from utime import sleep

class controll1:
    def __init__(self, pin1, pin2, PWMpin):
        self.in1 = Pin(pin1, Pin.OUT)
        self.in2 = Pin(pin2, Pin.OUT)
        self.enA = PWM(Pin(PWMpin))
        self.enA.freq(1000)
        
    def forward(self, speed, duration):
        self.in1.on()
        self.in2.off()
        self.enA.duty_u16(speed)
        sleep(duration)
        
    def backward(self, speed, duration):
        self.in1.off()
        self.in2.on()
        self.enA.duty_u16(speed)
        sleep(duration)
        
    def stop(self, duration):
        self.in1.off()
        self.in2.off()
        self.enA.duty_u16(0)
        sleep(duration)
        
class controll2:
    def __init__(self, pin1, pin2, pin3, pin4, PWMpin1, PWMpin2):
        self.in1 = Pin(pin1, Pin.OUT)
        self.in2 = Pin(pin2, Pin.OUT)
        self.in3 = Pin(pin3, Pin.OUT)
        self.in4 = Pin(pin4, Pin.OUT)
        self.enA = PWM(Pin(PWMpin1))
        self.enB = PWM(Pin(PWMpin2))  
        self.enA.freq(1000)
        self.enB.freq(1000)
        
    def forward(self, speed, duration):
        self.in1.on()
        self.in2.off()
        self.in3.on()
        self.in4.off()
        self.enA.duty_u16(speed)
        self.enB.duty_u16(speed)
        sleep(duration)
        
    def backward(self, speed, duration):
        self.in1.off()
        self.in2.on()
        self.in3.off()
        self.in4.on()
        self.enA.duty_u16(speed)
        self.enB.duty_u16(speed)
        sleep(duration)
        
    def spin_right(self, speed, duration):
        self.in1.on()
        self.in2.off()
        self.in3.off()
        self.in4.on()
        self.enA.duty_u16(speed)
        self.enB.duty_u16(speed)
        sleep(duration)
        
    def spin_left(self, speed, duration):
        self.in1.off()
        self.in2.on()
        self.in3.on()
        self.in4.off()
        self.enA.duty_u16(speed)
        self.enB.duty_u16(speed)
        sleep(duration)
        
    def stop(self, duration):
        self.in1.off()
        self.in2.off()
        self.in3.off()
        self.in4.off()
        self.enA.duty_u16(0)
        self.enB.duty_u16(0)
        sleep(duration)

class about:
    def what():
        script = f"""This lirary is for controlling an L298N motor driver.

You can also use it to controll other motor drivers like the L293D.

To code this library, you will use module "controll1" to drive 1 motor and "controll2"
to controll 2 motors. the way you code the controll1 module is simple: just type this in:
motor = L298N.controll1(0, 1, 5)  -The first number is the GPIO pin that you want connect to in1,
the second number is the GPIO pin that you want to connect to in2, and the last number is
the one you connect to enA.
If you want to controll 2 motors, then you will use the controll2 module. this is set up like this:
motors = L298N.controll2(0, 1, 2, 3, 5, 6) -The concept is the same as controll1, except you have 4 inputs, and 2 enable PWM pins
functions are: forward(), backward(), and stop() for controll1, and forward(), backward(), spin_right(), spin_left(), and stop() for controll2
inside of the parentheses, you put the speed (0-65535), and the duration (In seconds). For example, motors.forward(10000, 1) means that
you set the motors going forward at speed 10000 for one second. The duration is in all the functions."""
        print(script)

