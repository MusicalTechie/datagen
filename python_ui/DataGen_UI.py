import PySimpleGUI as sg
import subprocess
import os
import sys

# Define full paths
base_path = r"C:\Users\AllanBarnard\OneDrive - Accelalpha Software Pvt. Ltd\Documents\0_AAdocs\7_Project_-_DataGen"
config_path = os.path.join(base_path, "data_config", "config_main.ini")
main_script_path = os.path.join(base_path, "python_datagen", "DataGen_1010_Main_DataGen_Initial.py")

# Set window theme and layout
sg.theme("SystemDefault")

layout = [
    [sg.Text("DataGen", font=("Helvetica", 20), justification="center", expand_x=True)],
    [sg.Button("Edit CONFIG", size=(30, 2), key="EDIT")],
    [sg.Button("Run MAIN", size=(30, 2), key="RUN")],
    [sg.Button("EXIT", size=(30, 1), key="EXIT")]
]

window = sg.Window("DataGen", layout, element_justification="center", finalize=True)

# Event loop
while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED or event == "EXIT":
        break
    elif event == "EDIT":
        os.startfile(config_path)  # Opens in default editor (e.g., Notepad)
    elif event == "RUN":
        try:
            subprocess.run([sys.executable, main_script_path], check=True)
            sg.popup("Script executed successfully.", title="Success")
        except subprocess.CalledProcessError as e:
            sg.popup_error(f"Error occurred while running script:\n{e}", title="Execution Error")

window.close()
