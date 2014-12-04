sleep 2

e1="images/eye_contact.png"  
e2="images/eyes_closed.png"
e3="images/gaze_end.png"  
e4="images/gaze_middle.png"
e5="images/gaze_start.png"


timestep=0.1

#rosrun baxter_examples xdisplay_image.py -f $e1
#sleep $timestep 
rosrun baxter_examples xdisplay_image.py -f $e5 
#sleep $timestep 
#rosrun baxter_examples xdisplay_image.py -f $e4 
#sleep $timestep 
rosrun baxter_examples xdisplay_image.py -f $e3 
rosrun baxter_examples joint_trajectory_file_playback.py -f reaching2.rec
