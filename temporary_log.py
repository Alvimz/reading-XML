import os

class TemporaryLog:
    def __init__(self) -> None:
        self.create_file_temporary
        
    def create_file_temporary(self):
        if not os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt','w') as f:
                f.close()
    
    def write_log(self,time:float):
        with open('log_temporary.txt','a') as f:
            f.write(f'{time}\n')
            
    def read_log(self):
        with open('log_temporary.txt','r') as f:
            for linha in f:
                ...

a = TemporaryLog()
a.create_file_temporary()


        