#!/usr/bin/env python3

import rospy
from assignment_2_2023.msg import Velocity
from assignment_2_2023.srv import Input, InputResponse

def result_callback(_):
    # Create a response message
    response = InputResponse()
    
    # Set the x and y inputs in the response to the last desired positions
    last_des_x = rospy.get_param('/des_pos_x')
    last_des_y = rospy.get_param('/des_pos_y')
    
    response.input_x = last_des_x
    response.input_y = last_des_y

    # Return the response
    return response

def spin():
    rospy.spin()

def main():
    # Initialize the node with the name 'last_target_service'
    rospy.init_node('last_target_service')
    rospy.loginfo("Last target node initialized")

    # Provide a service named 'input', using the custom service type Input
    rospy.Service('input', Input, result_callback)

    # Keep the node running
    spin()

if __name__ == "__main__":
    main()

