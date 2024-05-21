cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)


# É PRECISO ADICIONAR ESSA LINHA E COLOCAR UMA NOVA MSG A CADA VEZ QUE CRIAR UMA NOVA
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/HardwareStatus.msg"
  "msg/LedStateStatus.msg"
  "srv/ComputeRectangleArea.srv"
  "srv/SetLed.srv"
)
# É PRECISO ADICIONAR ESSA LINHA TB
ament_export_dependencies(rosidl_default_runtime)

ament_package()
