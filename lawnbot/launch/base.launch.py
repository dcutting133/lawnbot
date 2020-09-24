import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.substitutions import EnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

#import xarco

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_dir = os.path.join(get_package_share_directory('lawnbot_description'), 'urdf')
    urdf_file = os.path.join(urdf_dir, 'lawnbot.urdf')
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    #xacro_file = os.path.join(urdf_dir, 'test-desc.urdf.xacro')
    #doc = xacro.process_file(xacro_file)
    #robot_desc = doc.toprettyxml(indent='  ')
    # https://answers.ros.org/question/361623/ros2-robot_state_publisher-xacro-python-launch/

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_desc,
            }]),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        ),
    ])
