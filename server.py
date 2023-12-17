import socket
from UserInfo import UserInfo
import json

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address[0]}:{client_address[1]}")

            # Handle client request
            request = client_socket.recv(1024).decode()
            print(request)
            if request == "REGISTER":
                response = "SUCCESS"
                client_socket.send(response.encode())
                self.register_user(client_socket)

            client_socket.close()

    def register_user(self, client_socket):
        data = client_socket.recv(1024).decode()
        user_json = json.loads(data)  # Convert JSON string to Python dictionary

        # Extract user information from the dictionary
        username = user_json['userName']
        password = user_json['userPassword']
        userPhone = user_json['userPhone']

        # Save user information to database or perform any other necessary actions
        # ...

        # Send response to client
        response = "SUCCESS"
        client_socket.send(response.encode())

    def stop(self):
        if self.server_socket:
            self.server_socket.close()
            print("Server stopped")


if __name__ == "__main__":
    server = Server("localhost", 8000)
    server.start()

