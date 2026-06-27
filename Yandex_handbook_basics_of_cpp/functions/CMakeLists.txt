cmake_minimum_required(VERSION 3.20)
project(stupid_thing LANGUAGES CXX)

file(GLOB HEADER_FILES "*.h")
file(GLOB SOURCE_FILES "*.cpp")

add_executable(
    stupid_thing
    ${HEADER_FILES}
    ${SOURCE_FILES}
)