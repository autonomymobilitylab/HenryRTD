Welcome to Henry's documentation!
===================================

**Henry** is a research platform vehicle at the Autonomy and Mobility laboratory at Aalto University.

.. image:: images/henry.jpg
  :width: 796
  :alt: The Henry vehicle at the lab.

.. note::

   This doc is under active development.

Contents
--------

.. toctree::

  system
  cameras
  lidar

Vehicle
--------

- Ford Focus (IV) 2019
  - 1.5L Diesel, 88kw

Sensor setup
------------

For a detailed diagram of the setup with connections, see :doc:`system diagram <system>`.

* :doc:`Camera <cameras>`

  * Blackfly S BFS-U3-31S4C-C
  * Resolution: 2048 x 1536

* Can-bus connections to 4 different can networks 

  * Possibility to be connected into 2 different can busses simultaneously 
  * Peak can-to-ethernet interface 

* :doc:`Lidar <lidar>` 

  * Velodyne Ultra Puck 80-VLP-32C-B 
  * Channels: 32 
  * Range: 200m 
  * Field of View
  
    * horizontal: 360°, vertical: 40° (-25° to +15 °) 

  * 3D LiDAR Data Points Generated: 
    
    * Single Return Mode:    ~600,000 points per second  
    * Dual Return Mode:     ~1,200,000 points per second 

* GPS & IMU 

  * PwrPak7D E2, with dual antenna installation (Tallysman VSP6337L) 
  * DGPS corrected (RTK capable device) 
  * Integrated inertial measure unit

Software
--------

* Ubuntu 22.04
* ROS2 Humble