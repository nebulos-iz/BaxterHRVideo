sleep 2

e1="images/eye_contact.png"  
e2="images/eyes_closed.png"
e3="images/gaze_end.png"  
e4="images/gaze_middle.png"
e5="images/gaze_start.png"
e6="images/gaze_away_middle.png"
e7="images/gaze_away_end2.png"

b="images/black.png"


timestep=0.1

blink=( $e1 $e2 $e1 )
look_away=( $e1 $e5 $e6 $e7 )
look_down=( $e1 $e5 $e4 $e3 )
empty=($b)

recording="recordings/crazy2.rec"

for image in ${empty[@]}
do
	echo "===================" $image
	rosrun baxter_examples xdisplay_image.py -f $image 1>/dev/null
done


rosrun baxter_examples joint_trajectory_file_playback.py -f $recording
