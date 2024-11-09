import subprocess

# List of configuration commands to run
commands = [
    "python main.py --config 1001 --generate_label --no_progress_bar",
    "python main.py --config 1002 --generate_label --no_progress_bar",
    "python main.py --config 1003 --generate_label --no_progress_bar",
    "python main.py --config 1004 --generate_label --no_progress_bar"
]

def run_command(command):
    try:
        print(f"Running command: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

if __name__ == "__main__":
    for cmd in commands:
        run_command(cmd)

    print("All commands executed.")
