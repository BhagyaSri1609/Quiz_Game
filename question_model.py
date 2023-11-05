import data
import random



class Question:
    
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
# i=1
# score=1
# def assign(Question, option):
#     question=Question(option["text"],option["answer"])
#     return question

# def check_answer(i, score, question, choice):
#     if choice==question.answer:
#         print("You got it right!")
#         print(f"The correct answer was: {question.answer}.")
#         print(f"Your current score is: {score}/{i}")
#         return 1
#     else:
#         print("Thats wrong.")
#         print(f"The correct answer was: {question.answer}.")
#         print(f"Your current score is: {score}/{i}")
#         return 1

# def user_answer(i, question):
#     choice=input(f"Q.{i}: {question.text} (True/False)?: ")
#     return choice

# def options(indexing):
#     option=data.question_data[indexing]
#     return option

# def random_index():
#     indexing=random.randint(0,11)
#     return indexing

# play_again=True
# while play_again:
#     indexing = random_index()
#     option = options(indexing)
#     question = assign(Question, option)
#     choice = user_answer(i, question)
#     checking_answer=check_answer(i, score, question, choice) 
#     if checking_answer==0:
#         play_again=False
#     else:
#         play_again=True
#     i+=1
    