#!/usr/bin/env python
# import power
import rospy
from sensor_msgs.msg import BatteryState

class BatteryObserver(): #BatteryObserver(power.PowerManagementObserver):
    def __init__(self, power_management):
        # super()
        self._pub = rospy.Publisher('BatteryState', BatteryState, queue_size=10)
        rospy.init_node('battery_pub', anonymous=True)

        # power_management.add_observer(self)

        # Filling in mock data
        self._msg = BatteryState()
        self._msg.voltage = 0.0
        self._msg.temperature = 29.4
        self._msg.current = -1.0
        self._msg.charge = 23.0
        self._msg.capacity = 30.0
        self._msg.design_capacity = 31.0
        self._msg.percentage = 0.65
        self._msg.power_supply_health = BatteryState.POWER_SUPPLY_HEALTH_GOOD
        self._msg.power_supply_technology = BatteryState.POWER_SUPPLY_TECHNOLOGY_LION
        self._msg.present = True

    def on_power_sources_change(self, power_management):
        # update message
        # self._msg.whatever = power_management.get_whatever()
    
        # publish message
        self._pub.publish(self._msg)


    def on_time_remaining_change(self, power_management):
        # update message
        # self._msg.whatever = power_management.get_whatever()
    
        # publish message
        self._pub.publish(self._msg)

if __name__ == '__main__':
    # p = power.PowerManagement()
    obs = BatteryObserver(None)


    # The code would normally look like this:
    """
    try:
        # Hold here until interrupted
        # The observer is async, so nothing has to happen here
        while not rospy.is_shutdown():
            pass

    except rospy.ROSInterruptException:
       pass

    finally:
        # p.remove_observer(o)
        exit(0)
    """

    # but just to fire some triggers:
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        obs.on_power_sources_change(None)
        obs.on_time_remaining_change(None)
        rate.sleep()