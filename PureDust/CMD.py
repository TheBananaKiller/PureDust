import os
import socket
import subprocess

SCRIPTS_FOLDER = "Scripts"
CHAT_FOLDER = "Source"
CHAT_CLIENT = "Client.py"
CHAT_SERVER = "Server.py"

print("LunarCMD written by Jordan Janke")
print("Read Txt file for tutorial.")

while True:
    command = input(">>> ")

    # Run scripts
    if command.startswith("LunarCMD.run "):

        filename = command.replace("LunarCMD.run ", "").strip()

        if not filename.endswith(".py"):
            filename += ".py"

        script_path = os.path.join(SCRIPTS_FOLDER, filename)

        if os.path.isfile(script_path):

            print(f"Running {filename}...")

            with open(script_path, "r", encoding="utf-8") as file:
                code = file.read()

            exec(code)

        else:
            print("Script not found.")

    # Connect command
    elif command.startswith("Connect "):

        ip = command.replace("Connect ", "").strip()

        if not ip:
            print("ERROR: No IP provided.")
            continue

        CHAT_PATH = os.path.join(CHAT_FOLDER, CHAT_CLIENT)

        if os.path.isfile(CHAT_PATH):

            print(f"Connecting to {ip}:55555...")

            # BLOCK LunarCMD until client closes
            subprocess.run(["python", CHAT_PATH, ip])

        else:
            print("Client.py not found.")
    else:
        print("ERROR 01: cmd not found")