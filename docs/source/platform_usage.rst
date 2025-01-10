##############
Platform usage
##############

.. _getting started:

Getting started
===============
1. Create a folder named ``henry_platform_ws`` in home repository.

2. Run the following command inside the folder to clone the henry_ros2 repository: 

    ``git clone https://github.com/autonomymobilitylab/henry_ros2.git``

3. Build the ROS2 package using the following command:

    ``colcon build --symlink-install``

4. Source the bash file. To do this automatically when opening a terminal, add the following line to the `~/.bashrc` file:

    ``source ~/henry_platform_ws/install/setup.bash``

5. The Henry platform is ready! To launch the **master** launch file, execute the following command in a new terminal:

    ``ros2 launch henry_launch henry_bringup_launch.py``

.. _launch:

Launch files
============

Master launch file
------------------
Henry has a master launch file named ``henry_bringup_launch.py``. This launches all the sensor ros nodes, along with the transforms and Rviz launch files.

To launch the master launch file, run:

``ros2 launch henry_launch henry_bringup_launch.py``

Configuration files
===================

The sensors use separate configuration files for their parameters. These files are located in the ``config`` folder of the ``henry_launch`` package, and the launch files use these configuration files to set the parameters for the sensors at start-up.

.. _rviz

Rviz
====

There is a custom configuration and launch file for Rviz in the ``henry_launch`` package. To launch Rviz with the custom configuration, run:

``ros2 launch henry_launch rviz.launch.py config_file:=config.rviz``

To use your own Rviz configuration file, place it in ``~/henry_platform_ws/src/henry_launch/config/`` and replace ``config.rviz`` with the name of to your configuration file in the command above.

Rviz text overlays
------------------

The `rviz_2d_overlay_plugins <https://index.ros.org/p/rviz_2d_overlay_plugins/>`_ package is used to display text overlays in Rviz. It's installed with the following command:

``sudo apt install ros-${ROS_DISTRO}-rviz-2d-overlay-plugins``

The package allows text to be displayed in the Rviz window. Any overlayed text must be published as a `TextOverlay` message in its own topic. The text overlay messages are constructed in `rviz_text_overlay_publishers.py` in the `henry_launch` package. See the already published overlays for examples to create your own. Note that the publishers have been written to publish the text immediately when a subscribed message comes in, which means that writing many different messages for frequently-updated topics will be heavy on the car's CPU - be mindful of what you display.
