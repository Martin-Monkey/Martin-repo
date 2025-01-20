import queue
import time
from request import Request


class Server:
    def __init__(self):
        self.request_queue = queue.PriorityQueue()
        self.stats = []

    def accept_request(self, request):
        self.request_queue.put(request)
        self.stats.append((request.user, time.ctime(request.time)))

    def process_requests(self):
        while not self.request_queue.empty():
            request = self.request_queue.get()
            print(f"Processing: {request}")

    def show_statistics(self):
        print("\nRequest Statistics:")
        for user, timestamp in self.stats:
            print(f"User: {user}, Time: {timestamp}")
