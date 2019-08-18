from flask import Flask
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import threading
import turtle
def tur():
    turtle.shape("turtle")
    turtle.color("skyblue")
    turtle.write("CONNECT THE PYTHONISTAS", font=("궁서체",18,"bold"))
    turtle.done()



class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('CONNECT THE PYTHONISTAS')
        self.move(300, 300)
        self.resize(400, 200)

        # lbl = QLabel("CONNECT THE PYTHONISTAS",self)
        # lbl.move(0,0)
        lbl2 = QLabel('<a href = "http://localhost:5000">CONNECT THE PYTHONISTAS<br><center>click me</center></br></a>',self)
        lbl2.setOpenExternalLinks(True)
        lbl2.move(100,100)
        self.show()
app = Flask(__name__)
@app.route('/')
def pycon():
    return 'CONNECT THE PYTHONISTAS'

def appRun():
    app.run()
t1 = threading.Thread(target=appRun,args=())
t1.start()
t2 = threading.Thread(target=tur, args=())
t2.start()
print('CONNECTT THE PYTHONISTAS')



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



