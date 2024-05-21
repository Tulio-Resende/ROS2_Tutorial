// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:msg/LedStateStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE_STATUS__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/msg/detail/led_state_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_LedStateStatus_z
{
public:
  explicit Init_LedStateStatus_z(::my_robot_interfaces::msg::LedStateStatus & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::msg::LedStateStatus z(::my_robot_interfaces::msg::LedStateStatus::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::msg::LedStateStatus msg_;
};

class Init_LedStateStatus_y
{
public:
  explicit Init_LedStateStatus_y(::my_robot_interfaces::msg::LedStateStatus & msg)
  : msg_(msg)
  {}
  Init_LedStateStatus_z y(::my_robot_interfaces::msg::LedStateStatus::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_LedStateStatus_z(msg_);
  }

private:
  ::my_robot_interfaces::msg::LedStateStatus msg_;
};

class Init_LedStateStatus_x
{
public:
  Init_LedStateStatus_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LedStateStatus_y x(::my_robot_interfaces::msg::LedStateStatus::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_LedStateStatus_y(msg_);
  }

private:
  ::my_robot_interfaces::msg::LedStateStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::msg::LedStateStatus>()
{
  return my_robot_interfaces::msg::builder::Init_LedStateStatus_x();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATE_STATUS__BUILDER_HPP_
