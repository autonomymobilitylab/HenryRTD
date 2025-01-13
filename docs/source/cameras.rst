#######
Cameras
#######

A **Blackfly S** camera is installed inside behind the dashboard.

* Model: `BFS-U3-50S5C <https://www.teledynevisionsolutions.com/en-gb/products/blackfly-s-usb3/?model=BFS-U3-50S5C-C&vertical=machine%20vision&segment=iis>`_
* Resolution: 2448 x 2048 (5 MP)
* Max frame rate: 35 fps
* Color
* USB 3.1 Gen 1
* Global shutter

.. _usage:

Usage
=====

The camera publishes bayer-format images. A debayer node from image_transport_plugins is used to get a color image from the camera.

Launch the camera driver with ``camera.launch.py`` in the platform workspace repository (see :doc:`platform_usage` for more details on the workspace). The launch file takes a single parameter file as its argument:

.. code-block:: bash

   ros2 launch henry_launch camera.launch.py parameter_file:=camera/front_camera_params.yaml

Replace ``front_camera_params.yaml`` with the parameter file for the setup that you want to launch. If you want to modify any parameters, make a separate parameter file. See :ref:`configuring_camera_settings` for more information on how to configure the camera settings.

Viewing the camera feed
-----------------------

To view the camera feed, either select the ``/<camera_name>/image_color`` topic in Rviz, or run ``ros2 run rqt_image_view rqt_image_view`` to view any of the image topics.

Published topics
----------------

``<camera_name>`` is the name of the camera, which is set in the parameter file. The name for the Blackfly S camera is ``front_camera``.

.. list-table:: Camera Topics
   :widths: 50 50 25
   :header-rows: 1

   * - Topic
     - Description
     - Source node
   * - ``/<camera_name>/camera_info``
     - Camera info message
     - Camera driver
   * - ``/<camera_name>/meta``
     - Camera exposure etc.
     - Camera driver
   * - ``/<camera_name>/image_raw``
     - Raw, bayer-format image
     - Camera driver
   * - ``/<camera_name>/image_color``
     - Debayered image, based on ``image_raw``
     - Debayering
   * - ``/<camera_name>/image_color/compressed``
     - Compressed version of ``image_color``
     - Debayering
   * - ``/<camera_name>/image_mono``
     - Monochrome version of ``image_color``
     - Debayering
   * - ``/<camera_name>/image_mono/compressed``
     - Monochrome of ``image_color/compressed``
     - Debayering

