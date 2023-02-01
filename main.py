# Bibliotecas a serem usadas
import pyautogui
import time

# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')

def loop_de_aulas():
    for i in range(5):
        # 1ª aula
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 2ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 3ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 4ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 5ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 6ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        enter()
        alttab()

        # ----------------Próximo dia no FET--------------
        up()
        up()
        up()
        up()
        up()
        right()
# -------------Código começa------------------------

alttab()
time.sleep(0.5)
alttab2()
time.sleep(0.5)
alttab()
time.sleep(0.5)
down()
up()

#-----------------------6°ano A----------------------
# --------Inicia a transferência-----------

loop_de_aulas()


