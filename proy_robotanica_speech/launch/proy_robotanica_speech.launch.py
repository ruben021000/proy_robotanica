from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='proy_robotanica_speech',
            executable='Proy_robotanica_Speech',
            output='screen'),
    ])