from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QMessageBox
import sys

from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,200,700,650)
        
        
        self.label_num1=QLabel("Numb_1: ",self)
        self.label_num1.setFont(QFont("Comic Sans MS",12))
        self.label_num1.move(50,50)
        self.label_1 = QLineEdit(self)
        self.label_1.setPlaceholderText("Enter num1...")
        self.label_1.setGeometry(150,50,200,30)
        self.label_1.setFont(QFont("Comic Sans MS",12))
        
        
        self.label_num2=QLabel("Numb_2: ",self)
        self.label_num2.setFont(QFont("Comic Sans MS",12))
        self.label_num2.move(50,100)
        self.label_2 = QLineEdit(self)
        self.label_2.setPlaceholderText("Enter num2...")
        self.label_2.setGeometry(150,100,200,30)
        self.label_2.setFont(QFont("Comic Sans MS",12))
        
        self.btn1 = QPushButton("+",self)
        self.btn1.move((self.width()-self.btn1.width())//2,20)
        self.btn1.setGeometry(50,200,100,30)
        self.btn1.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        self.btn2 = QPushButton("-",self)
        self.btn2.move((self.width()-self.btn1.width())//2,20)
        self.btn2.setGeometry(150,200,100,30)
        self.btn2.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        self.btn3 = QPushButton("*",self)
        self.btn3.move((self.width()-self.btn1.width())//2,20)
        self.btn3.setGeometry(250,200,100,30)
        self.btn3.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        self.btn4 = QPushButton("/",self)
        self.btn4.move((self.width()-self.btn1.width())//2,20)
        self.btn4.setGeometry(350,200,100,30)
        self.btn4.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        self.btn5 = QPushButton("//",self)
        self.btn5.move((self.width()-self.btn1.width())//2,20)
        self.btn5.setGeometry(450,200,100,30)
        self.btn5.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        self.btn6 = QPushButton("%",self)
        self.btn6.move((self.width()-self.btn1.width())//2,20)
        self.btn6.setGeometry(550,200,100,30)
        self.btn6.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setGeometry(150,300,250,60)
        self.reset_button.clicked.connect(self.reset)
        
        
        
        
        self.label_result=QLabel("Result: ",self)
        self.label_result.setFont(QFont("Comic Sans MS",12))
        self.label_result.move(50,250)
        self.label_res = QLineEdit(self)
        self.label_res.setGeometry(140,250,200,30)
        self.label_res.setFont(QFont("Comic Sans MS",12))
        self.label_res.setReadOnly(True)
        self.label_res.hide()
        self.label_result.hide()
        
        self.btn1.clicked.connect(self.calculate_add)
        self.btn2.clicked.connect(self.calculate_sub)
        self.btn3.clicked.connect(self.calculate_kopaytirish)
        self.btn4.clicked.connect(self.calculate_butun_bolish)
        self.btn5.clicked.connect(self.calculate_qoldiqsiz_bolish)
        self.btn6.clicked.connect(self.calculate_qoldiq_bolish)
        
        

    
    def calculate_add(self):
        add=int(self.label_1.text())+int(self.label_2.text())
        self.label_res.setText(str(add))
        self.label_res.show()
        self.label_result.show()
        
        
    def calculate_sub(self):
        add=int(self.label_1.text())-int(self.label_2.text())
        self.label_res.setText(str(add))
        self.label_res.show()
        self.label_result.show()
            
                    
    def calculate_kopaytirish(self):
        add=int(self.label_1.text())*int(self.label_2.text())
        self.label_res.setText(str(add))
        self.label_res.show()
        self.label_result.show()
        
        
    def show_error(self):
        xato = QMessageBox()
        xato.setIcon(QMessageBox.Critical)
        xato.setText("0 ga bo'linmaydi")
        xato.setWindowTitle("Error")
        xato.setStandardButtons(QMessageBox.Ok)
        xato.exec_()

    def calculate_butun_bolish(self):
        
        try:
            self.label_num1 = int(self.label_1.text())
            self.label_num2= int(self.label_2.text())
            if self.label_num2 == 0:
                self.show_error()
                return
            else:
                result = self.label_num1 / self.label_num2
                self.label_res.setText(str(result))
            self.label_res.show()
            self.label_result.show()
        except ValueError:
            self.label_res.setText("Invalid input")
            self.label_result.show()
            self.label_res.show()
    
    def calculate_qoldiq_bolish(self):
        try:
            self.label_num1 = int(self.label_1.text())
            self.label_num2= int(self.label_2.text())
            if self.label_num2 == 0:
                self.show_error()
                return
            else:
                result = self.label_num1 % self.label_num2
                self.label_res.setText(str(result))
            self.label_res.show()
            self.label_result.show()
        except ValueError:
            self.label_res.setText("Invalid input")
            self.label_result.show()
            self.label_res.show()
    
    def calculate_qoldiqsiz_bolish(self):
        try:
            self.label_num1 = int(self.label_1.text())
            self.label_num2= int(self.label_2.text())
            if self.label_num2 == 0:
                self.show_error()
                return
            else:
                result = self.label_num1 // self.label_num2
                self.label_res.setText(str(result))
            self.label_res.show()
            self.label_result.show()
        except ValueError:
            self.label_res.setText("Invalid input")
            self.label_result.show()
            self.label_res.show()
    
    
    def reset(self):
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_result.setText("")
        self.label_res.hide()
        self.label_result.hide()
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())