#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


def start_node():
    rospy.init_node('detect_pump')
    rospy.loginfo('detect_pump node started')
    rospy.Subscriber("/front_cam/camera/image", Image, process_image)
    rospy.spin()

def process_image(msg):
    bridge = CvBridge()
    orig = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow('IMAGEM RECEBIDA', orig)
    cv2.waitKey(1)

if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass