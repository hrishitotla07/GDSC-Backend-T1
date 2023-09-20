from Questions import question_data
from question_blueprint import Question
from quiz_control import Quiz

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.do_questions_remain():
    quiz.next_question()

print("Your final score is:", quiz.score)
