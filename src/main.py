"""Entry point for the app used in CI and Docker."""

def run() -> None:
    """Run the application."""
    print("Hello from CI/Docker")

if __name__ == "__main__":
    run()