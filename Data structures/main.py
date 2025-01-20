from server import Server
from request import Client

# Vytvoření serveru
server = Server()

# Vytvoření několika klientů
client1 = Client("Alice")
client2 = Client("Bob")
client3 = Client("Charlie")

# Klienti odesílají požadavky s různými prioritami
server.accept_request(client1.create_request(priority=3))
server.accept_request(client2.create_request(priority=1))
server.accept_request(client3.create_request(priority=2))

# Zpracování požadavků podle priority
server.process_requests()

# Zobrazení statistik
server.show_statistics()
