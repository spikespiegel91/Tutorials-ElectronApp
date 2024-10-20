import subprocess
import atexit
import time
import click
import requests
import os
import time

backend_process = None
# Use the absolute path to the Python interpreter in the virtual environment
venv_python = os.path.join(".venv", "Scripts", "python.exe")
activate_venv = os.path.join(".venv", "Scripts", "activate.bat")
backend_URL = "http://localhost:5000"

BACKEND_dir = "src"
GUI_dir = "GUI/src"
CLI_dir = "src"
CLI_TASK_dir = "src/cli"
CLI_RUN_name = os.path.basename(__file__) # "run.py"  

def check_backend_ready(url, timeout=0):
    print("Checking if backend is running...")
    for n in range(timeout):
        try:
            print("Trying to connect to the backend...{}".format(n))
            response = requests.get(url)
            if response.status_code == 200:
                print("Backend is ready!")
                return True
        except requests.ConnectionError:
            time.sleep(1)
    print("Backend did not start within the timeout period.")
    return False

def start_backend():
    """Start the backend."""
    global backend_process
    #backend_process = subprocess.Popen([venv_python, "src/Main_tool.py"])
    print("Starting the backend...")
    subprocess.run(['start', 'cmd', '/k', venv_python, f"{BACKEND_dir}/Main_tool.py"],shell=True)
    #time.sleep(5)

def stop_backend():
    global backend_process
    if backend_process:
        print("Stopping the backend...")
        backend_process.terminate()
        backend_process.wait()
        print("Backend stopped.")

#atexit.register(stop_backend)

def backend():
    """Start the backend."""
    if not check_backend_ready(backend_URL):
        start_backend()
    else:
        print("Backend is already running.")

def gui():
    subprocess.run( ['start', 'cmd', '/k', 'npm run dev'], cwd=GUI_dir, shell=True, check=True) 
   # subprocess.run("npm run dev", cwd="GUI/src", shell=True, check=True) 

def run_cli_task(my_task_name):
    if not check_backend_ready(backend_URL):
        start_backend()
    #subprocess.run(["python", "src/cli/task1.py"])
    time.sleep(2)
    time_start = time.time()
    subprocess.run([venv_python, f"{CLI_TASK_dir}/{my_task_name}.py"])
    time_end = time.time()
    print(f"Task {my_task_name} finished! -- elapsed time: {time_end - time_start:.2f} seconds")
    print("")
    # show help after the task is done
    subprocess.run([venv_python, f"{CLI_dir}/{CLI_RUN_name}", "--help"])
    #subprocess.run(["cmd.exe", "/K", venv_python, f"{CLI_TASK_dir}/{my_task_name}.py"]) # Keep the terminal open
    
def install():
    """Install Python and Node.js dependencies."""
    print("Installing dependencies...")
    subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"])
    subprocess.run("npm install", cwd=GUI_dir, shell=True, check=True)

def run_all_components():
    """Run Electron + Svelte GUI"""
    print("Starting the Electron + Svelte GUI...")
    if not check_backend_ready(backend_URL):
        backend()  # Starts the backend
    gui()  # Starts the GUI

# //////////////// Menu ////////////////
def menu():
    """Show menu and prompt user."""
    while True:
        print("\n")
        print(" (.venv) > python src/run.py show-menu")
        print(" (.venv) > Opening menu...🚀✨")
        print("===================================")
        print("    Python + Electron/Svelte CLI Menu Tool")
        print("===================================")
        print("[1] Install Dependencies")
        print("[2] Run Python + Flask Backend")
        print("[3] Run Electron + Svelte GUI")
        print("[4] Run All")
        print("[5] Open CLI tasks menu")
        print("[0] Exit")
        print("===================================")
        
        choice = input("Choose an option (0-5): ")

        if choice == '1':
            install()
        elif choice == '2':
            backend()
        elif choice == '3':
            gui()
        elif choice == '4':
            run_all_components()
        elif choice == '5':
            print("CLI tasks menu")
            print("===================================")
            print("[1] Task 1")
            print("[2] Task 2")
            print("[0] Back to main menu")
            print("===================================")
            task_choice = input("Choose a task (0-3): ")
            if task_choice == '1':
                run_cli_task("task1")
            elif task_choice == '2':
                run_cli_task("task2")
            elif task_choice == '0':
                continue
            else:
                print("Invalid choice, try again.")

        elif choice == '0':
            #stop_backend()
            print("Exiting...")
            subprocess.run([activate_venv])

            break
        else:
            print("Invalid choice, try again.")


# //////////////// Click commands ////////////////
# Click commands, for people who want to run tasks via CLI instead of the menu
# example: python src/run.py cli-task task1

@click.group()
def cli():
    pass

@cli.command()
def show_menu():
    """Launch the interactive menu."""
    menu()

@cli.command(help="Run a CLI task. Available tasks: task1, task2")
@click.argument('task_name')
def cli_task(task_name):
    """Run a CLI task."""
    run_cli_task(task_name)

@cli.command()
def run_backend():
    """Run the backend."""
    backend()

@cli.command()
def run_gui():
    """Run the GUI."""
    gui()

@cli.command()
def run_all():
    """Run backend and GUI."""
    run_all_components()

@cli.command()
def stop_backend():
    """Stop the backend."""
    stop_backend()

if __name__ == "__main__":
    cli(prog_name=f"python {CLI_dir}/{CLI_RUN_name}")