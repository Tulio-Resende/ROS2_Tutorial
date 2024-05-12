#!src/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus
from my_robot_interfaces.srv import ComputeRectangleArea

class HardawareStatusNode(Node):

    def __init__(self):
        super().__init__("hw_status_publisher")
        self.timer = self.create_timer(1.0, self.send_hardware_status)
        self.compute_area_ = self.create_service(ComputeRectangleArea, "compute_rectangle_area", self.callback_compute_area)
        self.hw_status_publisher_ = self.create_publisher(HardwareStatus, "hw_status", 10)
        self.get_logger().info("Hardware Status Node has been created")

    def send_hardware_status(self):
        msg = HardwareStatus()
        msg.temperature = 10
        msg.are_motors_ready = True
        if msg.are_motors_ready:
            msg.debug_message = "The motor is ready to operate"
        else:
            msg.debug_message = "The motor is not ready to operate!"
        
        self.hw_status_publisher_.publish(msg)

    def callback_compute_area(self, request, response):
        response.area = request.length*request.width
        self.get_logger().info(str(response.area))
        return response

        

def main(args=None):
    rclpy.init(args=args)
    node = HardawareStatusNode()
    rclpy.spin(node)
    rclpy.shutdown()