from flask import Flask, request
import os
import platform
import subprocess

app = Flask(__name__)

@app.route('/turn_off_monitor', methods=['GET'])
def turn_off_monitor():
    system = platform.system()
    if system == "Windows":
        subprocess.call("powershell.exe -command (Add-Type '[DllImport(\"user32.dll\")] public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)")
    elif system == "Linux":
        subprocess.call("xset dpms force off", shell=True)
    else:
        return "Unsupported operating system", 500
    return "Monitor turned off", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
