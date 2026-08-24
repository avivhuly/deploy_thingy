import typer
from detection.detect import detect_environment, ensure_directory

app = typer.Typer()

@app.command()
def environment():
    env = detect_environment()
    ensure_directory(env)
    print(f"Operating System: {env.os}")
    print(f"Container Engine: {env.container_engine}")
    print(f"Compose Engine: {env.compose_engine}")

if __name__ == "__main__":
    app()