from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #sets a fixed size of the app itself
        self.setFixedSize(272, 343)
        self.SubmitLabel.setText("")

        """
        this sets all boxes for scores invisible so later they can appear when attempts is inputed into
        """
        self.ScoreBox1.setVisible(False)
        self.ScoreBox2.setVisible(False)
        self.ScoreBox3.setVisible(False)
        self.ScoreBox4.setVisible(False)

        self.ScoreLabel1.setVisible(False)
        self.ScoreLabel2.setVisible(False)
        self.ScoreLabel3.setVisible(False)
        self.ScoreLabel4.setVisible(False)


        self.AttemptsBox.textChanged.connect(self.update_attempts)
        self.SubmitButton.clicked.connect(lambda: self.submit())

    def update_attempts(self):
        """
        Grabs name then sees if it is empty if it is then it will not let it pass/write and will return.
        """
        name : str = self.StudentBox.toPlainText()

        if name == '':
            self.SubmitLabel.setText("Enter name for student")
            return

        """
        Grabs attempts then sees if it is a empty string, then sees if it is a digit if not then also returns
        """
        attempts : str = self.AttemptsBox.toPlainText().strip()

        if attempts == '':
            self.SubmitLabel.setText("Enter amount of attempts")
            return

        if not attempts.isdigit():
            self.SubmitLabel.setText("Enter right amount of attempts 1-4")
            return

        """
        turns attepts into a integer, then sees if it is between the min and max of 1-4.
        """
        attempts: int = int(attempts)

        if attempts <= 0 or attempts > 4:
            self.SubmitLabel.setText("Enter amount of attempts 1-4")
            return

        """
        for how many attepts checks if it is greater than each one and then sets the visiblilitys
        on the boxes and labels True if they had that many attempts.
        """
        if attempts >= 1:
            self.ScoreBox1.setVisible(True)
            self.ScoreLabel1.setVisible(True)
        if attempts >= 2:
            self.ScoreBox2.setVisible(True)
            self.ScoreLabel2.setVisible(True)
        if attempts >= 3:
            self.ScoreBox3.setVisible(True)
            self.ScoreLabel3.setVisible(True)
        if attempts >= 4:
            self.ScoreBox4.setVisible(True)
            self.ScoreLabel4.setVisible(True)



    def submit(self):
        """
        Everything is the same for update_attempts
        """
        name : str = self.StudentBox.toPlainText().strip()

        if name == '':
            self.SubmitLabel.setText("Enter name for student")
            return


        attempts : str = self.AttemptsBox.toPlainText().strip()

        if attempts == '':
            self.SubmitLabel.setText("Enter amount of attempts")
            return


        if not attempts.isdigit():
            self.SubmitLabel.setText("Enter amount of attempts 1-4")
            return

        attempts : int = int(attempts)

        if attempts <= 0 or attempts > 4:
            self.SubmitLabel.setText("Enter amount of attempts 1-4")
            return




        if attempts >= 1:
            self.ScoreBox1.setVisible(True)
            self.ScoreLabel1.setVisible(True)
        if attempts >= 2:
            self.ScoreBox2.setVisible(True)
            self.ScoreLabel2.setVisible(True)
        if attempts >= 3:
            self.ScoreBox3.setVisible(True)
            self.ScoreLabel3.setVisible(True)
        if attempts >= 4:
            self.ScoreBox4.setVisible(True)
            self.ScoreLabel4.setVisible(True)



        """
        for each score it will grab it then check if its a blank and if so it will just be a string of 0.
        then turns it into a integer, after this it will check if it is between the min and max of 0-100 
        if so it passes if not then it returns.
        """
        score1 : str = self.ScoreBox1.toPlainText().strip()
        if score1 == '':
            score1 = '0'
        score1 : int = int(score1)
        if score1 > 100 or score1 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score2 : str = self.ScoreBox2.toPlainText().strip()
        if score2 == '':
            score2 = '0'
        score2 : int = int(score2)
        if score2 > 100 or score2 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score3 : str = self.ScoreBox3.toPlainText().strip()
        if score3 == '':
            score3 = '0'
        score3 : int = int(score3)
        if score3 > 100 or score3 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score4 : str = self.ScoreBox4.toPlainText().strip()
        if score4 == '':
            score4 = '0'
        score4 : int = int(score4)
        if score4 > 100 or score4 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        """
        first is just a list of all scores and what they are. Then cuts taht list to the amount of attempts
        taken. After this does the average calcualation. 
        """
        total_scores = [score1, score2, score3, score4]
        scores = total_scores[:attempts]
        average : int = int(sum(scores) / len(scores))



        """
        Now it opens the CSV file and writes the row in order from
        name, score1, score2, score3, score4, average
        """
        with open('Grades.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, score1, score2, score3, score4, average])


        """
        Finally sets the label to nothing since they did everything right.
        then clears all boxes. After that it turns all the score boxes invisible
        and sets cursor onto the student name box
        """
        self.SubmitLabel.setText("")


        self.StudentBox.clear()
        self.AttemptsBox.clear()
        self.ScoreBox1.clear()
        self.ScoreBox2.clear()
        self.ScoreBox3.clear()
        self.ScoreBox4.clear()

        for box in [self.ScoreBox1, self.ScoreBox2, self.ScoreBox3, self.ScoreBox4]:
            box.setVisible(False)

        for label in [self.ScoreLabel1, self.ScoreLabel2, self.ScoreLabel3, self.ScoreLabel4]:
            label.setVisible(False)


        self.StudentBox.setFocus()



