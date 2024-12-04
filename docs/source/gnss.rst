GPS
=======

A **Novatel PwrPak7D** GPS unit (with **Tallysman VSP6337L** dual antennas)  is installed. While the GPS unit is in the trunk of the vehicle, the two antennas are located on the two rear corners of the vehicle roof.

.. _installation:

Installation
------------

The required ROS2 drivers were installed from https://github.com/novatel/novatel_oem7_driver/discussions/73 and executed as outlined below.

1. ROS2 driver installation:
 ``sudo apt-get install ros-humble-novatel-oem7-driver``
2. Verify installation by locating the package:
 ``ros2 pkg prefix novatel_oem7_driver``
3. Test the package using:
 ``ros2 launch novatel_oem7_driver oem7_net.launch.py oem7_ip_addr:=192.168.1.20 oem7_port:=3001 oem7_if:=Oem7ReceiverTcp``

NOTE: Parameters for the above launch file include:

* **192.168.1.20**: IP address of the GPS receiver (i.e. device location on local network)

* **3001**: Port number used for communication (listening for commands and sending data) with the GPS receiver (this is usually a value between 3001 and 3007 but the default port of 3001 should work)

* **Oem7ReceiverTcp**: Specifies that the interface type used to communicate with the GPS receiver is a TCP connection

.. _usage:

Usage
-----

The GPS publishes to the topic ``/novatel/oem7/gps``.

After launching the package (refer to step 3 under *Installation*), the following commands can be used to get the details of the ROS2 GPS messages:

1. Information on the GPS receiver's sensor data (position, velocity, accuracy, etc...):
 ``ros2 interface show gps_msgs/msg/GPSFix``
2. Information on the status and health information of the GPS receiver and its satellite signal:
 ``ros2 interface show gps_msgs/msg/GPSStatus``

.. _topic information:

Topic information
-----------------

The **gps_msgs** package, which includes the **GPSFix** and **GPSStatus** message types, is yet to have a dedicated ROS 2 documentation page for this topic. The most detailed available documentation is mainly from ROS 1 (from which the package was ported), which is partially applicable (albeit some differences to the message structure).
Thus, for detailed information on this topic, you can refer to the following resources:

1. Github repository (**humble** branch): https://github.com/novatel/novatel_oem7_driver/tree/humble

2. ROS Wiki: https://wiki.ros.org/novatel_oem7_driver 

3. ROS Index (**humble**): https://index.ros.org/r/novatel_oem7_driver/github-novatel-novatel_oem7_driver/#humble 

