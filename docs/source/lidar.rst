#####################
Lidar
#####################

A **Velodyne VLP-32** lidar is installed on top of the car's roof.

* Measurement Range: 200 m
* Range Accuracy: Up to ±3 cm (Typical)1
* Horizontal Field of View: 360°
* Vertical Field of View: 40° (-25° to +15°)
* Minimum Angular Resolution (Vertical): 0.33° (non-linear distribution)
* Angular Resolution (Horizontal/Azimuth): 0.1° to 0.4°
* Rotation Rate: 5 Hz to 20 Hz

.. _usage:

Usage
=====

``velodyne_driver`` is the ROS2 driver for Velodyne devices. 
It reads the raw data and publishes ``/velodyne_packets`` topics (``velodyne_msgs/VelodyneScan``). 

It is subscribed by ``velodyne_pointcloud`` and  ``velodyne_laserscan`` nodes, 
and they publish ``velodyne_points`` (``sensor_msgs/PointCloud2``) and ``scan`` (``sensor_msgs/LaserScan``) topics respectively.

``velodyne`` package launches both ``velodyne_driver`` and ``velodyne_pointcloud`` nodes.

Configuring parameters
----------------------
The velodyne lidar has two configuration files. 

* To configure the velodyne driver, update the params in the ``VLP32C-velodyne_driver_node-params.yaml`` file.
* To configure the velodyne pointcloud, update the params in the ``VLP32C-velodyne_transform_node-params.yaml`` file.

More information about the params and descriptions can be found in the ROS wiki pages (link in the resources section). 
Make sure to build the packages after updating the param file.

.. _installation:

Installation
============

Run the following command in a new terminal to install the ROS2 driver and all the related packages for the velodyne lidar.

1. The terminal command to install all the necessary packages is:
   ``sudo apt install ros-${ROS_DISTRO}-velodyne-*``
2. To test the installation, launch the package using:
   ``ros2 launch velodyne velodyne-all-nodes-VLP32C-launch.py``

.. _resources:

Resources
=========

For the detailed official information about the ROS-2 drivers for velodyne, refer the following web pages. The ROS wiki pages have detailed description for the configuration parameters.

1. Github repository (**ros2** branch): `Link <https://github.com/ros-drivers/velodyne>`_

2. ROS wiki for velodyne_driver: `Link <https://index.ros.org/p/velodyne_driver/>`_

3. ROS wiki for velodyne_pointcloud: `Link <https://index.ros.org/p/velodyne_pointcloud/github-ros-drivers-velodyne/#humble>`_

4. Sensor datasheet: `Internal link <https://aaltofi.sharepoint.com/:b:/r/sites/AMLab2/Shared%20Documents/02-Henry/Technical%20documentation/Datasheets/63-9378_Rev%20D_ULTRA%20Puck_VLP-32C_Datasheet_Web.pdf?csf=1&web=1&e=qq59Sq>`_


