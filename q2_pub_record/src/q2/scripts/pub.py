#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('talker', String, queue_size=10)
    while not rospy.is_shutdown():
        hello_world = String()
        hello_world.data = "Hello, World!"
        pub.publish(hello_world)
        rospy.sleep(1)

if __name__ == '__main__':
    rospy.init_node('talker')
    talker()
