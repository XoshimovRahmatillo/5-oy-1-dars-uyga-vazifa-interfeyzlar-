
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 800, 500) 
        self.setStyleSheet("background: #006000")
        
        
        
        self.txt_username = QLabel("Username: ", self)
        self.txt_username.setStyleSheet("QLabel { color: red; font-size: 24px; }")
        self.username = QLineEdit(self)
        self.username.setStyleSheet("QLineEdit { color: red; font-size: 24px; }")
        self.username.setPlaceholderText("Enter username...")
        self.font(self.txt_username, 20, 100)
        self.font(self.username, 200, 100)
        

     
        self.txt_email = QLabel("Email: ", self)
        self.txt_email.setStyleSheet("QLabel { color: purple; font-size: 24px; }")
        self.email = QLineEdit(self)
        self.email.setStyleSheet("QLineEdit { color: purple; font-size: 24px; }")
        self.email.setPlaceholderText("Enter email...")
        self.font(self.txt_email, 20, 200)
        self.font(self.email, 200, 200)


        self.txt_password = QLabel("Password: ", self)
        self.txt_password.setStyleSheet("QLabel { color: blue; font-size: 24px; }")
        self.password = QLineEdit(self)
        self.password.setStyleSheet("QLineEdit { color: blue; font-size: 24px; }")
        self.password.setPlaceholderText("Enter password...")
        self.font(self.txt_password, 20, 300)
        self.font(self.password, 200, 300)
        self.password.setEchoMode(QLineEdit.Password)


        self.eye_button = QPushButton("👁️", self)
        self.eye_button.setCheckable(True)
        self.eye_button.clicked.connect(self.pasword_see)
        self.eye_button.setGeometry(475, 305, 50, 30)

       
        self.reset_button = QPushButton("Clear", self)
        self.reset_button.setStyleSheet("QPushButton {background-color: green; color: yellow}")
        self.font(self.reset_button, 20, 400)
        self.reset_button.setFixedWidth(350)
        self.reset_button.clicked.connect(self.clear)

      
        self.register_button = QPushButton("Register", self)
        self.register_button.setStyleSheet("QPushButton {background-color: black; color: white}")
        self.font(self.register_button, 20, 350)
        self.register_button.setFixedWidth(350)
        self.register_button.clicked.connect(self.register)

        self.show()

    def clear(self):
        self.username.setText("")
        self.email.setText("")
        self.password.setText("")

    def pasword_see(self):
        if self.eye_button.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def register(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        

        if not username or not email or not password:
            QMessageBox.warning(self, "Input Error", "Please fill all fields!")
            return


        QMessageBox.information(self, "Registration Successful", f"Welcome, {username}!")
        
    def font(self, obj, x, y):
        obj.setFont(QFont("Comic Sans MS", 12))  
        obj.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    sys.exit(app.exec_())
