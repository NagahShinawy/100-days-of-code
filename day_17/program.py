"""
created by Nagaj at 16/05/2021
"""

from data import question_data
from question_model import Question
from question_brain import QuizBrain


question_bank = [
    Question(text=question["text"], answer=question["answer"])
    for question in question_data
]


if __name__ == "__main__":
    print(question_bank)
    quiz = QuizBrain(question_bank)
    # for counter, question in enumerate(quiz, start=1):
    #     print(counter, question)
    # for _ in question_bank:
    #     quiz.next_question()
    quiz.report()
    while quiz.still_has_question():
        quiz.next_question()

    quiz.report()
