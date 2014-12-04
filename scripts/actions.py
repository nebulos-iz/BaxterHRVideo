import rospy

import cv2
import cv_bridge

import sys
#from joint_trajectory_file_playback import Trajectory

from sensor_msgs.msg import (
    Image,
)

# PARAMETERS
framerate=1



rospy.init_node('baxter_video_actions', anonymous=True)
pub = rospy.Publisher('/robot/xdisplay', Image, latch=True)

def send_image(path): 
    img = cv2.imread(path)
    msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
    pub.publish(msg)


def display_images(paths): 
    for p in paths: 
        send_image(p)
        rospy.sleep(framerate)


def play_action(filename): 
    traj = Trajectory()
    traj.parse_file(path.expanduser(args.file))
    #for safe interrupt handling
    rospy.on_shutdown(traj.stop)
    traj.start()
    result = traj.wait()


    
if __name__ == '__main__':
    sys.exit(main())
