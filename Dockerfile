FROM ros:noetic

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git