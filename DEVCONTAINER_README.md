# setup

```dockerfile
FROM ubuntu:22.04

# Define build-time argument
ARG UID
ARG UNAME

# Set environment variable
ENV UID=${UID}
ENV UNAME=${UNAME}

COPY .devcontainer/sys-requirements.txt .devcontainer/python-requirements.txt ./
RUN apt update && xargs -a sys-requirements.txt apt install -y

RUN useradd --uid $UID --create-home -s /bin/bash $UNAME
RUN usermod -aG sudo $UNAME
RUN echo "$UNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

```json
{
	"image": "hfagent-devcontainer:1.0.0",
	"runArgs": [
		"--name", "hfagent-devcontainer"
	],
	"workspaceFolder": "/home/${localEnv:USER}",
	"workspaceMount": "source=${localWorkspaceFolder},target=/home/${localEnv:USER},type=bind,consistency=cached",
	"remoteUser": "${localEnv:USER}",
	"customizations": {
		"vscode": {
			"extensions": [
				"eamodio.gitlens",
				"GitHub.vscode-pull-request-github",
				"GitHub.copilot",
				"GitHub.copilot-chat",
				"GitHub.vscode-github-actions",
				"shalldie.background",
				"ms-azuretools.vscode-docker",
				"ms-python.python",
				"kamikillerto.vscode-colorize",
				"trond-snekvik.simple-rst",
				"njpwerner.autodocstring"
			],
			"settings": {
				"python.pythonPath": "/usr/local/bin/python"
			}
		}
	}
}
```

```sh
docker build \
	--build-arg UID=$(id -u) \
	--build-arg UNAME=$(whoami) \
	-t hfagent-devcontainer:1.0.0 \
	-f .devcontainer/Dockerfile \
	.
```

Run `Dev Containers: Reopen in Container`, this will find the image just build, create a different one (`vsc-hfagent-...` ?!) and run it.

```sh
$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED              STATUS              PORTS     NAMES
4ac78c801ba1   hfagent-devcontainer:1.0.0   "/bin/sh -c 'echo Co…"   About a minute ago   Up About a minute             hfagent-devcontainer
```

# docker installation

install docker and access the devcontainer's host docker engine, not a new docker engine inside the devcontainer.

```sh
RUN apt update && apt install -y sudo curl

RUN install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt update \
    && apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```json
	"mounts": [
		"source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind"
	],
	"postStartCommand": "sudo chown ${localEnv:USER}:docker /var/run/docker.sock && sudo chmod 660 /var/run/docker.sock",
```

With these specs, it is possible to run `Dev Containers: Reopen in Container` and have access to the host docker engine, both when the devcontainer is running and when it is stopped.

# troubleshooting

Changes to Dockerfile require deleting the container and the vsc image and rebuilding the image. Reopening will run the container. Changes to devcontainer.json require stopping the container (which will remove it, see spec in devcontainer.json) and reopening.

# sources

- [devcontainer.json only applies when 'Reopen in Container'](https://github.com/microsoft/vscode-remote-release/issues/4190#issuecomment-745972100)

# gh-issues

- [name devcontainer image](https://github.com/microsoft/vscode-remote-release/issues/2485)
- [localEnv:UID not working](https://github.com/microsoft/vscode-remote-release/issues/6834)
- [Can't use existing image](https://github.com/microsoft/vscode-remote-release/issues/4229)
