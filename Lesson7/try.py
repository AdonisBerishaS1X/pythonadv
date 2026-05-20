from typing import final

try:
    division = 10/0
except ZeroDivisionError:
    print("You cannot Divise by Zero")

fruit = {
    "Orange":5,
    "Banana":7,
    "Boranana":3
}

try:
    print(fruit["Doorhinge"])
except KeyError:
    print("Shut the hell up Slim Shady")


text="This is not a number"

try:
    text_to_int =  int(text)
except Exception as e:
    print("An Unkown Error Has Occurred", e)
finally:
    print("Yo dude you made it to 27! good job")