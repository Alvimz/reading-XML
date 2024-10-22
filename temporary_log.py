import os
from xlsx_manager import XlsxManager
class TemporaryLog:
    def __init__(self) -> None:
        self.create_file_temporary()
        self.number_of_request_to_save = 3
        self.report_numbers = list()
        
    def create_file_temporary(self):
        if not os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt','w') as f:
                f.close()
    @staticmethod
    def write_log(time:float):
        with open('log_temporary.txt','a') as f:
            f.write(f'{time}\n')

    @staticmethod
    def clear_temporary_log():
        if os.path.exists('log_temporary.txt'):
            with open('log_temporary.txt', 'w') as f:
                f.write('')
            
    def save_csv_log(self):
        if self.len_txt_log():
            xls_manager = XlsxManager()
            avg_numbers = self.avg_text()
        
            xls_manager.save_to_log(avg_numbers)
            self.clear_temporary_log()
        
            

    def get_numbers_report(self,number):
        self.report_numbers.append(number)
        return self.report_numbers   
                
    def average_report(self):
        sum_numbers = sum(self.report_numbers)
        avg = sum_numbers/len(self.report_numbers)
        self.write_log(avg) # guarda a média no txt!
    
    
    def len_txt_log(self)->bool:
        count = 0
        with open('log_temporary.txt', 'r') as f:
            for _ in f:  
                count += 1
            if count > self.number_of_request_to_save:
                return True  
    
    def avg_text(self):
        list_numbers = list()
        with open('log_temporary.txt', 'r') as f:
            for num in f:
                list_numbers.append(float(num))
            avg = sum(list_numbers)/len(list_numbers)
            return avg
                
   
                
                   
    
if __name__ == '__main__':                
    a = TemporaryLog()
   


        