cmake_minimum_required(VERSION 3.29)
project(online_judge C)

set(CMAKE_C_STANDARD 11)

include_directories(.)
include_directories(src)

add_executable(online_judge
    src/PascalsTriangle2.c)
