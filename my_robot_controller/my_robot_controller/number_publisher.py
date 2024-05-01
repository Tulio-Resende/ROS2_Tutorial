#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.timer = self.create_timer(0.5, self.send_number)
        self.number_publisher_ = self.create_publisher(Int64, "number",10)
        self.get_logger().info("Number Publisher Node has been started")

    def send_number(self):
        number = Int64()
        number.data = 10
        self.number_publisher_.publish(number)

def main(args = None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()