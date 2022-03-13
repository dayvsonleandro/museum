#!/usr/bin/python3

import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()


def goto(px, py, oz, ow):

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.position.x = px
    goal.target_pose.pose.position.y = py
    goal.target_pose.pose.orientation.z = oz
    goal.target_pose.pose.orientation.w = ow

    client.send_goal(goal)
    client.wait_for_result()


rospy.loginfo('Start')
goto(0, 0, 0.5, 0.5)

goto(-5, 5, 0.5, 0.5)
rospy.loginfo('Welcome')

goto(-5, 0, 0.5, 0.5)
rospy.loginfo('First art')

goto(-5, -5, 0.5, 0.5)
rospy.loginfo('Second art')

goto(0, -5, 0.5, 0.5)
rospy.loginfo('Third art')

goto(5, -5, 0.5, 0.5)
rospy.loginfo('Fourth art')

goto(5, 0, 0.5, 0.5)
rospy.loginfo('Fifth art')

goto(0, 0, 0.5, 0.5)
rospy.loginfo('Sixth art')

goto(0, 5, 0.5, 0.5)
rospy.loginfo('Seventh art')


rospy.loginfo('End')
