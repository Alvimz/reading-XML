import time

class TimePassed:
    def __init__(self, func) -> None:
        self.func = func
        self._execution_time = None  

    def __call__(self, *args, **kwargs) -> float:
        start_time = time.time()
        result = self.func(*args, **kwargs)  
        self._execution_time = time.time() - start_time
        return result 

    @property
    def execution_time(self) -> float:
        return self._execution_time
