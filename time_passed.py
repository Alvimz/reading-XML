import time

class TimePassed:
    def define_time_set(self,action)->float:
        start_time= time.time()
        action()
        elapsed_time = time.time() - start_time
        return elapsed_time
    

