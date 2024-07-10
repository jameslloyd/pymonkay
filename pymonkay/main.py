import os
import subprocess
import argparse

def create_project(project_name):
    """Creates a Python project with venv, main.py, and requirements.txt."""
    # Check if the project directory already exists
    project_path = os.path.join(os.getcwd(), project_name)
    if os.path.exists(project_path):
        print(f"Project '{project_name}' already exists. Skipping creation.")
        return  # Exit the function without creating the project
    # Create project directory
    os.makedirs(project_name, exist_ok=True)  # Allow overwriting existing projects

    # Initialize virtual environment
    subprocess.run(["python", "-m", "venv", os.path.join(project_name, ".venv")])

    # Create main.py
    with open(os.path.join(project_name, "main.py"), "w") as f:
        f.write("# Your Python code goes here")

    # Create requirements.txt
    with open(os.path.join(project_name, "requirements.txt"), "w") as f:
        pass  # Empty file for now

    with open(os.path.join(project_name, ".gitignore"), "w") as f:
        f.write(".venv\n__pycache__\n*.pyc\n*.pyo\n*.pyd\n")
        
    with open(os.path.join(project_name, "Dockerfile"), "w") as f:
        f.write("FROM python:3.8\n\nWORKDIR /app\n\nCOPY . .\n\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"main.py\"]")

    with open(os.path.join(project_name, ".dockerignore"), "w") as f:
        f.write("""
# Ignore version control directories
.git
.svn
.hg

# Ignore Python build artifacts
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore virtual environments
venv/
.venv/
env/
.env/

# Ignore configuration files (adjust as needed)
.vscode/
.idea/
*.local

# Ignore other files (customize as needed)
*.log
.DS_Store
                """)
    
    
    print(f"Project '{project_name}' created successfully!")
def main():
    # Argument Parsing (for command-line use)
    parser = argparse.ArgumentParser(description="Automate Python project creation")
    parser.add_argument("project_name", help="Name of the project")
    args = parser.parse_args()

    create_project(args.project_name)    

if __name__ == "__main__":

    main()