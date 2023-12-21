import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import QFile, QTextStream
from CSFramework.client import Client
from CSFramework.UserInfo import UserInfo
import re


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.current_page = "Register"
        self.client = Client("localhost", 8000)
        self.user = None

    def init_ui(self):
        self.setWindowTitle("登录/注册")
        self.setGeometry(300, 300, 600, 400)

        self.load_stylesheet("style/style.qss")
        # 创建界面元素
        self.label_account = QLabel("账户:")
        self.label_password = QLabel("密码:")
        self.label_confirm_password = QLabel("确认密码:")
        self.label_username = QLabel("用户名:")


        self.edit_account = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_confirm_password = QLineEdit()
        self.edit_username = QLineEdit()

        # 设置密码输入框的回显模式为密码
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_confirm_password.setEchoMode(QLineEdit.Password)

        self.button_register = QPushButton("注册")
        self.button_register.clicked.connect(self.show_registration_fields)

        self.button_login = QPushButton("登录")
        self.button_login.clicked.connect(self.show_login_fields)

        self.button_confirm = QPushButton("确认")
        self.button_confirm.clicked.connect(self.confirm_button_clicked)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.button_register)
        layout.addWidget(self.button_login)
        layout.addLayout(self.create_form_layout())
        layout.addWidget(self.button_confirm)

        self.setLayout(layout)

        self.show()

    def create_form_layout(self):
        form_layout = QVBoxLayout()

        form_layout.addWidget(self.label_account)
        form_layout.addWidget(self.edit_account)
        form_layout.addWidget(self.label_password)
        form_layout.addWidget(self.edit_password)
        form_layout.addWidget(self.label_confirm_password)
        form_layout.addWidget(self.edit_confirm_password)
        form_layout.addWidget(self.label_username)
        form_layout.addWidget(self.edit_username)

        return form_layout

    def hide_registration_fields(self):
        self.label_username.hide()
        self.edit_username.hide()
        self.label_confirm_password.hide()
        self.edit_confirm_password.hide()

    def show_registration_fields(self):
        self.hide_registration_fields()
        self.label_username.show()
        self.edit_username.show()
        self.label_confirm_password.show()
        self.edit_confirm_password.show()
        self.edit_account.setText("")
        self.edit_password.setText("")
        self.edit_confirm_password.setText("")
        self.edit_username.setText("")
        self.current_page = "Register"

    def show_login_fields(self):
        self.hide_registration_fields()
        self.edit_account.setText("")
        self.edit_password.setText("")
        self.current_page = "Login"

    def confirm_button_clicked(self):
        # 处理确认按钮点击事件

        if self.current_page == "Register":
            if not re.match(r'^\d{6}$', self.edit_account.text()):
                QMessageBox.critical(self, "错误", "账户格式不正确")
                return
            # 处理有的信息为空的情况
            if (
                self.edit_account.text() == ""
                or self.edit_password.text() == ""
                or self.edit_confirm_password.text() == ""
                or self.edit_username.text() == ""
            ):
                print("尚未填写某些信息")
                QMessageBox.information(self, "提示", "尚未填写某些信息")
                return
            

            if self.edit_password.text() != self.edit_confirm_password.text():
                print("两次输入的密码不一致！")
                QMessageBox.information(self, "提示", "两次输入的密码不一致！")
                return
            useraccount = self.edit_account.text()
            userpassword = self.edit_password.text()
            username = self.edit_username.text()

            self.user = self.client.register_user(useraccount, userpassword, username)
            if self.user is not None:
                print(f"用户 {useraccount} 注册成功！")
            else:
                QMessageBox.information(self, "提示", "用户已存在")

            # 这里可以添加保存用户信息或其他相关操作

        elif self.current_page == "Login":
            if self.edit_account.text() == "" or self.edit_password.text() == "":
                print("尚未填写某些信息")
                QMessageBox.information(self, "提示", "尚未填写某些信息")
                return

            useraccount = self.edit_account.text()
            userpassword = self.edit_password.text()

            self.user = self.client.login_user(useraccount, userpassword)

            if self.user is not None:
                print(f"用户 {useraccount} 登录成功！")
            else:
                QMessageBox.information(self, "提示", "账户名或密码错误")
            
            # 这里可以添加登录逻辑

    def load_stylesheet(self, filename):
        # 从文件中加载样式表
        file = QFile(filename)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qq_style_registration_window = RegistrationWindow()
    sys.exit(app.exec_())
