#!usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

from functools import partial

class AddTwoIntsClientNode(Node):

    def __init__(self):
        super().__init__("add_two_ints")
        self.get_logger().info("Add Two Ints Client Node has been created")
        self.call_add_two_ints_server(6,7)
        

    def call_add_two_ints_server(self, a, b):

        client = self.create_client(AddTwoInts, "add_two_ints")

        while not client.wait_for_service(1.0): #Aguarda a conexão com o servidor ser estabelecida por 1s
            self.get_logger().warn("waiting for the server...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)  #manda o request assincrono para o servidor
        future.add_done_callback(partial(self.callback_add_two_ints, a=a, b=b)) #A variável future vai receber a resp. assim que o servidor enviar e essa função chama o callback quando isso acontecer

    def callback_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + "+" + str(b) + "=" + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call fail %r" %(e,))


def main(args = None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()