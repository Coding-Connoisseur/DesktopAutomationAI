# /DesktopAutomationAI/src/modules/gui_automation/__init__.py

"""
Initialization file for the GUI automation module.
This module provides automation functionality for interacting with desktop applications through
GUI controls like mouse clicks and keyboard inputs.
"""

# Import necessary components from gui_control to be used in other parts of the application.
from .gui_control import mouse_click, keyboard_input

# Initialize the GUI automation module
def initialize_gui_automation():
    """
    Initializes the GUI automation module.
    This function prepares the module for interaction with the rest of the system.

    Logic:
    1. Load any necessary configurations for GUI automation.
    2. Ensure necessary permissions (like accessibility permissions on macOS) are granted.
    3. Make the `mouse_click` and `keyboard_input` functions available to other modules.

    Interactions with the system:
    - This function will be called by the main module during program initialization to ensure
      the GUI automation system is ready to execute tasks.

    TODO-Future:
    - Check system compatibility (e.g., Windows, macOS, Linux).
    - Add any setup for external dependencies or libraries if needed.
    """
    print("GUI automation module initialized.")
    # TODO: Add any setup logic here.
