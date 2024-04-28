#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")

        self.time = self.create_timer(0.5, self.send_cmd_vel)

        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)  #Cria um publisher para publicar no tópico /turtle1/cmd_vel com o tipo de mensagem sendo Twist e com fila de 10
        self.get_logger().info("Draw Circle node has been started")

    def send_cmd_vel(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)
        #comentario


def main(args = None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":   #Serve para rodar o script direto do terminal
    main()