#!/usr/bin/env bash

rm /var/lib/dpkg/lock
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y wine32 python3-pip pyinstaller
wget https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
wine python-3.8.0.exe
sudo wine ~/.wine/drive_c/users/root/'Local Settings'/'Application Data'/Programs/Python/Python38-32/Scripts/pip3.exe install pyinstaller pynput
sudo pip3 install pynput
sudo pip3 install colorama
