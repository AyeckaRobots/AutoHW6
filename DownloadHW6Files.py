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
"""
3 -> 8 -> 1 -> 192.168.200.11 -> 2 -> 255.255.255.0 -> 7 -> 192.168.200.14
00000

4 -> a -> 1 -> 192.168.200.14 -> 2 -> 31 -> 4 -> y (sleep 30)
4 -> a -> 3 -> 2 -> 1 sleep (10) -> 4 -> y (sleep 30)

4 -> b -> 1 -> 192.168.200.14 -> 2 -> 32 -> 4 -> y (sleep 30)
4 -> b -> 3 -> 2 -> 1 sleep (10) -> 4 -> y (sleep 30)

4 -> f -> 2 -> 0 -> 4 -> y
4 -> f -> 5 -> y

4 -> 3 -> y sleep (20)
4 -> 2 -> y sleep (10)
"""


#### Use this on a caompletitly new HW6 without any pre installed versions on it ####

time.sleep(5)

#set up network
type_word("3")
type_word("8")
type_word("1")
enter_word("192.168.200.11")
type_word("2")
enter_word("255.255.255.0")
type_word("7")
enter_word("192.168.200.14")
type_word("00")

#set up software
type_word("4a1")
enter_word("192.168.200.14")
type_word("2")
enter_word("31")
type_word("4")
type_word("y")
time.sleep(30)
type_word("0000")
type_word("4a")
# type_word("3")
# type_word("2")
# type_word("1")
# time.sleep(10)
type_word("4")
type_word("y")
time.sleep(30)
type_word("0000")

#set up firmware
type_word("4b2")
enter_word("32")
type_word("4")
type_word("y")
time.sleep(50)
type_word("0000")
type_word("4b")
# type_word("3")
# type_word("2")
# type_word("1")
# time.sleep(10)25
type_word("4")
type_word("y")
time.sleep(50)
type_word("0000")

#set up bootloader
type_word("4f")
type_word("2")
enter_word("0")
type_word("4")
type_word("y")
time.sleep(20)
type_word("0000")
type_word("4f5")
type_word("y")
time.sleep(10) # 15

# apply everything
type_word("43") 
type_word("y")
time.sleep(40)
type_word("42")
type_word("y")
print("done")