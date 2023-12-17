import socket
from UserInfo import UserInfo
import json

class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def register_user(self, username, password):
        try:
            # Create a TCP socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the server
            client_socket.connect((self.server_host, self.server_port))
            
            # Send the registration request
            request = "REGISTER"
            client_socket.sendall(request.encode())

            # Receive the response from the server
            response = client_socket.recv(1024).decode()
            

            if response == "SUCCESS":
                self.send_register_info(client_socket, username, password)
            else:
                print("Failed to press the register button.")
            
            # Close the socket
            client_socket.close()
        
        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_register_info(self, client_socket, username, password):
        # Send the registration request
        user = UserInfo(username, password, username)
        user_json = json.dumps(user.__dict__)  # Convert user object to JSON string
        client_socket.sendall(user_json.encode())  # Send the JSON string
        
        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        

        if response == "SUCCESS":
            print("User registered successfully!")
        else:
            print("Failed to register user.")
        


# Usage example
client = Client("localhost", 8000)
client.register_user("john_doe", "password123")
