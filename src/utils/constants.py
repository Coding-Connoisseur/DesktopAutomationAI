# constants.py
"""
This file defines global constants used throughout the project. Constants are values that do not change during runtime
and provide a centralized place for configuration and shared settings.
"""

# Time-related constants
DEFAULT_TASK_TIMEOUT = 30  # Default timeout (in seconds) for task execution across the entire program.
RETRY_DELAY = 5            # Delay (in seconds) between retries for failed tasks.

# Path-related constants
LOGS_PATH = "./data/logs/"  # Directory path for storing log files.
MODELS_PATH = "./data/models/"  # Directory path for storing machine learning models.

# API-related constants
CHATGPT_API_ENDPOINT = "https://api.openai.com/v1/engines/chatgpt-4/completions"  # API endpoint for ChatGPT-4.
API_TIMEOUT = 15  # Timeout for API calls in seconds.

# Task statuses
STATUS_PENDING = "PENDING"
STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"
STATUS_RETRY = "RETRY"

# TODO: Future constants
# - Add more constants as the project grows, such as error codes, user preference settings, or configurable options.
# - Separate constants into multiple files if different modules need their own set of constants.
# - Make constants user-configurable by adding a settings file or a configuration manager.
