import os

class TemporaryLog:
    def __init__(self) -> None:
        ...
        
    def create_file_temporary(self):
        if not os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt','w') as f:
                f.close()
            

a = TemporaryLog()
a.create_file_temporary()


        