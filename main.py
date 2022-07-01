from PyQt5.QtWidgets import  QApplication, QMainWindow, QLabel, QGraphicsColorizeEffect, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys
import random

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Камень Ножницы Бумага")
        self.setGeometry(100, 100, 800, 600)
        self.UiComponents()
        self.show()
    
    def UiComponents(self):
        self.counter = -1
        self.choice = 0
        
        headLabel = QLabel("Камень Ножницы Бумага", self)
        headLabel.setGeometry(20, 10, 760, 60)
        
        font = QFont('Times', 24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setCapitalization(QFont.AllUppercase)

        headLabel.setFont(font)
        headLabel.setAlignment(Qt.AlignCenter)

        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        headLabel.setGraphicsEffect(color)

        self.vsLabel = QLabel("против", self)

        self.vsLabel.setGeometry(350, 195, 100, 100)

        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setItalic(False)
        self.vsLabel.setFont(font)

        self.userLabel = QLabel("Вы", self)

        self.userLabel.setGeometry(20, 90, 310, 310)
        self.userLabel.setStyleSheet("border : 2px solid black; background: white;")
        self.userLabel.setAlignment(Qt.AlignCenter)

        self.computerLabel = QLabel("Компьютер", self)

        self.computerLabel.setGeometry(470, 90, 310, 310)
        self.computerLabel.setStyleSheet("border : 2px solid black; background : white;")
        self.computerLabel.setAlignment(Qt.AlignCenter)

        self.resultLabel = QLabel(self)
        self.resultLabel.setGeometry(20, 410, 760, 60)
        self.resultLabel.setFont(QFont('Times', 24))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setStyleSheet("border : 2px solid black; background : white;")

        self.rockBtn = QPushButton("Камень", self)
        self.rockBtn.setGeometry(20, 480, 240, 50)
 
        self.scissorBtn = QPushButton("Ножницы", self)
        self.scissorBtn.setGeometry(280, 480, 240, 50)

        self.paperBtn = QPushButton("Бумага", self)
        self.paperBtn.setGeometry(540, 480, 240, 50)

        self.rockBtn.clicked.connect(self.rockBtnAction)
        self.paperBtn.clicked.connect(self.paperBtnAction)
        self.scissorBtn.clicked.connect(self.scissorsBtnAction)

        gameResetBtn = QPushButton("Перезагрузить", self)

        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.red)

        gameResetBtn.setGeometry(20, 540, 760, 50)
        gameResetBtn.setGraphicsEffect(color)

        gameResetBtn.clicked.connect(self.resetBtnAction)

        timer = QTimer(self)
 
        timer.timeout.connect(self.showTime)
        timer.start(1000)
 

    def showTime(self):
 
        if self.counter == -1:
            pass
        else:        
            self.computerLabel.setText(str(self.counter))
            if self.counter == 0:
                self.computerChoice = random.randint(1, 3)
                if self.computerChoice == 1:
                    pixmap = QPixmap('rock.png')
                    self.computerLabel.setPixmap(pixmap)
                elif self.computerChoice == 2:
                    pixmap = QPixmap('scissors.png')
                    self.computerLabel.setPixmap(pixmap)
                else:
                    pixmap = QPixmap('paper.png')
                    self.computerLabel.setPixmap(pixmap)
 
                self.whoWon()

            self.counter -= 1

    def rockBtnAction(self):
        self.choice = 1
        self.counter = 3
        pixmap = QPixmap('rock.png')
        self.userLabel.setPixmap(pixmap)
        self.rockBtn.setDisabled(True)
        self.paperBtn.setDisabled(True)
        self.scissorBtn.setDisabled(True)

    def scissorsBtnAction(self):
        self.choice = 2

        pixmap = QPixmap('scissors.png')
        self.userLabel.setPixmap(pixmap)

        self.counter = 3
 
        self.rockBtn.setDisabled(True)
        self.paperBtn.setDisabled(True)
        self.scissorBtn.setDisabled(True)
    
    def paperBtnAction(self):
        self.choice = 3

        pixmap = QPixmap('paper.png')
        self.userLabel.setPixmap(pixmap)

        self.counter = 3

        self.rockBtn.setDisabled(True)
        self.paperBtn.setDisabled(True)
        self.scissorBtn.setDisabled(True)
    
    def resetBtnAction(self):
 
        self.resultLabel.setText("")
 
        self.counter = -1
 
        self.rockBtn.setEnabled(True)
        self.paperBtn.setEnabled(True)
        self.scissorBtn.setEnabled(True)
 
        self.userLabel.clear()
        self.computerLabel.clear()
        self.userLabel.setText("Вы")
        self.computerLabel.setText("Компьютер")

    def whoWon(self):

        if self.choice == self.computerChoice:
            self.resultLabel.setText("НИЧЬЯ!")
        else:
            if self.choice == 1:
                if self.computerChoice == 3:
                    self.resultLabel.setText("КОМПЬЮТЕР ПОБЕДИЛ!")
                else:
                    self.resultLabel.setText("ПОЛЬЗОВАТЕЛЬ ПОБЕДИЛ!")
            elif self.choice == 2:
                if self.computerChoice == 1:
                    self.resultLabel.setText("КОМПЬЮТЕР ПОБЕДИЛ!")
                else:
                    self.resultLabel.setText("ПОЛЬЗОВАТЕЛЬ ПОБЕДИЛ!")
            elif self.choice == 3:
                if self.computerChoice == 2:
                    self.resultLabel.setText("КОМПЬЮТЕР ПОБЕДИЛ!")
                else:
                    self.resultLabel.setText("ПОЛЬЗОВАТЕЛЬ ПОБЕДИЛ!")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())