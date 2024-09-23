# /DesktopAutomationAI/src/modules/gui_automation/gui_control.py

"""
This file contains methods for controlling the GUI (Graphical User Interface) of the desktop.
It provides functions to simulate mouse clicks, keyboard inputs, and other interactions with
the desktop environment.
"""

import pyautogui  # A library for GUI automation.

def mouse_click(x, y, button="left"):
    """
    Simulates a mouse click at the specified coordinates (x, y).

    Parameters:
    - x (int): The x-coordinate of where the click should happen.
    - y (int): The y-coordinate of where the click should happen.
    - button (str): The mouse button to click, "left" or "right".

    Logic:
    1. Validate the input coordinates (x, y) to ensure they are within the screen bounds.
    2. Simulate a mouse click at the given coordinates using `pyautogui.click()`.
    3. Log the action for debugging and tracking purposes.

    Interactions with the system:
    - This function will be triggered when the AI needs to perform a GUI-based task that involves
      mouse interaction (e.g., clicking a button in a desktop app).
    - It is called from the task executor or task scheduler module, depending on task requirements.

    TODO-Future:
    - Add functionality to handle different types of clicks (e.g., double click).
    - Implement error recovery in case of invalid screen coordinates or permission issues.
    """
    try:
        print(f"Clicking at ({x}, {y}) with {button} button.")
        pyautogui.click(x=x, y=y, button=button)
    except Exception as e:
        print(f"Error during mouse click: {e}")
        # TODO: Implement error handling and retry logic.
        pass


def keyboard_input(text):
    """
    Simulates keyboard input by typing out the provided text.

    Parameters:
    - text (str): The string of text to type.

    Logic:
    1. Validate the input text to ensure it's a non-empty string.
    2. Use `pyautogui.typewrite()` to simulate typing the text.
    3. Log the action for debugging and tracking purposes.

    Interactions with the system:
    - This function will be triggered when the AI needs to perform a keyboard-related task, such as
      filling out a form or entering text in a desktop application.
    - It is likely to be used in combination with mouse clicks to fully automate GUI tasks.

    TODO-Future:
    - Add support for special keys (e.g., Enter, Shift, Ctrl) using `pyautogui.hotkey()`.
    - Handle different typing speeds or provide options for variable typing speed.
    """
    try:
        print(f"Typing text: {text}")
        pyautogui.typewrite(text)
    except Exception as e:
        print(f"Error during keyboard input: {e}")
        # TODO: Implement error handling and retry logic.
        pass


def move_mouse(x, y):
    """
    Moves the mouse cursor to the specified coordinates (x, y) on the screen.

    Parameters:
    - x (int): The x-coordinate to move the cursor to.
    - y (int): The y-coordinate to move the cursor to.

    Logic:
    1. Validate the input coordinates to ensure they are within the screen's dimensions.
    2. Move the mouse cursor to the specified (x, y) location using `pyautogui.moveTo()`.
    3. Optionally, add a delay for more natural mouse movement.

    Interactions with the system:
    - This function can be used to position the mouse before performing a click or drag operation.
    - It interacts with the task scheduler and error recovery modules to ensure the mouse is moved
      to the correct position before other tasks are executed.

    TODO-Future:
    - Implement smooth mouse movement with customizable speed.
    - Add logging for mouse movements to track the task flow.
    """
    try:
        print(f"Moving mouse to ({x}, {y}).")
        pyautogui.moveTo(x=x, y=y)
    except Exception as e:
        print(f"Error during mouse move: {e}")
        # TODO: Implement error handling and retry logic.
        pass


def scroll_mouse(amount):
    """
    Scrolls the mouse wheel by the specified amount.

    Parameters:
    - amount (int): The amount to scroll. Positive values scroll up, negative values scroll down.

    Logic:
    1. Validate the scroll amount to ensure it is a reasonable value.
    2. Use `pyautogui.scroll()` to simulate mouse scrolling.
    3. Log the action for debugging and tracking purposes.

    Interactions with the system:
    - This function will be used to scroll through pages or lists in desktop applications or web
      browsers as part of automated tasks.

    TODO-Future:
    - Add support for horizontal scrolling if required.
    - Handle cases where scrolling might not be possible (e.g., end of page).
    """
    try:
        print(f"Scrolling mouse by {amount}.")
        pyautogui.scroll(amount)
    except Exception as e:
        print(f"Error during mouse scroll: {e}")
        # TODO: Implement error handling and retry logic.
        pass
