import time
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from os import system, get_terminal_size

init()

# Không cần dùng system("mode 800") trong môi trường Linux
system("title TikTok Bot -By Setiawan007")

def color(str, color):
    if color.lower() == "green":
        result = f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}{str}{Fore.WHITE}]{Fore.LIGHTGREEN_EX}"

    elif color.lower() == "red":
        result = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}{str}{Fore.WHITE}]{Fore.LIGHTRED_EX}"

    return result

def align(str):
    lines = str.splitlines()
    greatest = []
    for i in lines:  
        greatest.append(len(i))

    for i in lines:
        length = round(int(greatest[-1])/2)
        print(f"{' '*round(get_terminal_size().columns/2-length)}{i}")

class printing():

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def text():
        text = f"""{Fore.LIGHTMAGENTA_EX}
\t\t\t\t\t▄▄▄▄▄▄▪  ▄ •▄ ▄▄▄▄▄      ▄ •▄     ▄▄▄▄·       ▄▄▄▄▄
\t\t\t\t\t  ██  ██ █▌▄▌▪•██  ▪     █▌▄▌▪    ▐█ ▀█▪▪     •██  
\t\t\t\t\t  ▐█.▪▐█·▐▀▀▄· ▐█.▪ ▄█▀▄ ▐▀▀▄·    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
\t\t\t\t\t  ▐█▌·▐█▌▐█.█▌ ▐█▌·▐█▌.▐▌▐█.█▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
\t\t\t\t\t  ▀▀▀ ▀▀▀·▀  ▀ ▀▀▀  ▀█▄▀▪·▀  ▀    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀  By: @Setiawan007
"""
        text = text.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('•', f'{Fore.GREEN}•{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('·', f'{Fore.GREEN}·{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('.', f'{Fore.GREEN}.{Fore.LIGHTMAGENTA_EX}')
        align(text)

    def info():
        align(f"""{Fore.WHITE}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║          {color(">", "green")} About: {Fore.LIGHTMAGENTA_EX}This Tool Uses Zefoy To Bot TikTok Stats.{Fore.WHITE}                     ║
║          {color(">", "green")} Updates: {Fore.LIGHTMAGENTA_EX}Error Fix & Adjustment --9/15/2022{Fore.WHITE}                          ║
║          {color(">", "green")} Made By: {Fore.LIGHTMAGENTA_EX}Setiawan007{Fore.WHITE}                                                ║
║          {color(">", "green")} Github: {Fore.LIGHTMAGENTA_EX}https://github.com/Setiawan007{Fore.WHITE}                             ║
║          {color(">", "green")} Download Chrome Driver: {Fore.LIGHTMAGENTA_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}  ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")

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

    def refresh():
        system("clear")  # Dùng "clear" thay cho "cls" để xóa màn hình trên Linux
        printing.text()
        align(f"\n\n\t\t\t{color('>', 'green')} Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114 {color('<', 'green')}")
        align(f"\t\t\t\t{color('>', 'green')} {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/Setiawan007/TikTokBot {color('<', 'green')}")
        printing.options()

def start(video, botChoice):

    option = webdriver.FirefoxOptions()  # Sử dụng FirefoxOptions thay cho ChromeOptions

    try:
        service = Service(executable_path="/usr/bin/geckodriver")  # Chỉ định đường dẫn đúng của geckodriver
        driver = webdriver.Firefox(service=service, options=option)  # Khởi tạo trình duyệt Firefox
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
                print(f"\n{color('>', 'red')} Fixed! Zefoy is Back Up. Starting Now.\n")
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

# Đoạn mã tiếp theo giữ nguyên
# ...
