#!/usr/bin/env python
NAME = 'add_two_ints_server'

# import the AddTwoInts service
from bridge_practice.srv import *
import rospy

def add_two_ints(req):
	print("Returning [x: %s, y: %s, z: %s]" % (req.a, req.b, req.c))
	AddTwoIntsResponse(rospy.Time.now())

def add_two_ints_server():
	rospy.init_node(NAME)
	s = rospy.Service('add_two_ints', AddTwoInts, add_two_ints)

	rospy.spin()

if __name__ == "__main__":
	add_two_ints_server()

