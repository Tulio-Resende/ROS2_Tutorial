#!src/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):

    def __init__(self):
        super().__init__("battery_node")
        self.battery_state = "off"
        self.timer_ = 0
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("The Battery Node has been started")

    def timer_callback(self):
        self.get_logger().info('Timer:' + str(self.timer_))
        
        if self.battery_state == "off" and self.counter_%4 == 0:
            self.call_set_led(3,"on")
            self.battery_state = "on"
            self.counter_ = 0
            self.get_logger().info("The battery is low")
        elif self.battery_state == "on" and self.counter_%6 == 0:
            self.call_set_led(0, "off")
            self.counter_ = 0
            self.battery_state = "off"
            self.get_logger().info("The battery is full")
        else:
            self.get_logger().info("The battery status is OK")

        self.timer_ += 1
        self.counter_ += 1

    def call_set_led(self, led_number, state):
        self.client_ = self.create_client(SetLed, "set_led")

        while not self.client_.wait_for_service(1.0):
            self.get_logger().info("Waiting for the set_led Server...")

        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        future = self.client_.call_async(request)


def main(args = None):

    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()
