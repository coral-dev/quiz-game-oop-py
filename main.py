from question_model import Question
from question_brain import QuestionBrain
from data import question_data

question_bank = []

def create_question_bank():
    for question in question_data:
        new_question = Question(question['text'], question['answer'])
        question_bank.append(new_question)

create_question_bank()
question_brain = QuestionBrain(question_bank)
while question_brain.still_has_questions():
    question_brain.next_question()

print("You've completed the quiz")
print(f"Your final score is {question_brain.score}/{len(question_bank)}")

