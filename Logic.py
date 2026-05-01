from PyQt6.QtWidgets import *
from gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(272, 343)

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
        name = self.StudentBox.toPlainText().strip()

        if name == '':
            self.SubmitLabel.setText("Enter name for student")
            return

        attempts = self.AttemptsBox.toPlainText().strip()

        if attempts == '':
            self.SubmitLabel.setText("Enter amount of attempts")
            return

        if not attempts.isdigit():
            self.SubmitLabel.setText("Enter amount of attempts 1-4")
            return

        attempts = int(attempts)

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


    def submit(self):
        name = self.StudentBox.toPlainText().strip()

        if name == '':
            self.SubmitLabel.setText("Enter name for student")
            return


        attempts = self.AttemptsBox.toPlainText().strip()

        if attempts == '':
            self.SubmitLabel.setText("Enter amount of attempts")
            return


        if not attempts.isdigit():
            self.SubmitLabel.setText("Enter amount of attempts 1-4")
            return

        attempts = int(attempts)

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




        score1 = self.ScoreBox1.toPlainText().strip()
        if score1 == '':
            score1 = '0'
        score1 = int(score1)
        if score1 > 100 or score1 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score2 = self.ScoreBox2.toPlainText().strip()
        if score2 == '':
            score2 = '0'
        score2 = int(score2)
        if score2 > 100 or score2 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score3 = self.ScoreBox3.toPlainText().strip()
        if score3 == '':
            score3 = '0'
        score3 = int(score3)
        if score3 > 100 or score3 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        score4 = self.ScoreBox4.toPlainText().strip()
        if score4 == '':
            score4 = '0'
        score4 = int(score4)
        if score4 > 100 or score4 < 0:
            self.SubmitLabel.setText("Enter right score")
            return

        total_scores = [score1, score2, score3, score4]
        scores = total_scores[:attempts]
        average = int(sum(scores) / len(scores))




        with open('Grades.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, score1, score2, score3, score4, average])

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



