#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class NumberCounterNode(Node):
    def __init__(self):
        self.counter = 0
        super().__init__("number_counter")
        self.number_counter_publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.number_counter_callback_ = self.create_subscription(Int64,"/number",self.number_counter_callback, 10)
        self.get_logger().info("Number Counter Node has been started")

    def number_counter_callback(self, number: Int64):
        self.get_logger().info(str(self.counter))
        msg = Int64()
        msg.data =  self.counter + number.data
        self.counter += 1
        self.number_counter_publisher_.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()