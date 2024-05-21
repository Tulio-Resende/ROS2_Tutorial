#!src/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateStatus
from my_robot_interfaces.srv import SetLed

class LedPanelNode(Node):

    def __init__(self):
        super().__init__("led_panel")
        self.timer_ = self.create_timer(1.0, self.send_led_status)
        self.led_panel_server_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.led_panel_publisher_ = self.create_publisher(LedStateStatus, "led_panel_state", 10)
        self.get_logger().info("Led Panel Node has been started")

    def send_led_status(self):
        pass

    def callback_set_led(self, request, response):

        msg = LedStateStatus()

        msg.z = request.led_number
        self.led_panel_publisher_.publish(msg)
        self.get_logger().info(str(request.state))

        response.success = True

        return response

def main(args = None):

    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()