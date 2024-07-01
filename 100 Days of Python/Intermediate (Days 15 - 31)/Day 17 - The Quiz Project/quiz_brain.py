class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list) # Boolean Return

    def check_question(self, user_answer, question):
        if user_answer == question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is {question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)").lower()
        self.check_question(user_answer, question)
    
    