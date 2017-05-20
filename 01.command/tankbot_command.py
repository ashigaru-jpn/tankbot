from __future__ import print_function
import time
import wiringpi
# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
_max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = _max_speed

class MotorDriver():
    pinRight1 = 0
    pinRight2 = 0
    pinLeft1 = 0
    pinLeft2 = 0
    isFirst = True
    
    def __init__(self):
        pass

    def setPin(self, pin_right_1, pin_right_2, pin_left_1, pin_left_2):
        self.pinRight1 = int(pin_right_1)
        self.pinRight2 = int(pin_right_2)
        self.pinLeft1 = int(pin_left_1)
        self.pinLeft2 = int(pin_left_2)

    def wakeup(self):
        if self.isFirst:
            wiringpi.wiringPiSetupGpio()

            wiringpi.pinMode(self.pinRight1, wiringpi.GPIO.OUTPUT)
            wiringpi.pinMode(self.pinRight2, wiringpi.GPIO.PWM_OUTPUT)
            wiringpi.pinMode(self.pinLeft1, wiringpi.GPIO.OUTPUT)
            wiringpi.pinMode(self.pinLeft2, wiringpi.GPIO.PWM_OUTPUT)

            wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
            wiringpi.pwmSetRange(MAX_SPEED)
            wiringpi.pwmSetClock(2)
            
            self.isFirst = False

    def quit(self):
        wiringpi.digitalWrite(self.pinRight1, 0)
        wiringpi.digitalWrite(self.pinLeft1, 0)
        wiringpi.digitalWrite(self.pinRight2, 0)
        wiringpi.digitalWrite(self.pinLeft2, 0)
        wiringpi.pwmWrite(self.pinRight2, 0)
        wiringpi.pwmWrite(self.pinLeft2, 0)
        self.isFirst = True

    def drive(self, right_value, left_value):
        if self.isFirst:
            self.wakeup()
        
        wiringpi.digitalWrite(self.pinRight1, right_value)
        wiringpi.pwmWrite(self.pinRight2, 320)
        wiringpi.digitalWrite(self.pinLeft1, left_value)
        wiringpi.pwmWrite(self.pinLeft2, 320)

    def goForward(self):
        self.drive(wiringpi.GPIO.LOW, wiringpi.GPIO.LOW)

    def goBack(self):
        self.drive(wiringpi.GPIO.HIGH, wiringpi.GPIO.HIGH)

    def turnLeft(self):
        self.drive(wiringpi.GPIO.LOW, wiringpi.GPIO.HIGH)

    def turnRight(self):
        self.drive(wiringpi.GPIO.HIGH, wiringpi.GPIO.LOW)

    def command(self, c):
        if c == 'q':
            # Qiut
            print('Qiut')
            self.quit()
        elif c == 'f':
            # goForward
            print('goForward')
            self.goForward()
        elif c == 'b':
            # goBack
            print('goBack')
            self.goBack()
        elif c == 'l':
            # left turn
            print('left turn')
            self.turnLeft()
        elif c == 'r':
            # right turn
            print('righ turn')
            self.turnRight()
        else:
            # stop
            print('stop')
            self.quit()

# end of class

# main
PIN_RIGHT_1 = 5
PIN_RIGHT_2 = 12
PIN_LEFT_1 = 6
PIN_LEFT_2 = 13

md = MotorDriver()
md.setPin(PIN_RIGHT_1, PIN_RIGHT_2, PIN_LEFT_1, PIN_LEFT_2)

try:
    # endless loop
    while True:
        # wait to enter command
        c = raw_input('> ')
        md.command(c)
    except KeyboardInterrupt:
        # exit the loop, if key Interrupt
        pass

#md.goForward()
#time.sleep(2)

#md.goBack()
#time.sleep(2)

#md.turnLeft()
#time.sleep(2)

#md.turnRight()
#time.sleep(2)

md.quit()
# end of main
