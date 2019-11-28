#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

is_unmanned = False

def callback(msg):
    global is_unmanned
    is_unmanned = msg.data
    if msg.data:
        rospy.loginfo("Keyswitch turned to UNMANNED")
    else:
        rospy.loginfo("Keyswitch turned to MANNED")

def keySwitch():
    global is_unmanned
    unmanned = rospy.Publisher('/teleop/unmanned', Bool, queue_size=10)
    manned = rospy.Publisher('/teleop/manned', Bool, queue_size=10)
    rospy.init_node('keyswitch', anonymous=True)
    rospy.Subscriber("set_unmanned", Bool, callback)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        unmanned.publish(not is_unmanned)
        manned.publish(is_unmanned)
        rate.sleep()

if __name__ == '__main__':
    try:
        keySwitch()
    except rospy.ROSInterruptException:
        pass
