class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def do_questions_remain(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}:{current_question.text}:(True or False):");
        user_answer = input()
        self.is_correct(user_answer, current_question.answer)

    def is_correct(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 2
        else:
            self.score -= 1
