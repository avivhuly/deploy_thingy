from src.modles.modles import Environment, OperatingSystem, ContainerEngine, ComposeEngine
import platform
import shutil
import subprocess

def get_os() -> OperatingSystem:
    system = platform.system()
    if system == "Windows":
        return OperatingSystem.WINDOWS
    elif system == "Linux":
        return OperatingSystem.LINUX
    else:
        raise ValueError(f"Unsupported operating system: {system}")

def detect_container_runtime() -> ContainerEngine | None:
    for runtime in [engine.value for engine in ContainerEngine]:
        if shutil.which(runtime):
            try:
                subprocess.run(
                    [runtime, "info"],
                    capture_output=True, timeout=3, check=True
                )
                return ContainerEngine(runtime)
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                continue
    return None

def detect_compose_runtime() -> ComposeEngine | None:
    for runtime in [engine.value for engine in ComposeEngine]:
        if shutil.which(runtime):
            try:
                subprocess.run(
                    [runtime, "info"],
                    capture_output=True, timeout=3, check=True
                )
                return ComposeEngine(runtime)
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                continue
    return None

def detect_service(proj_name: str) -> bool:
    return subprocess.run(["systemctl", "cat", f"{proj_name}.service", "&>", "/dev/null"]).returncode == 0

def detect_environment() -> Environment:
    os = get_os()
    container_engine = detect_container_runtime()
    compose_engine = detect_compose_runtime()

    if container_engine is None:
        raise RuntimeError("No supported container engine found.")
    if compose_engine is None:
        raise RuntimeError("No supported compose engine found.")

    return Environment(
        os=os,
        container_engine=container_engine,
        compose_engine=compose_engine
    )