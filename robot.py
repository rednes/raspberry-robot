#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

class ta7291:
    def __init__(self, gpio1, gpio2):
        # GPIO端子の設定
        self.gpio1 = gpio1
        self.gpio2 = gpio2
        # GPIO出力モードを1に設定する
        GPIO.setup(gpio1, GPIO.OUT)
        GPIO.setup(gpio2, GPIO.OUT)

    def positive(self):
        # モーターを正回転する
        GPIO.output(self.gpio1, True)
        GPIO.output(self.gpio2, False)

    def negative(self):
        # モーターを正回転する
        GPIO.output(self.gpio1, False)
        GPIO.output(self.gpio2, True)

class robot:
    def __init__(self, l_motor, r_motor):
        self.l_motor = l_motor
        self.r_motor = r_motor

    def go(self):
        # 左右のモーターを正回転する
        self.l_motor.positive()

    def left_turn(self):
        self.r_motor.positive()

    def right_turn(self):
        self.r_motor.negative()


GPIO.setmode(GPIO.BCM)

if __name__=='__main__':
    # ロボット初期化
    r = robot(ta7291(14, 15), ta7291(23, 24))

    # 引数
    param = sys.argv

    # # 第1引数
    # # go : 前進
    # order = param[1]

    # # 第2引数 秒数
    # second = int(param[2])

    # if order == "go":
    #     print(str(second)+"秒前進")
    #     r.go()
    #     time.sleep(second)

    r.go()
    time.sleep(5)
    r.left_turn()
    time.sleep(5)
    r.right_turn()
    time.sleep(5)
    
GPIO.cleanup()
