import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QFile, QTextStream
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建界面元素
        self.setWindowTitle('注册界面')
        self.setGeometry(300, 300, 300, 200)

        self.label_username = QLabel('用户名:')
        self.label_password = QLabel('密码:')
        self.label_confirm_password = QLabel('确认密码:')

        self.edit_username = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_confirm_password = QLineEdit()

        # 设置密码输入框的回显模式为密码
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_confirm_password.setEchoMode(QLineEdit.Password)

        self.button_register = QPushButton('注册')
        self.button_register.clicked.connect(self.register_button_clicked)

        # 从样式文件中加载样式表
        self.load_stylesheet('style/style.qss')

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.edit_confirm_password)
        layout.addWidget(self.button_register)

        self.setLayout(layout)

        self.show()

    def load_stylesheet(self, filename):
        # 从文件中加载样式表
        file = QFile(filename)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

    def register_button_clicked(self):
        # 处理注册按钮点击事件
        username = self.edit_username.text()
        password = self.edit_password.text()
        confirm_password = self.edit_confirm_password.text()

        if password == confirm_password:
            print(f"用户 {username} 注册成功！")
            # 这里可以添加保存用户信息或其他相关操作
        else:
            print("密码不一致，请重新输入。")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration_window = RegistrationWindow()
    sys.exit(app.exec_())
