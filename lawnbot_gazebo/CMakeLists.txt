cmake_minimum_required(VERSION 3.5)
project(lawnbot_gazebo)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

######################################################################################

# FIND AMENT DEPENDENCIES

######################################################################################

find_package(ament_cmake REQUIRED)
find_package(lawnbot_description REQUIRED)
find_package(gazebo_ros REQUIRED)
# find_package(joint_state_publisher REQUIRED) # this errors out on foxy for some reason? not necessary to run :shrug:
find_package(robot_state_publisher REQUIRED)

######################################################################################

# INSTALL

######################################################################################

install(DIRECTORY
	launch
	DESTINATION share/${PROJECT_NAME}/
)

######################################################################################

# TESTING

######################################################################################

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
