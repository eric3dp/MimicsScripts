import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import pygetwindow as gw
import time
import threading

# Path to the script folder
SCRIPT_FOLDER = r"C:\Users\bradened\github\MimicsScripts\Mimics"
TARGET_WINDOW = "Materialise Mimics Core"

class ScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mimics Script Runner")
        self.root.geometry("300x400")
        self.root.attributes("-topmost", True)  # Always on top
        self.root.configure(bg="white")

        # Label
        self.label = tk.Label(root, text="Mimics Script Runner", font=("Arial", 12, "bold"), bg="white")
        self.label.pack(pady=10)

        # Frame to hold buttons
        self.button_frame = tk.Frame(root, bg="white")
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        # Load script buttons
        self.load_scripts()

        # Monitor thread for keeping on top of Mimics
        self.monitor_thread = threading.Thread(target=self.monitor_mimics, daemon=True)
        self.monitor_thread.start()

    def load_scripts(self):
        """Loads Python scripts from the specified folder and creates buttons, excluding 'hidden' scripts."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()  # Clear existing buttons

        if not os.path.exists(SCRIPT_FOLDER):
            messagebox.showerror("Error", f"Folder not found: {SCRIPT_FOLDER}")
            return

        scripts = [
            f for f in os.listdir(SCRIPT_FOLDER) 
            if f.endswith(".py") and not f.lower().startswith("hidden")
        ]

        if not scripts:
            tk.Label(self.button_frame, text="No scripts found", bg="white", fg="red").pack(pady=5)
            return

        for script in scripts:
            btn = tk.Button(
                self.button_frame,
                text=script,
                font=("Arial", 10),
                bg="#4CAF50", fg="white",
                command=lambda s=script: self.run_script(s)
            )
            btn.pack(fill=tk.X, padx=10, pady=5)

    def run_script(self, script_name):
        """Runs the selected script in a new process."""
        script_path = os.path.join(SCRIPT_FOLDER, script_name)
        try:
            subprocess.run(["python", script_path], check=True)
        except Exception as e:
            messagebox.showerror("Execution Error", f"Error running {script_name}\n{e}")

    def monitor_mimics(self):
        """Keeps the window on top when Mimics is focused."""
        while True:
            try:
                active_window = gw.getActiveWindow()
                if active_window and TARGET_WINDOW.lower() in active_window.title.lower():
                    self.root.attributes("-topmost", True)
                else:
                    self.root.attributes("-topmost", False)
            except Exception:
                pass
            time.sleep(1)  # Adjust as needed

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
