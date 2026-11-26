# SPDX-FileCopyrightText: 2026 Kazuki Nakatomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
#from std_msgs.msg import Int16
from person_msgs.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()
node = Node("listener")


def cb(msg):                                           #メッセージが届くたびに呼ばれる
    node.get_logger().info("Listen: %s" % msg)    #msgの中身をログとして表示     #変更: メッセージ全体を文字列で表示


def main():
    sub = node.create_subscription(Person, "person", cb, 10)  #型、トピック名、コールバック、キュー長   #変更: 型とトピック名
    rclpy.spin(node)
