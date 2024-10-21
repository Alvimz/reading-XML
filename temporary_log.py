import os
from xlsx_manager import XlsxManager
class TemporaryLog:
    def __init__(self) -> None:
        self.create_file_temporary()
        self.avg_qnt = 10
        self.raw_numbers = list()
        
    def create_file_temporary(self):
        if not os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt','w') as f:
                f.close()
    @staticmethod
    def write_log(time:float):
        with open('log_temporary.txt','a') as f:
            f.write(f'{time}\n')
            
    def average_numbers(self):
        avg = sum(self.raw_numbers)/self.avg_qnt
        return avg

    @staticmethod
    def clear_temporary_log():
        if os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt', 'w') as f:
                f.write('')
            
    def save_csv_log(self):
        xls_manager = XlsxManager()
        avg = self.average_numbers() #chama outra função para caclular
        xls_manager.save_to_log(avg)
        self.clear_temporary_log()
            
    def get_numbers(self):
        with open('log_temporary.txt','r') as f:
            for line in f:
                line_number = float(line.strip())
                self.raw_numbers.append(line_number)
        return self.raw_numbers
        
        
                
                
    
if __name__ == '__main__':                
    a = TemporaryLog()
    a.get_numbers()
    print(len(a.raw_numbers))


        