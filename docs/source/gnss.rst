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

The following table presents a description of the GNSS data attributes included in the topic information (values of which could be obtained by the terminal command ``ros2 topic echo /novatel/oem7/gps``):

.. table:: GNSS Topic Attributes

   +----------------------------+--------------------------------------------------------------------------+
   | Attribute                  | Description                                                              |
   +============================+==========================================================================+
   | status.header.stamp.sec    | The seconds part of the time when the GNSS message was recorded.         |
   +----------------------------+--------------------------------------------------------------------------+
   | status.header.stamp.nanosec| The fractional part of the timestamp in nanoseconds, adding precision to |
   |                            | the recorded time. Together with `sec`, it gives the exact time.         |
   +----------------------------+--------------------------------------------------------------------------+
   | status.header.frame_id     | The name of the coordinate frame for the GNSS data (e.g., 'gps', 'map'), |
   |                            | to which the measurement data are in reference to. An empty value means  |
   |                            | the data is in the default form (not referenced to any predefine frame)  |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellites_used     | The number of satellites whose signals were used to calculate the GNSS   |
   |                            | position fix. More satellites usually mean better accuracy.              |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellite_used_prn  | A list of Pseudo Random Numbers (PRNs) of satellites used for the fix.   |
   |                            | Each satellite has a unique PRN for identifying it.                      |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellites_visible  | The total number of satellites that the GNSS receiver could detect at    |
   |                            | the time of measurement, whether or not they were used for the fix.      |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellite_visible_pr| A list of Pseudo Random Numbers for all visible satellites. This includes|
   | n                          | satellites that were detected but not necessarily used for position      |
   |                            | calculation.                                                             |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellite_visible_z | Elevation angles (in degrees) of the visible satellites relative to the  |
   |                            | receiver. Higher values indicate satellites higher in the sky.           |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellite_visible_az| Azimuth angles (in degrees) showing the compass direction (0° - 360°)    |
   | imuth                      | where the visible satellites are located relative to the receiver.       |
   +----------------------------+--------------------------------------------------------------------------+
   | status.satellite_visible_sn| Signal-to-Noise Ratios (SNR) of the visible satellites. Higher SNR means |
   | r                          | better signal strength, which usually results in better accuracy.        |
   +----------------------------+--------------------------------------------------------------------------+
   | status.status              | A numerical code indicating the GNSS fix status. Refer to the            |
   |                            | `NovAtel BESTPOS Status Codes`_ for a description of each code.                                  |
   +----------------------------+--------------------------------------------------------------------------+
   | status.motion_source*      | Specifies the source of motion data (e.g., speed). It is represented by  |
   |                            | a numerical code that identifies the sensor or method used.              |
   +----------------------------+--------------------------------------------------------------------------+
   | status.orientation_source* | Specifies the source of orientation data (e.g., roll, pitch, yaw). This  |
   |                            | is represented by a numerical code.                                      |
   +----------------------------+--------------------------------------------------------------------------+
   | status.position_source*    | Specifies the source of position data (such as GNSS, odometry, or other  |
   |                            | localization methods), represented by a numerical code.                  |
   +----------------------------+--------------------------------------------------------------------------+
   | latitude                   | Latitude (in degrees) representing the receiver's north-south position   |
   |                            | on the Earth's surface. Positive values are north of the equator.        |
   +----------------------------+--------------------------------------------------------------------------+
   | longitude                  | Longitude (in degrees) representing the receiver's east-west position    |
   |                            | on the Earth's surface. Positive values are east of the prime meridian.  |
   +----------------------------+--------------------------------------------------------------------------+
   | altitude                   | Altitude (in meters) above mean sea level. Indicates the receiver's      |
   |                            | vertical position.                                                       |
   +----------------------------+--------------------------------------------------------------------------+
   | track                      | Direction of movement (in degrees) of the receiver relative to true      |
   |                            | north (i.e. heading). For example, 0° means moving north, 90° means east.|
   +----------------------------+--------------------------------------------------------------------------+
   | speed                      | The speed of the receiver's movement over the ground, measured in m/s    |
   +----------------------------+--------------------------------------------------------------------------+
   | climb                      | The rate of the receiver's vertical movement (climbing or descending),   |
   |                            | measured in m/s. Positive values indicate upward movement.               |
   +----------------------------+--------------------------------------------------------------------------+
   | pitch                      | The tilt angle (in degrees) of the receiver relative to the lateral axis |
   |                            | plane. Positive pitch indicates the front is pointing upwards.           |
   +----------------------------+--------------------------------------------------------------------------+
   | roll                       | The tilt angle (in degrees) of the reciever relative to the longitudinal |
   |                            | axis. Positive roll indicates tilting to the right.                      |
   +----------------------------+--------------------------------------------------------------------------+
   | dip                        | The angle (in degrees) between the of the receiver's horizontal plane and|
   |                            | the direction of the Earth's magnetic field at a given location. Positive|
   |                            | dip indicates magnetic field lines pointing downwards into the Earth's   |
   |                            | surface (common in the northern hemisphere).                             |
   +----------------------------+--------------------------------------------------------------------------+
   | time                       | GNSS-provided time (in epoch seconds). This timestamp is in Unix time    |
   |                            | format. It is useful for synchronizing data with other sensors.          |
   +----------------------------+--------------------------------------------------------------------------+
   | gdop                       | Geometric Dilution of Precision: A measure of overall accuracy based on  |
   |                            | satellite geometry (`DOP Guide`_). Lower values mean better accuracy.    |
   +----------------------------+--------------------------------------------------------------------------+
   | pdop                       | Position Dilution of Precision: Measures accuracy of 3D position.        |
   |                            | (`DOP Guide`_). Lower values indicate better position accuracy.          |
   +----------------------------+--------------------------------------------------------------------------+
   | hdop                       | Horizontal Dilution of Precision: Reflects accuracy of the horizontal    |
   |                            | position. (`DOP Guide`_). Lower values mean better horizontal accuracy.  |
   +----------------------------+--------------------------------------------------------------------------+
   | vdop                       | Vertical Dilution of Precision: Reflects accuracy of vertical position.  |
   |                            | (`DOP Guide`_). Lower values mean better vertical accuracy.              |
   +----------------------------+--------------------------------------------------------------------------+
   | tdop                       | Time Dilution of Precision: Reflects accuracy of time synchronization.   |
   |                            | (`DOP Guide`_). Lower values mean better timing accuracy.                |
   +----------------------------+--------------------------------------------------------------------------+
   | err                        | General estimate of the uncertainty in the position fix (in meters).     |
   +----------------------------+--------------------------------------------------------------------------+
   | err_horz                   | Estimated horizontal position error (in meters) which indicates the      |
   |                            | uncertainty in the latitude and longitude measurements.                  |
   +----------------------------+--------------------------------------------------------------------------+
   | err_vert                   | Estimated vertical position error (in meters) which indicates the        |
   |                            | uncertainty in the altitude measurements.                                |
   +----------------------------+--------------------------------------------------------------------------+
   | err_track                  | Estimated error (in degrees) in the calculated direction of travel       |
   |                            | (heading).                                                               |
   +----------------------------+--------------------------------------------------------------------------+
   | err_speed                  | Estimated error (in m/s) in the reported speed of the receiver.          |
   +----------------------------+--------------------------------------------------------------------------+
   | err_climb                  | Estimated error (in m/s) in the climb rate (vertical speed).             |
   +----------------------------+--------------------------------------------------------------------------+
   | err_time                   | Estimated error (in seconds) in the GNSS-provided time (accurate time    |
   |                            | synchronization is critical for sensor fusion and data alignment)        |
   +----------------------------+--------------------------------------------------------------------------+
   | err_pitch                  | Estimated error (in degrees) of the forward tilt angle (pitch            |
   |                            | measurement).                                                            |
   +----------------------------+--------------------------------------------------------------------------+
   | err_roll                   | Estimated error (in degrees) of the side-to-side tilt angle (roll        |
   |                            | measurement).                                                            |
   +----------------------------+--------------------------------------------------------------------------+
   | err_dip                    | Estimated error (in degrees) of inclination of the magnetic field (dip   |
   |                            | measurement).                                                            |
   +----------------------------+--------------------------------------------------------------------------+
   | position_covariance        | A 3x3 matrix that provides the statistical uncertainty for the position  |
   |                            | estimates along x, y, and z axes.                                        |
   +----------------------------+--------------------------------------------------------------------------+
   | position_covariance_type   | Indicates the type of covariance provided. A value of **2** corresponds  |
   |                            | to a diagonal position covariance matrix.                                |
   +----------------------------+--------------------------------------------------------------------------+

**NOTE**: Float values of **0.0** for corresponding attributes above may typically mean that no measurement was made. 
.. _NovAtel BESTPOS Status Codes: https://docs.novatel.com/OEM7/Content/Logs/BESTPOS.htm?Highlight=bestpos#SolutionStatus
.. _DOP Guide: https://en.wikipedia.org/wiki/Dilution_of_precision_(navigation) 
'*': numerical code guide not located

In addition, note that the **gps_msgs** package, which includes the **GPSFix** and **GPSStatus** message types, is yet to have a complete ROS 2 documentation page for the topic information. The most detailed available documentation is mainly from ROS 1 (from which the package was ported), which is partially applicable (albeit some differences to the message structure). For detailed information on the web for this topic, you can refer to the following resources:

1. Github repository (**humble** branch): https://github.com/novatel/novatel_oem7_driver/tree/humble

2. ROS Wiki: https://wiki.ros.org/novatel_oem7_driver 

3. ROS Index (**humble**): https://index.ros.org/r/novatel_oem7_driver/github-novatel-novatel_oem7_driver/#humble 

4. Commands and logs: https://docs.novatel.com/OEM7/Content/PDFs/OEM7_Commands_Logs_Manual.pdf
