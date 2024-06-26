#!src/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateStatus
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):

    def __init__(self):
        self.lead_states = [0, 0, 0]
        super().__init__("led_panel")
        self.led_panel_server_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.led_panel_publisher_ = self.create_publisher(LedStateStatus, "led_panel_state", 10)
        self.get_logger().info("Led Panel Node has been started")

    def callback_set_led(self, request, response):

        msg = LedStateStatus()

        if request.led_number > len(self.lead_states):
            response.success = False
            return response
        elif request.led_number == 3:
            msg.led_states = [0, 0, 1]
            self.get_logger().info(str(request.state))
            self.led_panel_publisher_.publish(msg)
            response.success = True
            return response
        elif request.led_number == 0:
            msg.led_states = [0, 0, 0]
            self.get_logger().info(str(request.state))
            self.led_panel_publisher_.publish(msg)
            response.success = True
            return response

def main(args = None):

    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()