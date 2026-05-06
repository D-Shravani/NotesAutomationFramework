import time


class Timer:

    def __init__(self):

        self.start_time = None

    def start(self):

        self.start_time = time.time()

    def stop(self):

        end_time = time.time()

        execution_time = (
            end_time - self.start_time
        )

        return round(
            execution_time,
            2
        )