#!/usr/bin/env python3

from queue import Queue
from random import randint
from threading import Thread
from time import sleep

class Worker(Thread):
    def __init__(self, id_num, queue):
        Thread.__init__(self)
        self.id = id_num
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            seconds = self.queue.get()
            print("Worker {} busy for {} seconds".format(self.id, seconds))
            sleep(seconds)
            print("Worker {} completed {}-second job".format(self.id, seconds))
            self.queue.task_done()

def main():
    num_workers = 3
    num_tasks = 8
    queue = Queue()

    # Create threads (workers), associating each with the queu
    for i in range(num_workers):
        worker = Worker(i, queue)
        # Setting daemon to True will let the main thread exit
        # even though the workers are blocking.
        worker.daemon = True
        worker.start()

    # Load tasks into queue
    for _ in range(num_tasks):
        t = randint(0, 20)
        print('Queueing {}-second job'.format(t))
        queue.put(t)

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Done')

if __name__ == '__main__':
    main()
