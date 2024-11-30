class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
       question = input(f"\nQ.{self.question_number + 1}: {self.question_list[self.question_number].text}(True / False)?: ")
       answer = self.check_answers(question)
       self.question_number += 1
       return answer

    def check_answers(self, ans):
        if self.question_list[self.question_number].answer == ans:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer is: {self.question_list[self.question_number].answer}")
            print(f"Your score is: {self.score}/{self.question_number + 1}")
        else:
            print("You got it wrong!")
            print(f"The correct answer is: {self.question_list[self.question_number].answer}")
            print(f"Your score is: {self.score}/{self.question_number + 1}")