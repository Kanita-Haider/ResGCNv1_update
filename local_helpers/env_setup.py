import os
import subprocess
import sys
import venv

# Configuration
venv_dir = "venv"
requirements_file = "scripts/requirements.txt"

# Define a helper function to run shell commands
def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell, check=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

# Step 1: Check if virtual environment exists, if not, create it
if not os.path.exists(venv_dir):
    print(f"Virtual environment not found. Creating new virtual environment at {venv_dir}...")
    venv.create(venv_dir, with_pip=True)

# Step 2: Activate the virtual environment
if os.name == "nt":  # Windows
    activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
else:  # Unix/MacOS
    activate_script = os.path.join(venv_dir, "bin", "activate")

print(f"Activating virtual environment...")
activate_command = f". {activate_script}" if os.name != "nt" else activate_script

# Ensure the script continues with the activated venv
if os.name != "nt":
    run_command(["/bin/bash", "-c", f"{activate_command} && python -m pip install --upgrade pip"])
else:
    subprocess.run(activate_command, shell=True, check=True)

# Step 3: Install PyTorch and tqdm
print("Installing PyTorch and tqdm...")
packages_to_install = [
    "torch",
    "torchvision",
    "torchaudio",
    "tqdm"
]
torch_install_command = [sys.executable, "-m", "pip", "install"] + packages_to_install
run_command(torch_install_command)

# Step 4: Install requirements from scripts/requirements.txt
if os.path.exists(requirements_file):
    print(f"Installing packages from {requirements_file}...")
    run_command([sys.executable, "-m", "pip", "install", "-r", requirements_file])
else:
    print(f"{requirements_file} not found. Skipping requirements installation.")

print("Setup complete.")
