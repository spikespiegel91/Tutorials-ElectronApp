import os
import winshell
from win32com.client import Dispatch
from tkinter import Tk
from tkinter.filedialog import askdirectory

def create_shortcut(shortcut_dir, shortcut_name, script_arguments, icon_file, target_script=None,  keep_terminal_open = False):
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Move up one directory from /scripts to the project root
    
    base_dir = os.path.abspath(os.path.join(script_dir, ".."))

    python_exe = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
    icon_path = os.path.join(base_dir, "icons", icon_file)

    shortcut_path = os.path.join(shortcut_dir, f"{shortcut_name}.lnk")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.WorkingDirectory = base_dir
    shortcut.IconLocation = icon_path

   
    if target_script:
        script_path = os.path.join(base_dir, "src", target_script)
        shortcut.TargetPath = python_exe
        shortcut.Arguments = f"{script_path} {script_arguments}"
        #shortcut.Arguments = f'cmd /k "{python_exe} {script_path} {script_arguments}"'
        if keep_terminal_open:
            shortcut.TargetPath = "cmd.exe"
            shortcut.Arguments = f'/k "{python_exe} {script_path} {script_arguments}"'
        else:
            shortcut.TargetPath = python_exe
            shortcut.Arguments = f'{script_path} {script_arguments}'

    else:
        shortcut.TargetPath = python_exe

    shortcut.save()
    print(f"Shortcut created at: {shortcut_path}")


def create_shortcut2(shortcut_dir, shortcut_name, script_arguments, icon_file, target_scripts=None, keep_terminal_open=False):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, ".."))

    python_exe = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
    icon_path = os.path.join(base_dir, "icons", icon_file)
    shortcut_path = os.path.join(shortcut_dir, f"{shortcut_name}.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.WorkingDirectory = base_dir
    shortcut.IconLocation = icon_path

    if target_scripts:
        commands = []
        for script, args in target_scripts:
            script_path = os.path.join(base_dir, "src", script)
            commands.append(f"{python_exe} {script_path} {args}")

        full_command = " && ".join(commands)
        
        if keep_terminal_open:
            shortcut.TargetPath = "cmd.exe"
            shortcut.Arguments = f'/k "{full_command}"'
        else:
            shortcut.TargetPath = "cmd.exe"
            shortcut.Arguments = f'/c "{full_command}"'
    else:
        shortcut.TargetPath = python_exe

    shortcut.save()
    print(f"Shortcut created at: {shortcut_path}")

    

def main():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    # Use Tkinter to open a directory selection dialog
    shortcut_dir = askdirectory(title="Select Folder to Save Shortcuts")
    
    # If the user cancels, provide a default option or exit
    if not shortcut_dir:
        print("No directory selected. Exiting...")
        return

    # Create shortcuts
    # (shortcut_dir, "SpikeTool_Run_All", "", "on.ico", "Main_tool.py")
    # create_shortcut(shortcut_dir, "SpikeTool_Kill", "", "off.ico", "run.py stop-backend")
    create_shortcut(shortcut_dir, "Run_CLI", "", "icono_2.ico", "run.py show-menu")

    # Create a shortcut that runs multiple scripts
    create_shortcut2(
        shortcut_dir = shortcut_dir,
        shortcut_name = "Run_GUI",
        script_arguments = "",
        icon_file = "icono_1.ico",
        target_scripts = [("run.py", "run-backend"), ("run.py", "run-gui")],
        keep_terminal_open = False
    )

if __name__ == "__main__":
    main()
