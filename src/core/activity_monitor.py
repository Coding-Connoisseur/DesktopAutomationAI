import psutil
import time
import logging
import os
from pynput import keyboard, mouse

# TODO: Implement process monitoring with resource tracking (CPU, Memory) for enhanced insights.
# TODO: Add real-time browser activity tracking using Selenium or browser APIs.
# TODO: Ensure that the monitoring logic does not block the main application (use threading or async).

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class ActivityMonitor:
    """
    Monitors the user's desktop activity, including application usage, keystrokes, and mouse actions.
    The goal is to provide insightful feedback on user productivity and automate repetitive tasks.
    """

    def __init__(self):
        """
        Initializes the activity monitor, setting up tracking for processes, keystrokes, and mouse events.
        """
        self.active_window_name = None  # Store the name of the active window
        self.last_app_check_time = 0     # Time of last application check to minimize overhead
        self.key_strokes = []           # Record of all captured keystrokes
        self.mouse_actions = []         # Record of all mouse actions

        # TODO: Allow user-defined intervals for how frequently activity is checked (configurable).
        self.check_interval = 5         # Check system every 5 seconds
        self.cpu_threshold = 80         # High CPU usage threshold for logging
        self.memory_threshold = 80      # High Memory usage threshold for logging

    def monitor_processes(self):
        """
        Monitor running processes and their resource usage.
        Logs any process that exceeds CPU or memory usage thresholds.
        """
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                if proc.info['cpu_percent'] > self.cpu_threshold or proc.info['memory_percent'] > self.memory_threshold:
                    logger.warning(f"High resource usage detected: {proc.info}")
                # TODO: Enhance the reporting to include historical trends of resource usage for each app.
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def on_key_press(self, key):
        """
        Callback function to handle key press events.
        Logs each keystroke and stores it in the key_strokes list.
        """
        try:
            logger.info(f"Key pressed: {key.char}")
            self.key_strokes.append(key.char)
        except AttributeError:
            logger.info(f"Special key pressed: {key}")
            self.key_strokes.append(str(key))

    def on_click(self, x, y, button, pressed):
        """
        Callback function to handle mouse clicks.
        Logs mouse click position and button pressed.
        """
        if pressed:
            logger.info(f"Mouse clicked at ({x}, {y}) with {button}")
            self.mouse_actions.append((x, y, str(button)))

    def monitor_keystrokes(self):
        """
        Set up a listener to monitor and log all keyboard activity.
        """
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

    def monitor_mouse(self):
        """
        Set up a listener to monitor and log all mouse activity.
        """
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def get_active_window(self):
        """
        Get the name of the currently active window on the user's desktop.
        Logs when a new window becomes active.
        """
        try:
            active_window = os.popen('xdotool getwindowfocus getwindowname').read().strip()
            if active_window and active_window != self.active_window_name:
                logger.info(f"Active window changed to: {active_window}")
                self.active_window_name = active_window
            return active_window
        except Exception as e:
            logger.error(f"Error retrieving active window: {e}")

    def start_monitoring(self):
        """
        Begin monitoring processes, keystrokes, and mouse activity in the background.
        This function will run indefinitely unless manually stopped.
        """
        while True:
            current_time = time.time()
            
            # Check the active window every check_interval
            if current_time - self.last_app_check_time >= self.check_interval:
                self.monitor_processes()
                self.get_active_window()
                self.last_app_check_time = current_time

            # TODO: Use threading to run keystroke and mouse monitoring in parallel.
            time.sleep(1)  # Sleep to prevent excessive CPU usage

if __name__ == "__main__":
    monitor = ActivityMonitor()
    # TODO: Start process monitoring in a separate thread
    monitor.start_monitoring()
    # TODO: Implement proper shutdown procedure (graceful termination)
