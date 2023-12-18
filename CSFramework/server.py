import socket
from UserInfo import UserInfo
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import json
import sys

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

        self.init_db()

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
            if request == "REGISTER":
                response = "SUCCESS"
                client_socket.send(response.encode())
                self.register_user(client_socket)
            elif request == "LOGIN":
                response = "SUCCESS"
                client_socket.send(response.encode())
                self.login_user(client_socket)

            client_socket.close()

    def init_db(self):
        # 初始化数据库连接
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName('localhost')  
        self.db.setPort(5432)  
        self.db.setDatabaseName('schoolmis')  
        self.db.setUserName('postgres')  
        self.db.setPassword('20130903ab')  

        if not self.db.open():
            print("Unable to open the database")
            sys.exit(1)

    def register_user(self, client_socket):
        data = client_socket.recv(1024).decode()
        user_json = json.loads(data)  # Convert JSON string to Python dictionary

        # Extract user information from the dictionary
        useraccount = user_json['userAccount']
        userpassword = user_json['userPassword']
        username = user_json['userName']

        query = QSqlQuery()
        query.prepare('INSERT INTO UserInfo (userAccount, userPassword, userName) VALUES (?, ?, ?)')
        query.addBindValue(useraccount)
        query.addBindValue(userpassword)
        query.addBindValue(username)

        response = "FAIL"
        if not query.exec_():
            print("Database Error, Failed to add information")
            client_socket.send(response.encode())
        else:
            print("Success")
            # Send response to client
            response = "SUCCESS"
            client_socket.send(response.encode())

        query.finish()

    # 登录函数
    def login_user(self, client_socket):
        data = client_socket.recv(1024).decode()
        user_json = json.loads(data)  # Convert JSON string to Python dictionary

        # Extract user information from the dictionary
        useraccount = user_json['userAccount']
        userpassword = user_json['userPassword']

        query = QSqlQuery()
        query.prepare('SELECT * FROM UserInfo WHERE userAccount = ? AND userPassword = ?')
        query.addBindValue(useraccount)
        query.addBindValue(userpassword)

        response = "FAIL"
        if not query.exec_():
            print("Database Error, Failed to find information")
            client_socket.send(response.encode())
        else:
            print("Success")
            # Send response to client
            response = "SUCCESS"
            client_socket.send(response.encode())

        query.finish()  

    def stop(self):
        if self.server_socket:
            self.server_socket.close()
            print("Server stopped")


if __name__ == "__main__":
    server = Server("localhost", 8000)
    server.start()

