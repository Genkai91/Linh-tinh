import time
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from os import system, get_terminal_size

# Khởi tạo colorama
init()

def color(text, color_name):
    if color_name.lower() == "green":
        return f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}{text}{Fore.WHITE}]{Fore.LIGHTGREEN_EX}"
    elif color_name.lower() == "red":
        return f"{Fore.WHITE}[{Fore.LIGHTRED_EX}{text}{Fore.WHITE}]{Fore.LIGHTRED_EX}"

def align(text):
    lines = text.splitlines()
    greatest_length = max(len(line) for line in lines)
    for line in lines:
        padding = (get_terminal_size().columns - greatest_length) // 2
        print(f"{' ' * padding}{line}")

class printing():
    @staticmethod
    def text():
        banner = f"""{Fore.LIGHTMAGENTA_EX}
▄▄▄▄▄▄▪  ▄ •▄ ▄▄▄▄▄      ▄ •▄     ▄▄▄▄·       ▄▄▄▄▄
  ██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪    ▐█ ▀█▪▪     •██  
  ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
  ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
  ▀▀▀ ▀▀▀·▀  ▀ ▀▀▀  ▀█▄▀▪·▀  ▀    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀  
By: @Setiawan007
"""
        align(banner)

    @staticmethod
    def options():
        align(f"""{Fore.WHITE}
╔═══════════════════════════════╗
║                               ║
║          {color("1", "green")} {Fore.LIGHTMAGENTA_EX}Start{Fore.WHITE}            ║
║          {color("2", "green")} {Fore.LIGHTMAGENTA_EX}Info{Fore.WHITE}             ║
║          {color("3", "green")} {Fore.LIGHTMAGENTA_EX}Options{Fore.WHITE}          ║
║          {color("4", "green")} {Fore.LIGHTMAGENTA_EX}Clear{Fore.WHITE}            ║
║          {color("5", "green")} {Fore.LIGHTMAGENTA_EX}Exit{Fore.WHITE}             ║
║                               ║
╚═══════════════════════════════╝
""")

    @staticmethod
    def refresh():
        system("clear")  # Xóa màn hình trên Linux
        printing.text()
        align(f"\n\n{color('>', 'green')} Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114 {color('<', 'green')}")
        printing.options()

def start(video, botChoice):
    option = webdriver.FirefoxOptions()

    try:
        # Sử dụng đường dẫn chính xác cho geckodriver
        service = Service(executable_path="/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(service=service, options=option)
    except Exception as DriverError:
        print(f"{color('>', 'red')} {Fore.LIGHTRED_EX}Error: {DriverError}")
        input(f"{color('>', 'red')} {Fore.LIGHTRED_EX}Press Enter to Exit")
        exit()

    driver.get("https://zefoy.com")

    if driver.title == "zefoy.com | 502: Bad gateway":
        print(f"{color('>', 'red')} Zefoy Is Down... Attempting To Fix.\n")
        while driver.title == "zefoy.com | 502: Bad gateway":
            time.sleep(20)
            driver.refresh()
            if driver.title != "zefoy.com | 502: Bad gateway":
                print(f"\n{color('>', 'green')} Fixed! Zefoy is Back Up. Starting Now.\n")
                break
    else:
        print(f"\n{color('>', 'green')} Zefoy Is Up!\n")
    
    captchaCheck = input(f"{color('>>>', 'green')} Type \"y\" Once You Finished The Captcha: {Fore.LIGHTMAGENTA_EX}")
    captchaFinish = False

    if captchaCheck == "y":
        while not captchaFinish:
            try:
                driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/h5")
                captchaFinish = True
            except:
                print(f"\n{color('>', 'red')} You Didn't Finish The Captcha.")
                input(f"{color('>>>', 'green')} Type \"y\" Once You Finished The Captcha: {Fore.LIGHTMAGENTA_EX}")

    # Defining bot options (follow, hearts, views, shares)
    # Tiếp tục thêm logic tương tự cho bot...
    # ...
    
printing.refresh()

while True:
    choice = input(f"{color('>>>', 'green')} Choice: {Fore.LIGHTMAGENTA_EX}")
    if choice == "1":
        video = input(f"{color('>>>', 'green')} TikTok Video URL: {Fore.LIGHTMAGENTA_EX}")
        printing.options()
        option = input(f"\n{color('>>>', 'green')} Which to Bot: {Fore.LIGHTMAGENTA_EX}")
        start(video, int(option))
        break
    elif choice == "2":
        printing.info()
    elif choice == "3":
        printing.options()
    elif choice == "4":
        printing.refresh()
    elif choice == "5":
        exit()
