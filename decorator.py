import time

def measure_time(func):
    """
    A decorator function that measures and prints the execution time 
    of the decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result
        
    return wrapper

if __name__ == "__main__":
    # Example usage to demonstrate the decorator
    
    @measure_time
    def example_task(seconds):
        print(f"Running task for {seconds} seconds...")
        time.sleep(seconds)
        return "Task Completed!"

    print("Starting execution...")
    result = example_task(1.2)
    print(f"Result: {result}")
