from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton
import sys

from datetime import datetime

from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,200,700,650)
        self.setStyleSheet("background-color: pink; color: black; border: 2px solid black;")
        
        self.line = QLineEdit(self)
        self.line.setGeometry(150,50,300,40)
        self.line.setFont(QFont("Comic Sans MS",12))
        

        
        
        
        
        self.btn1 = QPushButton("Lower",self)
        self.btn1.move((self.width()-self.btn1.width())//2,20)
        self.btn1.setGeometry(150,200,200,70)
        self.btn1.setStyleSheet("background-color: yellow; color: black; border: 2px solid black;")
        
        
        self.btn2 = QPushButton("Upper",self)
        self.btn2.move((self.width()-self.btn1.width())//2,20)
        self.btn2.setGeometry(400,200,200,70)
        self.btn2.setStyleSheet("background-color: blue; color: black; border: 2px solid black;")
        
        self.btn3 = QPushButton("Lenght",self)
        self.btn3.move((self.width()-self.btn1.width())//2,20)
        self.btn3.setGeometry(150,300,200,70)
        self.btn3.setStyleSheet("background-color: red; color: black; border: 2px solid black;")
        
        self.btn4 = QPushButton("Reverse",self)
        self.btn4.move((self.width()-self.btn1.width())//2,20)
        self.btn4.setGeometry(400,300,200,70)
        self.btn4.setStyleSheet("background-color: green; color: black; border: 2px solid black;")
        
        
        self.btn5 = QPushButton("Sana",self)
        self.btn5.move((self.width()-self.btn1.width())//2,20)
        self.btn5.setGeometry(270,400,200,70)
        self.btn5.setStyleSheet("background-color: orange; color: black; border: 2px solid black;")
        
        
        
        
        self.label_result=QLabel("Result: ",self)
        self.label_result.setFont(QFont("Comic Sans MS",12))
        self.label_result.move(50,150)
        self.label_result.setStyleSheet("background-color: black; color: yellow; border: 2px solid black;")
        self.label_res = QLineEdit(self)
        self.label_res.setGeometry(140,150,200,30)
        self.label_res.setFont(QFont("Comic Sans MS",12))
        self.label_res.setReadOnly(True)
        self.label_res.hide()
        self.label_result.hide()
        self.label_res.setStyleSheet("background-color: black; color: white; border: 2px solid white;")
        
        
        self.btn1.clicked.connect(self.lower)
        self.btn2.clicked.connect(self.upper)
        self.btn3.clicked.connect(self.lenght)
        self.btn4.clicked.connect(self.reverse)
        self.btn5.clicked.connect(self.sana)
        


        
        
    def lower(self):
        text=self.line.text()
        text=text.lower()
        self.label_res.setText(text)
        self.label_res.show()
        self.label_result.show()
        
    def upper(self):
        text=self.line.text()
        text=text.upper()
        self.label_res.setText(text)
        self.label_res.show()
        self.label_result.show()
        
    def lenght(self):
        text=self.line.text()
        lenght=len(text)
        self.label_res.setText(str(lenght)) 
        self.label_res.show()
        self.label_result.show()       
        
    def reverse(self):
        text=self.line.text()
        text=text[::-1]
        self.label_res.setText(text)
        self.label_res.show()
        self.label_result.show()


    def sana(self):
        current_time = datetime.now()
        text = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.label_res.setText(text)
        self.label_res.show()
        self.label_result.show()

        
        
        
app=QApplication([])

window=Calculator()
window.show()

app.exec_()