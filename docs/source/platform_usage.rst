##############
Platform usage
##############

TODO: add content on how to start everything up and use the platform.

.. _getting started:

Getting started
===============
1. Create a folder named ``henry_platform_ws`` in home repository.
2. Run the following command inside the folder to clone the henry_ros2 repository: 
    ``git clone https://github.com/autonomymobilitylab/henry_ros2.git``
3. Build the ROS2 package using the following command:
    ``colcon build``
4. Source the bash file. To do this, add the following line to the `~/.bashrc` file:
    ``source ~/henry_platform_ws/install/setup.bash``
5. The Henry platform is ready! To launch the **master** launch file, execute the following command in a new terminal:
    ``ros2 launch henry_launch henry_bringup_launch.py``

.. _launch:

Launch files
============

Master launch file
------------------
Henry has a master launch file names ``henry_bringup_launch.py``. This launches all the sensor ros nodes, along with the transforms launch file.