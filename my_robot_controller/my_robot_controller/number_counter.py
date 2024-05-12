#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_srvs.srv import SetBool


class NumberCounterNode(Node):
    def __init__(self):
        self.counter = 0
        super().__init__("number_counter")
        self.number_counter_publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.number_counter_callback_ = self.create_subscription(Int64,"/number",self.number_counter_callback, 10)
        self.server_ = self.create_service(SetBool,"reset_count",self.callback_reset_number_counter)
        self.get_logger().info("Number Counter Node has been started")

    def callback_reset_number_counter(self, request, response):
        if request.data == True:
            self.counter = 0
            response.success = True
        return response
    
    def number_counter_callback(self, number: Int64):
        msg = Int64()
        self.counter += number.data
        msg.data =  self.counter
        self.number_counter_publisher_.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()