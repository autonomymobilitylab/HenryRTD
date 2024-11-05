Cameras
=======

A **Blackfly S** camera is installed inside behind the dashboard.

.. _usage:

Usage
-----

The camera publishes to the topics ``/flir_camera_driver/image_raw`` and ``/flir_camera_driver/image_raw/compressed``.

.. _installation:

Installation
------------

To install the needed drivers for ROS2, follow the instructions at
https://github.com/ros-drivers/flir_camera_driver/ in the folder *spinnaker_camera_driver*
to install the Spinnaker SDK and ROS2 driver:

1. Install the Spinnaker SDK from the `Teledyne website <https://www.teledynevisionsolutions.com/support/support-center/software-firmware-downloads/iis/spinnaker-sdk-download/spinnaker-sdk--download-files/>`_ (default, not Python; see the above instructions for which version number to install).
2. Install the ROS2 drivers:
   ``sudo apt install ros-${ROS_DISTRO}-spinnaker-camera-driver``
3. Install the ROS2 image transport plugins to enable compression:
   ``sudo apt install ros-${ROS_DISTRO}-image-transport-plugins``
4. Test with the default launch parameters:
   ``ros2 launch spinnaker_camera_driver driver_node.launch.py 'camera_type:=blackfly' 'serial:="SERIAL NUMBER HERE"'``
