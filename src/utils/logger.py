# logger.py
import logging
from datetime import datetime

# Initialize the logger
def setup_logger(log_file='task_log.txt'):
    """
    Sets up the logger for the program.
    
    1. Create a logger instance that writes to a file.
    2. Log different levels of messages (INFO, ERROR, DEBUG).
    3. All tasks and errors will be logged using this logger.

    How it interacts with the program:
    - The logger will be called by various modules like task_executor, error_handler, 
      and self_learning to log task executions, errors, and performance.
    
    TODO-future:
    - Extend to handle logging to a remote server or cloud storage for real-time monitoring.
    """
    logger = logging.getLogger('desktop_automation_ai')
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # Create console handler with a higher log level (error only)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

# Log task executions
def log_task_execution(logger, task_name, status):
    """
    Logs the execution of tasks performed by the AI.
    
    1. Log the start and end of each task execution.
    2. Include the task name and status (success/failure).

    How it interacts with the program:
    - This function will be called every time a task is executed or completed, 
      providing a history of actions performed by the AI.

    TODO-future:
    - Enhance to log additional metadata, such as the time taken for each task, 
      task complexity, or system resource usage.
    """
    logger.info(f"Task executed: {task_name}, Status: {status}")

# Log errors
def log_error(logger, error_message):
    """
    Logs any errors encountered by the AI.
    
    1. Record the error message and any related stack trace.
    2. Categorize errors to facilitate the self-healing mechanism.

    How it interacts with the program:
    - Called by the error_handler module when any error is detected.
    - Helps in diagnosing problems and creating a history of common failures for learning.
    
    TODO-future:
    - Add error categorization (e.g., GUI errors, network errors) to improve error handling.
    - Consider integrating with a real-time alerting system.
    """
    logger.error(f"Error encountered: {error_message}")

# Log debug information
def log_debug(logger, message):
    """
    Logs debug-level information for deeper inspection.
    
    1. Log details that help trace the flow of the program.
    2. Provide insights into variable states, task sequences, etc.
    
    How it interacts with the program:
    - This is useful during development and debugging to track internal states 
      without polluting higher-level logs with unnecessary information.

    TODO-future:
    - Create a toggle for logging debug messages based on user preference or execution mode.
    """
    logger.debug(f"Debug: {message}")
