#######
Cameras
#######

A **Blackfly S** camera is installed inside behind the dashboard.

* Resolution: 2448 x 2048 (5 MP)
* Max frame rate: 35 fps
* Color
* USB3

.. _usage:

Usage
=====

The camera publishes to the topics ``/flir_camera_driver/image_raw`` and ``/flir_camera_driver/image_raw/compressed``.
From the image_transport package, a debayer node is used to get a compressed color image from the camera.

To view the camera feed, run ``rqt_image_view`` and select the topic ``/flir_camera_driver/image_raw/compressed``:

.. code-block:: bash
  ros2 run rqt_image_view rqt_image_view

Launch the camera driver with ``camera.launch.py`` in the platform workspace repository (see :doc:`platform_usage` for more details).

Configuring camera settings
---------------------------

The camera driver uses two different config files: one for each camera type, and one for the camera settings of each camera.
The camera type configuration (for example `this one <https://github.com/ros-drivers/flir_camera_driver/blob/humble-devel/spinnaker_camera_driver/config/blackfly_s.yaml>`_) maps the Spinnaker nodes (the settings which you see in Spinview) to ROS parameters.
Then, they can be set in the launch file (like in `this example <https://github.com/ros-drivers/flir_camera_driver/blob/4d72f5972a48fdadc9916acdb82a8d0c51a87282/spinnaker_camera_driver/launch/driver_node.launch.py#L26>`_) or a separate config file.

* If a setting is available in the camera type config file, it can be set in the launch file or camera settings config.
* If a setting is not available in the camera type config file (but is shown in Spinview), it can be added to the camera type config file. See the `instructions in the flir_camera_driver repository <https://github.com/ros-drivers/flir_camera_driver/tree/humble-devel/spinnaker_camera_driver#how-to-develop-your-own-camera-configuration-file>`_ for how to do this, but in a nutshell: check what the name of the parameter is in Spinview, and add it to the in the same format as the others. Then, set the parameter in the launch file or camera settings config.

.. _installation:

Installation
============

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