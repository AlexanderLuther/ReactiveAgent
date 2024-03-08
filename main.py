import threading
import keyboard
from time import sleep


def main():
    thread_menu = threading.Thread(
        target=menu(),
        name='ThreadMenu'
    )
    thread_menu.start()


def menu():
    print("Presione M para insertar moneda")
    print("Presione 1 para servir refresco C1")
    print("Presione 2 para servir refresco C2")
    print("Presione 3 para servir refresco C3")
    perception: int = 0
    state: int = 0
    while True:
        if keyboard.read_key() == "m":
            print("\nInsertando moneda")
            perception = 1
            sleep(0.1)
        elif keyboard.read_key() == "1":
            print("\nSolicitando refresco C1")
            perception = 2
            sleep(0.1)
        elif keyboard.read_key() == "2":
            print("\nSolicitando refresco C2")
            perception = 3
            sleep(0.1)
        elif keyboard.read_key() == "3":
            print("\nSolicitando refresco C3")
            perception = 4
            sleep(0.1)

        state = setAction(state, perception)


def setAction(state, perception):
    if state == 0:
        if perception == 1:
            print("Moneda insertada\n")
            print("Seleccione su refresco")
            return 1
        else:
            print("Insertar Moneda")
            return 0

    if state == 1:
        if perception == 2:
            print("Sirviendo refreso C1")
            return 0
        elif perception == 3:
            print("Sirviendo refreso C2")
            return 0
        elif perception == 4:
            print("Sirviendo refreso C3")
            return 0
        else:
            print("Seleccionar refreso")
            return state


if __name__ == '__main__':
    main()
