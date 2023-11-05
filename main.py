from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for i in range(0,12):
    texts=question_data[i]["text"]
    answers=question_data[i]["answer"]
    choice=Question(texts,answers)
    question_bank.append(choice)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{12}")