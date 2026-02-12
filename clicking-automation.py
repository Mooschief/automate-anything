import time
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()


def exit_program():
    return False


def save_position():
    position = list(mouse.position)
    with open("Mouse_position.txt", "a") as file:
        file.write(f"{position}\n")


def load_positions():
    positions = []
    with open("Mouse_position.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            line = line.strip("[]")
            x_str, y_str = line.split(",")
            x = int(x_str.strip())
            y = int(y_str.strip())
            positions.append((x, y))
    return positions


def mario_check_in():
    print("Starting Mario check-in")
    positions = load_positions()

    for x, y in positions:
        mouse.position = (x, y)
        time.sleep(0.2)
        mouse.click(Button.left, 1)
        time.sleep(0.2)


key_actions = {
    keyboard.Key.esc: exit_program,
    keyboard.Key.f9: save_position,
    keyboard.Key.tab: mario_check_in
}


def on_press(key):
    action = key_actions.get(key)
    if action:
        result = action()
        if result is False:
            return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
