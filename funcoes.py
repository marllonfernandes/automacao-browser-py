import pyautogui
import time
import datetime
import sys
import schedule
from win32api import GetSystemMetrics

def ValidaResolucaoMonitor():
    
    result = True
    if GetSystemMetrics(0) != 1366 and GetSystemMetrics(1) != 768 :
        print("Resolução do monitor diferente do programado para execução!")
        result = False

    return result

def ValidaDiasUteis():
    
    result = True
    dt = datetime.datetime.now()
    weekday_name = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]
    wkday = dt.weekday()

    if(weekday_name[wkday] in "SAB/DOM"):
        print("Final de semana, não será processado!")
        result = False

    return result

def ExecutarPontoEntrada():
    Executar()

def ExecutarPontoSaida():
    Executar()

def Executar():
    
    if not(ValidaResolucaoMonitor() and ValidaDiasUteis()):
        exit()

    
    url = ''
    login = ''
    pwd = ''

    print("Iniciando Automação App Meu Rh...")
    pyautogui.PAUSE = 0.5
    pyautogui.press('winleft')
    pyautogui.write('chrome')
    pyautogui.moveTo(227, 212)
    pyautogui.click(button='right')
    pyautogui.moveTo(179, 432)
    pyautogui.click(button='left')
    #pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(315, 393)
    pyautogui.click(button='left')
    pyautogui.write(login)
    pyautogui.press('tab')
    pyautogui.write(pwd)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write(url)
    # posiciona no item menu ponto
    pyautogui.moveTo(185, 323)
    pyautogui.mouseDown()
    pyautogui.click()
    # posiciona no item menu relogio
    pyautogui.moveTo(175, 468)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(3)
    # posiciona no poup permitir localizacao
    pyautogui.moveTo(310, 162)
    pyautogui.click()
    time.sleep(1)
    # posiciona no menu bater ponto
    pyautogui.moveTo(813, 400)
    pyautogui.mouseDown()
    time.sleep(1)
    # posiciona no menu bater ponto indo para o lado direito para realizar a batida
    pyautogui.moveTo(1060, 400, duration=0.5)
    time.sleep(3)
    pyautogui.mouseUp()
    
    dataformatada = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    time.sleep(5)
    pyautogui.screenshot(f'ponto_registrado_{dataformatada}.png')
    print("Finalizando Automação App Meu Rh...")
