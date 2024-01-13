#!/usr/bin/env python3

import rospy
import math
from assignment_2_2023.msg import Velocity
from assignment_2_2023.srv import Average, AverageResponse

def get_distance_and_average_velocity(msg, distance, average_vel_x):
    # Get the desired x and y positions from the parameter server
    des_x = rospy.get_param('/des_pos_x')
    des_y = rospy.get_param('/des_pos_y')

    # Get the window size for the velocity calculation from the parameter server
    velocity_window_size = rospy.get_param('/window_size')

    # Get the actual x and y positions from the message
    actual_x = msg.pos_x
    actual_y = msg.pos_y

    # Calculate the distance between the desired and actual positions
    des_coordinates = [des_x, des_y]
    actual_coordinates = [actual_x, actual_y]
    distance[0] = math.dist(des_coordinates, actual_coordinates)

    # Calculate the average velocity
    if isinstance(msg.vel_x, list):
        vel_data = msg.vel_x[-velocity_window_size:]
    else:
        vel_data = [msg.vel_x]

    average_vel_x[0] = sum(vel_data) / min(len(vel_data), velocity_window_size)

def get_values(_, distance, average_vel_x):
    # Return a response with the distance and average velocity
    return AverageResponse(distance[0], average_vel_x[0])

def spin():
    rospy.spin()

def main():
    # Initialize the node with the name 'info_service'
    rospy.init_node('info_service')
    rospy.loginfo("Info service node initialized")

    # Initialize variables for the average velocity and distance
    average_vel_x = [0]
    distance = [0]

    # Provide a service named 'info_service', using the custom service type Ave_pos_vel
    rospy.Service("info_service", Average, lambda _: get_values(_, distance, average_vel_x))
    # Subscribe to the '/pos_vel' topic, using the custom message type Vel
    rospy.Subscriber("/pos_vel", Velocity, lambda msg: get_distance_and_average_velocity(msg, distance, average_vel_x))

    # Function to keep the node running
    spin()

if __name__ == "__main__":
    # Start the node
    main()

