import time
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting '{func.__name__}' at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        
        result = func(*args, **kwargs)  # Execute the decorated function
        
        end_time = time.time()
        print(f"Finished '{func.__name__}' at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result
    
    return wrapper

# Example of usage
@log_time
def my_function():
    time.sleep(2)  # Simulating a task that takes 2 seconds
    print("Function is running!")

my_function()
