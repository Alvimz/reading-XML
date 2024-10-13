import logging
import threading
import time
# import concurrent.futures

class MyThreadRequest(threading.Thread):

    def _setup(self):
        log("_setup")
        self.__keep_running = True

    def run(self) -> None:
        
        x = 0
        while(self.__keep_running):
            log("run - Test %s" % x)
            x+=1
            time.sleep(2)

        return super().run()
        
    def stop(self):
         self.__keep_running = False



def log(message):
    logging.info("%s - %s" % (threading.current_thread().name, message))

if __name__ == "__main__": 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    myThreadPool = list()
    for x in range(10):
        newObj = MyThreadRequest()
        myThreadPool.append(newObj)

    log(myThreadPool)
    time.sleep(10)

    for task in myThreadPool:
        task._setup()
        task.start()

    time.sleep(10)
    for task in myThreadPool:
        task.stop()
        task.join()

    log(myThreadPool)
    myThreadPool.clear()
    log(myThreadPool)

    time.sleep(10)
    


    





    