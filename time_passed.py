import time

class TimePassed:
    def define_time_set(self,action)->str:
        start_time= time.time()
        action()
        elapsed_time = time.time() - start_time
        return f'{elapsed_time:.3f}'
    

