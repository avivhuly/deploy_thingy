from enum import Enum
from pydantic import BaseModel

class OperatingSystem(Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    
class ContainerEngine(Enum):
    DOCKER = "docker"
    PODMAN = "podman"

class ComposeEngine(Enum):
    DOCKER_COMPOSE = "docker-compose"
    PODMAN_COMPOSE = "podman-compose"

class Environment(BaseModel):
    os: OperatingSystem
    container_engine: ContainerEngine
    compose_engine: ComposeEngine