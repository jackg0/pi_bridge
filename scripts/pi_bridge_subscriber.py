#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import Int32


GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
pwm.start(75)

try:
	def callback(data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		pwm.ChangeDutyCycle(data.data)

	def listener():

		rospy.init_node('pi_bridge_subscriber', anonymous=True)

		rospy.Subscriber("pwm_transfer", Int32, callback)

		rospy.spin()

	if __name__ == '__main__':
		listener()
except KeyboardIntterupt:
	GPIO.cleanup()
