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


