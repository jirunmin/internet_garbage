import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout
from PyQt5.QtCore import QFile, QTextStream

class QQStyleRegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QQ风格登录/注册界面')
        self.setGeometry(300, 300, 600, 400)

        self.load_stylesheet('style.qss')
        # 创建界面元素
        self.label_account = QLabel('账户:')
        self.label_password = QLabel('密码:')
        self.label_confirm_password = QLabel('确认密码:')
        self.label_username = QLabel('用户名:')

        self.edit_account = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_confirm_password = QLineEdit()
        self.edit_username = QLineEdit()

        self.button_register = QPushButton('注册')
        self.button_register.clicked.connect(self.show_registration_fields)

        self.button_login = QPushButton('登录')
        self.button_login.clicked.connect(self.show_login_fields)

        self.button_confirm = QPushButton('确认')
        self.button_confirm.clicked.connect(self.confirm_button_clicked)

        # 隐藏初始时不需要的输入框
        self.hide_registration_fields()

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

    def hide_login_fields(self):
        self.label_username.hide()
        self.edit_username.hide()
        self.label_confirm_password.hide()
        self.edit_confirm_password.hide()

    def show_login_fields(self):
        self.hide_login_fields()

    def confirm_button_clicked(self):
        # 处理确认按钮点击事件
        if self.button_register.isChecked():
            username = self.edit_username.text()
            print(f"用户 {username} 注册成功！")
            # 这里可以添加保存用户信息或其他相关操作
        elif self.button_login.isChecked():
            account = self.edit_account.text()
            print(f"用户 {account} 登录成功！")
            # 这里可以添加登录逻辑

    def load_stylesheet(self, filename):
        # 从文件中加载样式表
        file = QFile(filename)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qq_style_registration_window = QQStyleRegistrationWindow()
    sys.exit(app.exec_())
