#!/usr/bin/env python3     #indica ao SO qual interpreter deve ser utilizado para rodar o script (nesse caso o python 3)
import rclpy
from rclpy.node import Node #importa as funções do Node


class MyNode(Node):

    def __init__(self):
        super().__init__('first_node') #O super serve para herdar as funções da classe
        self.counter_ = 0

        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello ' + str(self.counter_))
        self.counter_ += 1 

def main(arg = None):
    rclpy.init(args=arg)

    node = MyNode() #Mantem o nó vivo (precisa matar com CTRL + C no terminal)
    rclpy.spin(node)
    rclpy.shutdown() #Mata o nó

if __name__ == '__main__':
    main()
