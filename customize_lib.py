import os
import sys


python_folder = sys.executable
python_path = os.path.dirname(python_folder)
print (python_path)
whats = os.path.join(python_path, 'Lib', 'site-packages', 'pywhatkit', 'whats.py')
print(whats)




if os.path.isfile(whats):
    with open(whats, 'r') as archivo:
        contenido = archivo.read()

    contenido_modificado = """import time
import webbrowser as web
from datetime import datetime
from urllib.parse import quote

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()


def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 7,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(2)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 2)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
    phone_no: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 7,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group_instantly(
    group_id: str,
    message: str,
    wait_time: int = 7,
    tab_close: bool = True,
    close_time: int = 3,
) -> None:

    current_time = time.localtime()

    time.sleep(wait_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)



def sendwhats_image(
    receiver: str,
    img_path: str,
    caption: str = "",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:

    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    current_time = time.localtime()
    core.send_image(
        path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
    )
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
    if tab_close:
        core.close_tab(wait_time=close_time)

def open_web() -> bool:

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True"""

    with open(whats, 'w') as archivo_modificado:
        archivo_modificado.write(contenido_modificado)


    print('Archivo 1 de 2 ...................... whats.py modificado correctamente.')
else:
    print('El archivo whats.py no existe  o no se ha enconrado.')



##########################################################



core = os.path.join(python_path, 'Lib', 'site-packages', 'pywhatkit', 'core', 'core.py')
print(core)


if os.path.isfile(core):
    with open(core, 'r') as archivo2:
        contenido2 = archivo2.read()

    contenido_modificado2 = """import time
from platform import system
from urllib.parse import quote
from webbrowser import open

import requests
from pyautogui import click, hotkey, press, size, typewrite

from pywhatkit.core.exceptions import InternetException

WIDTH, HEIGHT = size()


def check_number(number: str) -> bool:

    return "+" in number or "_" in number


def close_tab(wait_time: int = 2) -> None:

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")


def check_connection() -> None:

    try:
        requests.get("https://google.com")
    except requests.RequestException:
        raise InternetException(
            "Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )


def _web(receiver: str, message: str) -> None:
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)


def send_message(message: str, receiver: str, wait_time: int) -> None:

    _web(receiver=receiver, message=message)
    time.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    time.sleep(wait_time - 7)
    if not check_number(number=receiver):
        for char in message:
            if char == "\\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    press("enter")"""

    with open(core, 'w') as archivo_modificado2:
        archivo_modificado2.write(contenido_modificado2)


    print('Archivo 2 de 2 ...................... core.py modificado correctamente.')
else:
    print('El archivo core.py no existe o no se ha enconrado.')

