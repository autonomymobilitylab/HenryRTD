Velodyne VLP-32 Lidar
=======

A **Velodyne VLP-32** lidar is installed on top of the car's roof.

.. _usage:

Usage
-----

``velodyne_driver`` is the ROS2 driver for Velodyne devices. 
It reads the raw data and publishes ``/velodyne_packets`` topics (``velodyne_msgs/VelodyneScan``). 
Then, it was subscribed by ``velodyne_pointcloud`` and  ``velodyne_laserscan`` nodes, 
and they publish ``velodyne_points`` (``sensor_msgs/PointCloud2``) and ``scan`` (``sensor_msgs/LaserScan``) topics respectively.

.. _installation:

Installation
------------

To install the Spinnaker SDK and ROS2 driver:

1. Install the ROS2 drivers:
   ``sudo apt install ros-${ROS_DISTRO}-velodyne-*``
