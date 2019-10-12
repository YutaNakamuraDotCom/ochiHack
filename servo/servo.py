import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO4を制御パルスの出力に設定
gp_out = 14
GPIO.setup(gp_out, GPIO.OUT)

#GPIO.PWM( [ピン番号] , [周波数Hz] )
servo = GPIO.PWM(gp_out, 50)

#パルス出力開始。　servo.start( [デューティサイクル 0~100%] )
servo.start(0)
#time.sleep(1)

for i in range(1):
    #デューティサイクルの値を変更することでサーボが回って角度が変わる。
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)


servo.stop()
GPIO.cleanup()
