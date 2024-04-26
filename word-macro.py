from pynput import keyboard
import time
import json
from pynput.keyboard import Key, Controller, KeyCode

def main():
    # Load the macros from the JSON file
    with open('macros.json', 'r') as file:
        data = json.load(file)

    # Extract macros from the loaded data
    macros = data["macros"]

    # Creates a controller
    board = Controller()

    # Create a dictionary to store macros
    macro_functions = {}

    # Iterates over every macro
    for macro in macros:
        # Macro details
        name = macro["name"]
        keycodes = macro["keycodes"]
        delay = macro["delay"]

    # Defines the macro function
        macro_function = lambda keycodes=keycodes, delay=delay: [
            # Press the key according to the keycode
            (board.press(Key.enter) if keycode == Key.enter else
            board.press(Key.space) if keycode == Key.space else
            # If keycode is a single character then press that key
            board.press(keycode) if len(keycode) == 1 else
            # Else if the key is in the form <...> then press that key
            board.press(KeyCode.from_vk(int(keycode[1:-1]))),
            # Delay
            time.sleep(delay),
            # Release the key according to the key code
            board.release(Key.enter) if keycode == Key.enter else
            board.release(Key.space) if keycode == Key.space else
            # If keycode is a single character then release that key
            board.release(keycode) if len(keycode) == 1 else
            # Else if the key is in the form <...> then release that key
            board.release(KeyCode.from_vk(int(keycode[1:-1]))))
            # Iterate over every keycode in the macro
            for keycode in keycodes
        ]

        # Add the macro function to the dictionary with the macro name as the key
        macro_functions[name] = macro_function



