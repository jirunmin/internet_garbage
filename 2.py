import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Chat System")
        self.resize(400, 300)

        # Create text area for displaying messages
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)

        # Create input field for typing messages
        self.input_field = QLineEdit(self)

        # Create buttons for sending messages
        self.send_private_button = QPushButton("Send Private", self)
        self.send_group_button = QPushButton("Send Group", self)

        # Create layout for the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.input_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_private_button)
        button_layout.addWidget(self.send_group_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
