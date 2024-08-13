import pyautogui as pag
import time

def main():
    time.sleep(5)
    for i in range(96, 270, 6):
        pag.moveTo(58, 558, duration=.2)
        pag.dragRel(100, 0, duration=.2)
        pag.doubleClick()
        pag.typewrite("250")
        pag.typewrite(["tab"])
        pag.typewrite(["tab"])
        pag.typewrite("250")
        pag.typewrite(["tab"])
        pag.typewrite(str(i))
        pag.typewrite(["tab"])
        pag.typewrite(["tab"])
        pag.typewrite(["tab"])
        pag.typewrite(["tab"])
        pag.typewrite(["enter"])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
