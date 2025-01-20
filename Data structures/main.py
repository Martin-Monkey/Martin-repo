from server import Server
from request import Client


server = Server()


client1 = Client("Alice")
client2 = Client("Bob")
client3 = Client("Charlie")


server.accept_request(client1.create_request(priority=3))
server.accept_request(client2.create_request(priority=1))
server.accept_request(client3.create_request(priority=2))


server.process_requests()


server.show_statistics()
