# __init__.py - Initializes the self-healing module

# Import all self-healing components
from .retry_strategy import RetryStrategy
from .learning_agent import LearningAgent

# Initialize the components
retry_strategy = RetryStrategy()
learning_agent = LearningAgent()

# Function to start self-healing mechanisms
def initialize_self_healing():
    """
    Initializes the self-healing module by setting up retry mechanisms and the learning agent.
    
    Logic:
    1) Prepare retry strategies for task execution.
    2) Set up the learning agent to monitor task successes and failures.
    3) Link the self-healing mechanisms to core task execution.
    
    Interaction with the program:
    - This function will be called by the core system when task automation begins.
    - It ensures self-healing strategies are active for all tasks and links them to the retry logic.
    
    TODO:
    - Future task: Make the initialization dynamic based on the type of task being performed.
    """
    retry_strategy.initialize_retry_mechanism()
    learning_agent.start_monitoring()
