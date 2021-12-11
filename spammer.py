import time
import pyautogui


def spamm(script):
    for e in range(5, 1, -1):
        print(f"{e} seconds before nuke")
        time.sleep(1)
    f = open(script, "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


print("Start")

print("b:Entiere Beemovie Script (baddest movie ever made")
print("t:Entiere Titanic Script (long)")
print("3: Spamm one message many times")
print("4: Spamm your own script or text")
text = input("What should i Spamm? Type nummber from above:")

if text == "b":
    spamm("beemovie.txt")


elif text == "t":
    spamm("titanic.txt")

elif text == "3":
    message = input("type your message here and press enter: ")
    Quantity = int(input("How many times you want the message get spammed?"))
    for i in range(5, 1, -1):
        print(f"{i} seconds before nuke")
        time.sleep(1)
    print("Get ready")
    time.sleep(1)
    for i in range(0, Quantity):
        pyautogui.typewrite(message)
        pyautogui.press("enter")

elif text == "4":
    print("Paste your text/script in the empty spamm.txt file")
    input("Press enter when pasted and saved")
    spamm("spamm.txt")

print("done")
