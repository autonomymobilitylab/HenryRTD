Cameras
=======

A **Blackfly S** camera is installed inside behind the dashboard.

* Resolution: 2048 x 1536 (3.2 MP)
* Max frame rate: 55 fps
* USB3

.. _usage:

Usage
-----

The camera publishes to the topics ``/flir_camera_driver/image_raw`` and ``/flir_camera_driver/image_raw/compressed``.
From the image_transport package, a debayer node is used to get a compressed color image from the camera.

To view the camera feed, run ``rqt_image_view`` and select the topic ``/flir_camera_driver/image_raw/compressed``:

.. code-block:: bash
  ros2 run rqt_image_view rqt_image_view

Launch the camera driver with ``camera.launch.py`` in the common launch repository (see :doc:`platform_usage` for more details).

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
   ``ros2 launch spinnaker_camera_driver driver_node.launch.py 'camera_type:=blackfly_s' 'serial:="SERIAL NUMBER HERE"'``

With the spinnaker_camera_driver's own launch file, the camera might not start publishing compressed color images from BayerRGB8 right away, and does not have all possible configs available. Use our own camera launch file for these.