from Trivia_model import Question
from Trivia_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html


question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)





print("Du har gjort klart quizet!")
print(f"Din totala poäng är: {quiz.score}/{quiz.question_no}")