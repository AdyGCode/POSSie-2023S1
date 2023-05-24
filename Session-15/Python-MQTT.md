# MQTT Demo with Python

## Making Windows Command Prompt the Default in PyCharm

- Open Terminal tab
- Locate the +v on the PyCharm Screen (Usually opens in the
  lower part of the editor)
- Click on the V and select the settings
- In the .... dropdown select `C:\Windows\system32\cmd.exe`


## Activating the Local `venv`
This presumes you have a Python `venv` folder. It may 
be called `venv-306`, or similar.

- Open a command prompt (Terminal in PyCharm)
- Change into the folder with this project 
    - (use `cd` for this)
- On Windows run the command: `.\venv\Scripts\activate` 
    - (replace venv with the correct Python venv folder name)

This will activate the Python virtual environment (venv) ready 
for use.

NB: On ordinary command prompts, you are unlikely to 
see a `(venv)` at the start of the command line.




## Mosquitto - the MQTT Broker for development & home use

Get Mosquitto from: https://mosquitto.org/

Download the relevant version of Mosquitto (Windows)
eg: mosquitto-2.0.15-install-windows-x64.exe

Open the installer

