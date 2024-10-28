import time

class TimePassed:
    def __init__(self, func) -> None:
        self.func = func
        self.execution_time = None  

    def __call__(self, *args, **kwargs) -> float:
        start_time = time.time()
        result = self.func(*args, **kwargs)  
        self.execution_time = time.time() - start_time
        return result 

    def get_execution_time(self) -> float:
        return self.execution_time
