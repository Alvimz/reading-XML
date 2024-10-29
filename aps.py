from apscheduler.schedulers.background import BackgroundScheduler

class Aps:
    
    def __init__(self) -> None:
        self.scheduler = BackgroundScheduler()
    
    def start(self,func,minutes=1):
        self.scheduler.add_job(func, trigger='interval', minutes=minutes, args=())
        self.scheduler.start()
        
    def stop(self):
        self.scheduler.shutdown()
        print('Parando o trabalho')
    