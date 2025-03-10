FROM ubuntu:22.04

# Define build-time argument
ARG USRID
ARG USRNAME

# Set environment variable
ENV USRID=${USRID}
ENV USRNAME=${USRNAME}

COPY .devcontainer/sys-requirements.txt .devcontainer/python-requirements.txt ./
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt update && xargs -a sys-requirements.txt apt install -y

RUN useradd --uid $USRID --create-home -s /bin/bash $USRNAME
RUN usermod -aG sudo $USRNAME
RUN echo "$USRNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Docker Installation ##########################################################
RUN install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt update \
    && apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
