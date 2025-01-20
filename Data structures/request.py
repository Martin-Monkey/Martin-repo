import time
import queue

class Request:
    def __init__(self, user, priority):
        self.user = user
        self.priority = priority
        self.time = time.time()  # Čas odeslání požadavku

    def __lt__(self, other):
        return self.priority < other.priority  # Nižší číslo = vyšší priorita

    def __str__(self):
        return f"Request(user={self.user}, priority={self.priority}, time={self.time})"


class Client:
    def __init__(self, name):
        self.name = name

    def create_request(self, priority):
        return Request(self.name, priority)
