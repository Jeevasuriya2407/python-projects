#need to add the list of questions
#need to build a function
import random

questions={
    "The leargest beach in tamilnadu is? ":"marina",
    "The name of the containers which holds the value is? ":"variables",
    "the datatype which is used to store decimal values is? ":"float",
    "Sequence of characters can be referred as? ":"string",
    "The datatype which returns true or false is called? ":"boolean",
    "the datastructure which are muttable are called? ":"list",
    "the data structure which are immutable are called? " : "tuples",
    "which type of loop is used to repeat a block of code until a condition is true? ":"while",
    "the oops concept which is used to perform operator overloading is called? ":"polymorphism",
    "which keyword is used to build customized error message in python? ":"raise"
    }

def trivia_game():
    
    question_list=list(questions.keys())
    total_question=5
    score=0
    select_question=random.sample(question_list,total_question)
    
    for idx,question in enumerate(select_question):
        print(f"{idx+1}.{question}")
        user_answer=input("enter the answer: ").lower().strip()
        correct_answer=questions[question]
        if user_answer==correct_answer:
            print("correct answer!!!")
            score+=1
        else:
            print(f"the answer is wrong and the correct answer is {correct_answer}")
    print(f"Game over and the total score is {score}")
    

trivia_game()
    