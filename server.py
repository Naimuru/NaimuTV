from flask import Flask, request
import os
import platform
import subprocess

app = Flask(__name__)

@app.route('/turn_off_monitor', methods=['GET'])
def turn_off_monitor():
    system = platform.system()
    if system == "Windows":
        subprocess.call('powershell.exe -command "Add-Type -TypeDefinition \'public class User32 { [System.Runtime.InteropServices.DllImport(\\"user32.dll\\")] public static extern int SendMessage(int hWnd, uint Msg, int wParam, int lParam); }\' -PassThru; $WM_SYSCOMMAND = 0x0112; $SC_MONITORPOWER = 0xF170; $MonitorOff = 2; [User32]::SendMessage(-1, $WM_SYSCOMMAND, $SC_MONITORPOWER, $MonitorOff)"', shell=True)
    elif system == "Linux":
        subprocess.call("xset dpms force off", shell=True)
    else:
        return "Unsupported operating system", 500
    return "Monitor turned off", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
