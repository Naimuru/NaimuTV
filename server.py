from flask import Flask, request
import os
import platform
import subprocess

app = Flask(__name__)

@app.route('/turn_off_monitor', methods=['GET'])
def turn_off_monitor():
    system = platform.system()
    if system == "Windows":
        subprocess.call("powershell.exe -command (Add-Type '[DllImport(\"user32.dll\")] public static extern int SendMessage(IntPtr hWnd, UInt32 Msg, UIntPtr wParam, IntPtr lParam);' -Name a -Pas)::SendMessage([IntPtr]::Zero, 0x0112, [UIntPtr]::op_Explicit(0xF170), [IntPtr]::op_Explicit(2))")
    elif system == "Linux":
        subprocess.call("xset dpms force off", shell=True)
    else:
        return "Unsupported operating system", 500
    return "Monitor turned off", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
