import os
from xlsx_manager import XlsxManager
class TemporaryLog:
    def __init__(self) -> None:
        self.create_file_temporary
        self.logs = list()
        self.avg_qnt = 10
        
    def create_file_temporary(self):
        if not os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt','w') as f:
                f.close()
    
    def write_log(self,time:float):
        with open('log_temporary.txt','a') as f:
            f.write(f'{time}\n')
            
    def save_csv_log(self):
        xls_manager = XlsxManager()
        with open('log_temporary.txt','r') as f:
            for linha in f:
                self.logs.append(linha)
            if len(self.logs) == self.avg_qnt:
                avg = self.average_numbers(self.logs)
                xls_manager.save_to_log(avg)
                self.clear_temporary_log()
                
                
    def average_numbers(self,list_numbers):
        avg = sum(list_numbers)/self.avg_qnt
        return avg

    def clear_temporary_log(self):
        if os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt', 'w') as f:
                f.write('')
                
a = TemporaryLog()
a.create_file_temporary()


        