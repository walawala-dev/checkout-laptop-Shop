import os
import subprocess


REPO_URL = "https://github.com/walawala-dev/checkout-laptop-Shop.git"


def run_git_command(command):
    print(f"Running: {' '.join(command)}")
    subprocess.run(command, check=True)


def main():
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Initial commit: Setup Flask laptop shop UI"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "add", "origin", REPO_URL],
        ["git", "push", "-u", "origin", "main"],
    ]

    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        for cmd in commands:
            run_git_command(cmd)
        print("All git commands executed successfully.")
    except subprocess.CalledProcessError as error:
        print(f"Error while executing git command: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
