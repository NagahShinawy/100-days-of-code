"""
created by Nagaj at 16/05/2021
"""
from prettytable import PrettyTable
from question_model import Question


class QuizBrain:
    REPORT_FIELDS = ["Status", "Score", "Total"]

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question: Question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text}. (True/False)?: "
        )
        self.check_answer(user_answer, current_question.answer)
        return current_question

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def __getitem__(self, item):
        return self.question_list[item]

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            message = "You got it right"

        else:
            message = "That's Wrong"
        print(message)
        print(f"The Correct Answer was : '{current_answer}'")
        print("Score is ({} / {})".format(self.score, self.question_number))
        print("\n")

    def report(self):
        if self.question_number == len(self.question_list):

            print("You've Completed the quiz")
            print(f"Your Final Score Was: {self.score}/{self.question_number}")
            status = "Completed"
        else:
            print("You Still Answering The Quiz")
            status = "Working"
        report = PrettyTable()
        report.field_names = QuizBrain.REPORT_FIELDS
        report.add_rows([(status, self.score, self.question_number)])
        print(report)
