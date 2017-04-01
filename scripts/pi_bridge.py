#!/usr/bin/env python
NAME = 'pi_bridge_server'

# import the PiBridge service
from pi_bridge.srv import *
import rospy

def pi_bridge(req):
	print("Returning [x: %s, y: %s, z: %s]" % (req.a, req.b, req.c))
	PiBridgeResponse(rospy.Time.now())

def pi_bridge_server():
	rospy.init_node(NAME)
	s = rospy.Service('pi_bridge', PiBridge, pi_bridge)

	rospy.spin()

if __name__ == "__main__":
	pi_bridge_server()

