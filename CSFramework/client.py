import socket
from CSFramework.UserInfo import UserInfo
import json


class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def register_user(self, useraccount, userpassword, username):
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
                return self.send_register_info(
                    client_socket, useraccount, userpassword, username
                )
            else:
                print("Failed to press the register button.")
                return None

        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_register_info(self, client_socket, useraccount, userpassword, username):
        client_socket.sendall(useraccount.encode())
        client_socket.sendall(userpassword.encode())
        client_socket.sendall(username.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()

        if response == "SUCCESS":
            print("User registered successfully!")
            return UserInfo(useraccount, userpassword, username)
        else:
            print("Failed to register user.")
            return None

    def login_user(self, useraccount, userpassword):
        try:
            # Create a TCP socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to the server
            client_socket.connect((self.server_host, self.server_port))

            # Send the registration request
            request = "LOGIN"
            client_socket.sendall(request.encode())

            # Receive the response from the server
            response = client_socket.recv(1024).decode()

            if response == "SUCCESS":
                return self.send_login_info(client_socket, useraccount, userpassword)
            else:
                print("Failed to press the login button.")
                return None

        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_login_info(self, client_socket, useraccount, userpassword):
        client_socket.sendall(useraccount.encode())
        client_socket.sendall(userpassword.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()

        if response == "SUCCESS":
            data = client_socket.recv(1024).decode()
            user_json = json.loads(data)
            useraccount = user_json["userAccount"]
            userpassword = user_json["userPassword"]
            username = user_json["userName"]

            if useraccount is None or userpassword is None or username is None:
                return None

            print("User login successfully!")
            return UserInfo(useraccount, userpassword, username)

        else:
            print("Failed to login user.")
            return None


if __name__ == "__main__":
    client = Client("localhost", 8000)
    client.register_user(UserInfo("17326120763", "password123", "John Doe"))
