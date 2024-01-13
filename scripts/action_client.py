#!/usr/bin/env python3

import rospy
import actionlib
import actionlib.msg
import assignment_2_2023.msg
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
from std_srvs.srv import SetBool
from actionlib_msgs.msg import GoalStatus
from assignment_2_2023.msg import Velocity
from assignment_2_2023.msg import PlanningAction, PlanningGoal, PlanningResult

def publish_position_velocity(pub, msg):
    # Extract current position and velocity from the Odometry message
    current_pos = msg.pose.pose.position
    current_vel_linear = msg.twist.twist.linear
    current_vel_angular = msg.twist.twist.angular

    # Create a new Vel message with the current position and velocity
    pos_and_vel = Velocity()
    pos_and_vel.pos_x = current_pos.x
    pos_and_vel.pos_y = current_pos.y
    pos_and_vel.vel_x = current_vel_linear.x
    pos_and_vel.vel_z = current_vel_angular.z

    # Publish the Vel message
    pub.publish(pos_and_vel)

def handle_goal_commands(pub, client, goal_cancelled):
    while not rospy.is_shutdown():
        # Subscribe to /odom topic and publish position and velocity
        rospy.Subscriber("/odom", Odometry, lambda msg: publish_position_velocity(pub, msg))

        # Get user command
        command = input("Press 'n' to set a target or 'c' to cancel it: ")

        # Get current target position
        target_pos_x = rospy.get_param('/des_pos_x')
        target_pos_y = rospy.get_param('/des_pos_y')

        # Create a new goal with the current target position
        goal = assignment_2_2023.msg.PlanningGoal()
        goal.target_pose.pose.position.x = target_pos_x
        goal.target_pose.pose.position.y = target_pos_y
        rospy.loginfo("target: target_x = %f, target_y = %f", target_pos_x, target_pos_y)

        if command == 'n':
            try:
                # Get new goal coordinates from user
                input_x = float(input("Enter x: "))
                input_y = float(input("Enter y: "))
            except ValueError:
                rospy.logwarn("Invalid input!")
                continue

            # Update target position parameters and the goal
            rospy.set_param('/des_pos_x', input_x)
            rospy.set_param('/des_pos_y', input_y)
            goal.target_pose.pose.position.x = input_x
            goal.target_pose.pose.position.y = input_y

            # Send the new goal to the action server
            client.send_goal(goal)
            goal_cancelled[0] = False

        elif command == 'c':
            if not goal_cancelled[0]:
                # Cancel the current goal if there is one
                goal_cancelled[0] = True
                client.cancel_goal()
                rospy.loginfo("Target has been cancelled")
            else:
                rospy.loginfo("There is no target to cancel")
        else:
            rospy.logwarn("Invalid command!")

        rospy.loginfo("Last target: target_x = %f, target_y = %f", goal.target_pose.pose.position.x, goal.target_pose.pose.position.y)

def main():
    # Initialize the node and start handling goal commands
    rospy.init_node('set_target_client')
    
    # Initialize publisher and action client
    pub = rospy.Publisher("/pos_vel", Velocity, queue_size=1)
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)
    client.wait_for_server()
    
    # Flag to track if the current goal has been cancelled
    goal_cancelled = [True]
    
    handle_goal_commands(pub, client, goal_cancelled)

if __name__ == '__main__':
    main()

