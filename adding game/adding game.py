from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random


class Window(QMainWindow):  # define window
    def __init__(self):  # windows parameter
        super().__init__()

        self.setWindowTitle("calculator game for kids")  # set window title
        self.setGeometry(0, 0, 600, 400)  # set window size and location
        self.UiComponents()  # refer to UiComponents below to show
        self.show()  # shoing the ui and all the window components

    def UiComponents(self):  # call this a folder for ui elements
        self.title = QLabel("Calculator game for kids", self)  # set header of the game
        self.title.setGeometry(250, 10, 1000, 20)  # s4tting header geometry

        self.n1 = QLabel(" ", self)  # set number 1 label to not have strings
        self.n1.setGeometry(230, 30, 1000, 20)  # set size of number 1
        self.n2 = QLabel(" ", self)  # set plus sign
        self.n2.setGeometry(275, 30, 1000, 20)  # set size of plus sign
        self.n3 = QLabel(" ", self)  # set number 2 label to not have string
        self.n3.setGeometry(300, 30, 1000, 20)  # set size of number 2
        self.n4 = QLabel(" ", self)  # set of equal sign
        self.n4.setGeometry(325, 30, 1000, 20)  # set size of equal sign
        self.n5 = QLineEdit(self)  # set the awnser box for the question
        self.n5.setGeometry(350, 30, 50, 20)  # set geometry for answer box
        self.n5.setVisible(False)  # setting the opacity of the text box to 0%
        self.result = QLabel(" ", self)  # setting result lable to be invisible
        self.result.setGeometry(
            285, 170, 1000, 20
        )  # setting the size of the result label
        self.mt = QLabel("Minimum number", self)  # setting header for minimum number
        self.mt.setGeometry(
            20, 25, 100, 20
        )  # setting size and pos of minimum number header
        self.mta = QLabel("Maximum number", self)  # setting maximum number header
        self.mta.setGeometry(
            20, 75, 100, 20
        )  # setting the size and pos of maximum number header
        self.score = QLabel("Score Streak : ", self)  # setting lable for score streak
        self.score.setGeometry(
            460, 5, 100, 20
        )  # set size of scoore streak label and pos
        self.n6 = QLabel("0", self)  # set the showing score number
        self.n6.setGeometry(
            550, 5, 100, 20
        )  # set the position of the showing score number and size

        self.minval = QLineEdit(
            "1", self
        )  # set the textbox for minimum value and note that the value is automatically set to 1 which can be changed
        self.minval.setGeometry(20, 50, 100, 20)  # set the textbox size and position
        self.maxval = QLineEdit(
            "10", self
        )  # set the textbox for maximum value and note that the vakue is automatically set to 10 which can be changed
        self.maxval.setGeometry(20, 100, 100, 20)  # set the textbox size and position

        self.btn1 = QPushButton(
            "start / next", self
        )  # setting the start and next button
        self.btn1.setGeometry(
            207, 50, 200, 50
        )  # setting the size and position of the button
        self.btn1.clicked.connect(
            self.start
        )  # connecting button on pressed to the def function start
        self.btn2 = QPushButton("check", self)  # setting the check ans button
        self.btn2.setGeometry(
            207, 110, 200, 50
        )  # setting the check ans button size and position
        self.btn2.clicked.connect(
            self.test
        )  # connect button on pressed to the def function test

    def start(self):  # start def function start
        min = self.minval.text()  # reading val of mininum value
        max = self.maxval.text()  # reading val of maximum value
        minint = int(min)  # changing from min (as a string) to integer
        maxint = int(max)  # changing from max (as a string) to integer
        x = random.randint(
            minint, maxint
        )  # first number random number due to the max and min val
        y = random.randint(
            minint, maxint
        )  # second number random number due to the max and min val

        self.n1.setText(str(x))  # set text for num 1
        self.n3.setText(str(y))  # set text for num 2
        self.n2.setText("+")  # set text for plus
        self.n4.setText("=")  # set text for equals
        self.n5.setVisible(True)  # showing the previously invisible textbox visible

    def test(self):  # start def test
        a = self.n1.text()  # reading value of number 1
        b = self.n3.text()  # reading vcalue of number 2
        c = int(
            a
        )  # changing number 1 from string to integer (because string cant add each other)
        d = int(
            b
        )  # changing number 2 from string to integer (because string cant add each other)
        e = c + d  # setting the vaulue of number 1 plus number 2
        f = self.n5.text()  # reading value of the textbox (ans)
        g = int(f)  # changing value of textbox from string to int
        # result
        h = self.result.text()  # reading value of result label
        # score
        i = self.n6.text()  # reading value of score
        j = int(i)  # changing from string to int (score)

        if e == g:  # if the added value = the number typed in the text box,
            self.result.setText("Correct!")  # let the result label say correct
        else:
            self.result.setText("Incorrect")  # if not then say incorrect
            # score
            j = (
                j - j
            )  # when wrong the current score which is j is set back to 0 via j - j (current number - current number)
            j = str(
                j
            )  # then change the number which is now 0 to a string so it can be shown
            self.n6.setText(j)  # showing the number by n6 label (score)

        if h == "Correct!":  # if the result label said correct!
            min = (
                self.minval.text()
            )  # note that line 130 -142 is the same as line 81 - 95. this was only for reoeating the test
            max = self.maxval.text()
            minint = int(min)
            maxint = int(max)
            x = random.randint(minint, maxint)
            y = random.randint(minint, maxint)

            self.n1.setText(str(x))
            self.n3.setText(str(y))
            self.n2.setText("+")
            self.n4.setText("=")
            self.n5.clear()  # clearing the textbox value
            self.result.clear()  # clearing the result label
            # score
            j = j + 1  # if it is correct then add j by 1 using j = j + 1
            j = str(j)  # then make the j which is a int turns into a string to be shown
            self.n6.setText(j)  # showing the j value


# closing the porgram
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
