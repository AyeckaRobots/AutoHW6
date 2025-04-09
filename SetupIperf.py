import pyautogui
import time

def press(key: str) -> None:
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)


def type_word(string: str) -> None:
    for char in string:
        press(char)
    print(f"wrote: {string}")
    time.sleep(0.1)

def enter_word(string: str) -> None:
    type_word(string)
    press('\n')
    time.sleep(0.1)



print("started")
time.sleep(5)
type_word("1111")
enter_word("1400")
type_word("f1")
type_word("e12")
enter_word("D0-D1-D2-D3-D4-D5")
type_word("5")
type_word("000000")
type_word("1211")
enter_word("1400")
type_word("f1")
type_word("e12")
enter_word("D0-D1-D2-D3-D4-D5")
type_word("5")
type_word("000000")
type_word("3d")
type_word("0")
