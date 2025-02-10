import ctypes
import time
from threading import Thread
import psutil
import os

# Constants for quick switch
QUICK_SWITCH_INTERVAL = 5  # seconds
FOREGROUND_TASKS = ['notepad.exe', 'chrome.exe']  # Example foreground tasks
BACKGROUND_TASKS = ['spotify.exe', 'dropbox.exe']  # Example background tasks

def is_foreground_window(process_name):
    """Check if the given process is the foreground window."""
    user32 = ctypes.windll.user32
    foreground_window = user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    user32.GetWindowThreadProcessId(foreground_window, ctypes.byref(pid))
    foreground_process_name = psutil.Process(pid.value).name()
    return process_name.lower() == foreground_process_name.lower()

def switch_to_foreground(task_name):
    """Bring the task to the foreground."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == task_name.lower():
            try:
                os.system(f'taskkill /F /PID {proc.info["pid"]}')  # Close if running
            except Exception as e:
                print(f"Error terminating {task_name}: {e}")
    os.startfile(task_name)  # Start the process

def automate_switching():
    """Automate the switching between foreground and background tasks."""
    while True:
        for task in FOREGROUND_TASKS:
            if not is_foreground_window(task):
                print(f"Switching to foreground task: {task}")
                switch_to_foreground(task)
                time.sleep(QUICK_SWITCH_INTERVAL)
        
        for task in BACKGROUND_TASKS:
            if is_foreground_window(task):
                print(f"Switching to background task: {task}")
                switch_to_foreground(task)
                time.sleep(QUICK_SWITCH_INTERVAL)

if __name__ == "__main__":
    switcher_thread = Thread(target=automate_switching)
    switcher_thread.start()
    switcher_thread.join()