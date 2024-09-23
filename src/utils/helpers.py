# helpers.py
"""
This file contains helper functions that provide common utility operations across the project. These are often 
reusable snippets of code that perform basic tasks such as data formatting, time handling, and other miscellaneous 
operations. The goal is to keep the core logic clean and focused by offloading these auxiliary tasks.
"""

import time
import os
import json

def format_time(seconds):
    """
    Converts time in seconds into a more human-readable format (HH:MM:SS).
    
    Logic:
    1. This function should take in a time value in seconds and convert it to hours, minutes, and seconds.
    2. Return a string in the format "HH:MM:SS", even for durations longer than 24 hours.
    
    Interaction with the program:
    - This function can be used when logging task durations, measuring retry intervals, or displaying execution times 
      in the feedback generator.
    
    TODO: Handle edge cases such as negative time values or extremely large durations.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def create_directory_if_not_exists(path):
    """
    Checks if a directory exists, and if not, creates it.
    
    Logic:
    1. This function takes a file path as input.
    2. If the directory at the specified path does not exist, it creates it.
    3. Return True if the directory already existed or was successfully created, False if the creation failed.
    
    Interaction with the program:
    - This function is useful when initializing the environment (e.g., for log or model storage).
    - It ensures that necessary directories are available before the program tries to write logs or models.
    
    TODO: Add error handling for cases where the directory cannot be created (e.g., due to permission issues).
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        print(f"Error creating directory {path}: {e}")
        return False


def load_json_file(file_path):
    """
    Loads data from a JSON file.
    
    Logic:
    1. This function takes a file path to a JSON file.
    2. It attempts to open and read the file, then parses it into a Python dictionary.
    3. Returns the parsed data or an empty dictionary if the file does not exist or cannot be loaded.
    
    Interaction with the program:
    - This is used for loading models, task patterns, or user configurations stored in JSON files.
    - The self-learning module might use this to load saved task data for learning purposes.
    
    TODO: Implement validation checks to ensure the JSON structure is valid for the program's expected format.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return {}


def save_json_file(data, file_path):
    """
    Saves data to a JSON file.
    
    Logic:
    1. This function takes a Python dictionary (`data`) and a file path as input.
    2. It serializes the dictionary into JSON format and writes it to the specified file.
    3. If the file does not exist, it is created.
    
    Interaction with the program:
    - The AI's self-learning module can use this to save updated task patterns and results.
    - Useful for storing configuration settings, model data, or logs in a structured format.
    
    TODO: Add error handling to manage cases where the file cannot be written (e.g., permission issues or disk space).
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully saved data to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")


def retry_function(func, max_retries=3, delay=RETRY_DELAY):
    """
    Retries a function up to a specified number of times if it fails.
    
    Logic:
    1. Takes a function (`func`) and the number of retries (`max_retries`) as input.
    2. Calls the function, and if it raises an exception, retries after a delay (specified in seconds).
    3. Continues until the function succeeds or the maximum number of retries is reached.
    4. Returns the function's result if successful, or raises an exception after the final failure.
    
    Interaction with the program:
    - This is used to add robustness to critical operations that might fail due to transient issues (e.g., network timeouts, 
      unavailable resources).
    - Integrated with the `task_executor` module to ensure tasks are retried automatically.
    
    TODO: Customize the exception handling to provide more context-specific error messages.
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception(f"Function failed after {max_retries} retries.")


# TODO: Add more helper functions as the program scales.
# - Consider adding utility functions for data validation, file I/O operations, and API response formatting.
# - Add more detailed error reporting for complex operations.
