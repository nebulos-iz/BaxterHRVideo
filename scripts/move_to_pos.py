#!/usr/bin/env python

import rospy
import baxter_interface
import sys


filename = sys.argv[1]

rospy.init_node('move_to_starting_pos')
limb = baxter_interface.Limb('left')

angles = limb.joint_angles()
print angles
start_pos = {}


with open(filename, 'r') as f:
	lines = f.readlines()
joint_names = lines[0].rstrip().split(',')
start_joints = lines[1].rstrip().split(',')
joint_pos = zip(joint_names, start_joints)
for joint, pos in joint_pos: 
	if joint != "time" and joint.startswith('left') and joint != 'left_gripper': 
		start_pos[joint] = float(pos)

print start_pos

limb.move_to_joint_positions(start_pos)
quit()

#time,left_s0,left_s1,left_e0,left_e1,left_w0,left_w1,left_w2,left_gripper,right_s0,right_s1,right_e0,right_e1,right_w0,right_w1,right_w2,right_gripper

#0.734823,0.681854459436,0.526155409644,0.14266021311,1.07570402628,-0.00536893275146,-0.234315565082,-0.185228179926,96.9648590088,0.657310766858,-0.904665168622,0.0655776786072,1.85956820799,-0.0671116593933,0.626631151135,-0.0203252454163,96.7914428711
