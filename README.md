# Battery Status Package
### Author: Harry O'Brien
### Created: 2022-09-01
### Using: ROS 2 Noetic

## Description
Publishes battery information from the laptop to the BatteryStatus topic. All of the information published is mock data and not actually read from the system. For a robot where accesing low-level information like this would (should) be intuitive and then easy enough to publish to the system to be read via Serial or over CAN etc.

Information on the data provided by BatteryState can be found [here](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/BatteryState.html).

## Deps
Assumes Python 3
requires the python package 'power':
    `pip install power`

## Build
- `catkin_make`
- `source ./devel/setup.sh`

## Run
##### Terminal 1:
- `roscore`

##### Terminal 2:
- `rosrun battery_status battery_pub.py`

##### Terminal 3:
- `rostopic echo BatteryState`