# config.py
import json

CONFIG_FILE = 'config.json'

def load_config(config_file=CONFIG_FILE):
    """
    Loads the configuration settings from a file.
    
    1. Reads the configuration file, which contains settings like API keys and user preferences.
    2. Parse the settings into a dictionary and return it.
    
    How it interacts with the program:
    - The configuration settings (API keys for ChatGPT-4, user preferences, task thresholds) 
      are loaded and used across all modules.
    - For example, api_communicator.py will use the API key loaded here to communicate with OpenAI's API.

    TODO-future:
    - Add support for environment variables to override config settings for secure deployments.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        # Handle missing config file scenario
        print("Configuration file not found. Loading default settings.")
        return default_config()

def save_config(config, config_file=CONFIG_FILE):
    """
    Saves the current configuration to a file.
    
    1. Writes the configuration settings to a JSON file.
    2. Ensures any changes to the configuration during runtime (e.g., changing user preferences)
       are saved persistently.

    How it interacts with the program:
    - This function allows the AI to save settings persistently, so any changes the user 
      makes (such as new API keys or automation preferences) can be saved.

    TODO-future:
    - Extend support to securely encrypt sensitive information like API keys before saving.
    """
    try:
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")

def default_config():
    """
    Provides default configuration settings.
    
    1. Return a dictionary with default values for API keys, task preferences, and other settings.
    
    How it interacts with the program:
    - If no configuration file exists or there is an error in loading it, this function ensures 
      the program runs with default settings (e.g., default retry counts, log levels).

    TODO-future:
    - Add a mechanism to update default settings based on the environment (e.g., development vs production).
    """
    return {
        "openai_api_key": "your-default-api-key",
        "task_retry_limit": 3,
        "log_level": "DEBUG",
        "preferred_browser": "chrome"
    }

def update_config_key(key, value, config_file=CONFIG_FILE):
    """
    Updates a specific key in the configuration.
    
    1. Load the current configuration.
    2. Update the value for the specified key.
    3. Save the updated configuration back to the file.
    
    How it interacts with the program:
    - This function will be called when the user changes any settings, 
      such as updating an API key or adjusting task preferences.
    
    TODO-future:
    - Implement validation to ensure the key and value being updated are valid.
    """
    config = load_config(config_file)
    config[key] = value
    save_config(config, config_file)