.. note::
   When using the camera, most probably the only topics you want to use are:

   * ``/<camera_name>/image_color`` (or ``image_mono`` if you don't need color)
   * ``/<camera_name>/image_color/compressed``
   * ``/<camera_name>/camera_info`` (this might be empty though, check if needed)

When recording, the **compressed** image is often the best choice.

The image_transport_plugins package automatically compresses the images without any configuration needed. The camera driver has been set to not publish ``image_raw/compressed`` and ``image_raw/theora``, but they can be easily included if needed.

.. _configuring_camera_settings:

Configuring camera settings
---------------------------

The camera driver uses three different config files:

* The driver parameter file, which is passed as an argument to the launch file. It has parameters for configuring a single camera, such as the camera serial number, which mapping file to use, and which camera settings file to use.

   * For example ``front_camera_params.yaml`` in the Henry platform workspace repository.
   * If you need to change camera settings for your own project, copy the parameter file, name it with your own name/project's name, and modify it as needed.

* The camera type -specific Spinnaker parameter mapping file, which maps the Spinnaker parameters ("Spinnaker nodes") available in Spinview to be configurable by the ROS driver.

   * Any parameter available in the Spinnaker SDK can be set in the ROS driver after it is added to this mapping file.
   * Mapping files for different cameras can be found in the `flir_camera_driver repository <https://github.com/ros-drivers/flir_camera_driver/tree/humble-devel/spinnaker_camera_driver/config>`_. We have made additions to the ``blackfly_s.yaml`` file, now called ``blackfly_s_spinnaker_param_mapping.yaml`` in the Henry platform workspace repository.
   * If a setting is not available in the camera type config file (but is shown in Spinview), it can be added to the camera type config file. See the `instructions in the flir_camera_driver repository <https://github.com/ros-drivers/flir_camera_driver/tree/humble-devel/spinnaker_camera_driver#how-to-develop-your-own-camera-configuration-file>`_ for how to do this, but in a nutshell: check what the name of the parameter is in Spinview, and add it to the in the same format as the others. Then, set the parameter in the launch file or camera settings config.

* The camera settings configuration file, which sets the camera settings given to the ROS driver by the parameter mapping file. Examples for these parameters can be found in the `flir_camera_driver example launch file <https://github.com/ros-drivers/flir_camera_driver/blob/4d72f5972a48fdadc9916acdb82a8d0c51a87282/spinnaker_camera_driver/launch/driver_node.launch.py#L26>`_.

   * For example ``front_camera_spinnaker_config.yaml`` in the Henry platform workspace repository.
   * If you need to change camera settings for your own project, copy the configuration file, name it with your own name/project's name, and modify it as needed.

In short, if you need to change camera settings, make a new camera Spinnaker SDK settings configuration file, change whatever you need to, and make a new parameter file (which is given as an argument to the camera launch file) which points to the new camera settings configuration file.

The camera driver has example values for the Spinnaker driver parameters and ready-made parameter mapping files for some cameras, and will try to use them if you don't provide ``config_file`` or ``parameter_mapping_file`` in the main parameter file. This is convenient for testing new cameras, but any long-term setups should get their own parameter mapping file and driver config file.


Troubleshooting
---------------

Some pain points when working with the camera driver:

* Do not trust ``ros2 topic hz`` to show the correct frame rate, especially for topics with large messages, such as images and point clouds. This might have something to do with the DDS QOS settings of ``ros2 topic hz``.
* The default driver does not do debayering. This means that when publishing in BayerRBG format, the image will be grayscale. To get a color image, our driver uses the ``image_proc`` package to debayer the image.

   * Documentation is still lacking, a good starting point is the `ROS 2 Rolling version of the image_proc package <https://docs.ros.org/en/rolling/p/image_proc/>`_ along with the old `ROS 1 documentation <http://wiki.ros.org/image_proc>`_ and the `source code for the ROS 2 Humble version <https://github.com/ros-perception/image_pipeline/tree/humble/image_proc>`_.

   * The default debayering algorithm (number 3) is best quality, but too slow to debayer a 5 MP image at 35 fps. The algorithm can be changed in the launch file. Number 0 is the fastest, and works with the Blackfly S camera.

   * Edge-aware algorithms (alg. numbers 1 and 2) can't be used with the Bayer pattern of the Blackfly S, at least on ROS 2 Humble. They only support Bayer GRBG8. The debayering will fall back to bilinear (the fastest algorithm).

   * The documentation for the debayering node seems to suggest that compressed images can be used, but setting the node's ``image_transport`` parameter to ``compressed`` does not do anything. Debayering will not work as well with compressed images, it assumes the image is in raw format.

* The current implementation only allows for one camera. The flir_camera_driver repository has a `launch file for multiple cameras <https://github.com/ros-drivers/flir_camera_driver/blob/humble-devel/spinnaker_camera_driver/launch/multiple_cameras.launch.py>`_ whose approach looks like it would be easy to implement in our own launch file.
* The camera driver prints the incoming raw image's FPS to the console when starting the camera. To my understanding, this is the same FPS as Spinview sees, and is not affected by ROS. On one occasion, the FPS was only about 25 Hz. If this happens again, I would check with another USB cable. The current cable is (maybe) 5 m long, which might be too long for USB 3.1 with the full 5MP image resolution of the Blackfly S.

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