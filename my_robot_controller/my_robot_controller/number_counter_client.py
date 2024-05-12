#!src/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from functools import partial

class NumberCounterClientNode(Node):
    def __init__(self):
        super().__init__("numer_counter_client")
        self.call_number_counter(True)

    def call_number_counter(self, data):
        client = self.create_client(SetBool, "reset_count")

        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for the reset_count Server...")
        
        request = SetBool.Request()
        request.data = data

        future = client.call_async(request)
        # future.add_done_callback(partial(self.callback_number_counter, data=data))

    
    # def callback_number_counter(self, future, data):
    #     try:
    #         response = future.result()
    #         self.get_logger().info(str(response.success))
    #     except Exception as e:
    #         self.get_logger().error("Service call fail %r" %(e,))



def main(args= None):
    rclpy.init(args=args)
    node =NumberCounterClientNode()
    rclpy.spin(node)
    rclpy.shutdown()