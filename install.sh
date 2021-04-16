#!/bin/bash

echo "Time To Learn Installer"

# Unix & Linux
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
#python3 -m pip install -r requirements.txt
python3 -m pip install tk
python3 -m pip install PySimpleGUI
python3 -m pip install request
python3 -m pip install flask
python3 -m pip install gTTS
python3 -m pip install pyinstaller
python3 -m pip install flask


# Windows
python -m pip install --upgrade pip
python -m venv venv
source venv/Scripts/activate
#python -m pip install -r requirements.txt
python -m pip install tk
python -m pip install PySimpleGUI
python -m pip install request
python -m pip install flask
python -m pip install gTTS
python -m pip install pyinstaller
python -m pip install flask
