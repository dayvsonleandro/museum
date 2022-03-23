#!/usr/bin/python3

import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
import cv2
import imutils
import os
import vlc
import time

rospy.init_node('send_client_goal')

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

obra = ['monalisa.mp4', 'mulher_de_sombrinha.mp4',
        'nascimentos_de_venus.mp4', 'noite_estrelada.mp4', 'traicao_das_imagens.mp4']


def goto(px, py, oz, ow):

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.position.x = px
    goal.target_pose.pose.position.y = py
    goal.target_pose.pose.orientation.z = oz
    goal.target_pose.pose.orientation.w = ow

    client.send_goal(goal)
    client.wait_for_result()


def showvideo_1(name):
    capture = cv2.VideoCapture(os.path.dirname(__file__)+'/videos/' + name)

    while (capture.isOpened()):

        ret, frame = capture.read()
        cv2.namedWindow("Art", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Art", 426, 240)
        if (ret == True):
            cv2.imshow("Art", frame)
            if (cv2.waitKey(30) == ord('s')):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()


def showvideo(name):
    player = vlc.MediaPlayer(os.path.dirname(__file__)+'/videos/' + name)

    player.play()
    time.sleep(3)
    while player.is_playing():
        a = 0

    player.stop()


rospy.loginfo('Start')
# goto(0, 0, 0.7, 0.7)  # 1

goto(-5, 5, 0, 1)  # 2
rospy.loginfo('Welcome')

goto(-5, 0, 0, 1)  # 3
rospy.loginfo('First art')
showvideo(obra[0])

goto(-5, -5, 0.7, 0.7)  # 4
rospy.loginfo('Second art')
showvideo(obra[1])

goto(0, -5, 0.7, 0.7)  # 5
rospy.loginfo('Third art')
showvideo(obra[2])

goto(5, -5, 0.7, 0.7)  # 6
rospy.loginfo('Fourth art')
showvideo(obra[3])

goto(5, 0, 1, 0)  # 7
rospy.loginfo('Fifth art')
showvideo(obra[4])

# goto(0, 0, 0.7, 0.7)  # 8
# rospy.loginfo('Sixth art')

goto(0, 5, 0.7, 0.7)  # 9
# rospy.loginfo('Seventh art')


rospy.loginfo('End')
