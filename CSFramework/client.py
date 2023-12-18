import socket
from CSFramework.UserInfo import UserInfo
import json

class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def register_user(self, userinfo: UserInfo):
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
                self.send_register_info(client_socket, userinfo)
            else:
                print("Failed to press the register button.")
            
        
        except ConnectionRefusedError:
            print("Failed to connect to the server.")
    
    # 用户登录
    def login_user(self, userinfo: UserInfo):
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
                self.send_login_info(client_socket, userinfo)
            else:
                print("Failed to press the register button.")
            
        
        except ConnectionRefusedError:
            print("Failed to connect to the server.")

    def send_register_info(self, client_socket, userinfo: UserInfo):
        # Send the registration request
        user_json = json.dumps(userinfo.__dict__)  # Convert user object to JSON string
        client_socket.sendall(user_json.encode())  # Send the JSON string
        
        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        

        if response == "SUCCESS":
            print("User registered successfully!")
        else:
            print("Failed to register user.")
    
    # 发送登录信息
    def send_login_info(self, client_socket, userinfo: UserInfo):
        # Send the registration request
        user_json = json.dumps(userinfo.__dict__)  # Convert user object to JSON string
        client_socket.sendall(user_json.encode())  # Send the JSON string
        
        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        

        if response == "SUCCESS":
            print("User login successfully!")
        else:
            print("Failed to login user.")
        


if __name__ == "__main__":
    client = Client("localhost", 8000)
    client.register_user(UserInfo("17326120763", "password123", "John Doe"))

