# Battery Status Package
### Author: Harry O'Brien
### Created: 2022-09-01

## Description
Publishes battery information from the laptop to the BatteryStatus topic.

## Build
- `catkin_make`
- `source ./devel/setup.sh`

## Run
##### Terminal 1:
- `roscore`

##### Terminal 2:
- `rosrun battery_status battery_pub`