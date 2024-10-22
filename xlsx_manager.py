import openpyxl
from datetime import datetime
from time import sleep

class XlsxManager:
    
    def save_to_log(self, avg_time: float):
        # Carrega a planilha existente
        workbook = openpyxl.load_workbook('log.xlsx')
        sheet = workbook.active
        next_row = 2
        while sheet[f'A{next_row}'].value is not None:
            next_row += 1

        sheet[f'A{next_row}'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        sheet[f'B{next_row}'] = avg_time
        workbook.save('log.xlsx')
        workbook.close()
        
        print('Salvo no log!')

if __name__ == '__main__':
    xls = XlsxManager()
    xls.save_to_log(0.3)
    sleep(3)
    xls.save_to_log(0.9)
