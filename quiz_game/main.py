from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['question'], q['answer']))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.ask_question()

print("You have completed this quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")