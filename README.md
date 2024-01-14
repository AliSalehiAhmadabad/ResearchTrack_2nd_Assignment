Research Track Second Assignment
=================================

Author: Ali Salehi Ahmadabad
-------------------------------------------------------
Student Number: S6110138 
-------------------------------------------------------
Related Professor: Mr. Carmine Tommaso Recchiuto
--------------------------------------------------------
The second assignment of the Research Track 1 course entails the creation of a new package that comprises three nodes. The primary function of these nodes is to govern the movement of a robot within a specified environment and concurrently collect relevant data.

The requirements of the question are:
- Create a new package, in which you will develop three nodes:
  
- (a) A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. Try to use the 
feedback/status of the action server to know when the target has been reached. The node also publishes the
robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the
topic /odom;

- (b) A service node that, when called, returns the coordinates of the last target sent by the user;

- (c) Another service node that subscribes to the robot’s position and velocity (using the custom message) and
implements a server to retrieve the distance of the robot from the target and the robot’s average speed.

- Create a launch file to start the whole simulation. Use a parameter to select the size of the averaging window of node (c)

  --------------------------------------------------------
  Abstract:

  1) We need to clone the repository of the question (https://github.com/CarmineD8/assignment_2_2023) that involves some scripts for robot movement, action files, gazebo and Rviz interfaces, ...
  2) We need to write 3 nodes as the question requires and put them in the scripts folder
  3) We need to write some msg and srv files (here we create 1 msg and 2 srv files)
  4) We need to modify the launch file
  5) We need to modify the CMakelist file to define msg and services that we wrote
  6) We need to make our codes executable
  7) We need to run this comment in the scripts folder terminal: $apt-get -y install xterm
  8) Finally in the package folder terminal we need to run this comment: $roslaunch assignment_2_2023 assignment1.launch
 
  --------------------------------------------------------
  


