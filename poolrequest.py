from concurrent.futures import ThreadPoolExecutor, as_completed

class MaybeThreads:
    def __init__(self):
        self.exec = ThreadPoolExecutor(max_workers=5)
        self._threads = list()

    def run(self, func, *args):
        future = self.exec.submit(func, *args)
        self._threads.append(future)

    def wait_4_complete(self):
        for future in as_completed(self._threads):
            future.result()

    def shutdown(self):
        self.exec.shutdown(wait=True)