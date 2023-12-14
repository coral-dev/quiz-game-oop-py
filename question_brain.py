class QuestionBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} True/False?")
        self.question_number += 1
        self.check_answer(user_answer, self.question_list[self.question_number - 1].answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong:(")
        print(f"The correct answer if {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


