cmake_minimum_required(VERSION 2.8.3)
project(moose_gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roslaunch
)

find_package(gazebo REQUIRED)

catkin_package(
  CATKIN_DEPENDS gazebo_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

roslaunch_add_file_check(launch/moose_world.launch)
