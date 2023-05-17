from quiz_brain import QuizBrain, Question
import requests


amount_of_questions_pick=[str(i) for i in range(1,101)]
category_pick=[str(i) for i in range(1,13)]

while True:
    amount=input("How much questions (from 1 to 100) do you want in this quiz? : ")
    if amount not in amount_of_questions_pick:
        print("Wrong number, write again")
    else:
        break

print("\n")

while True:
    type=input("What category would be interesting for you?\n"
               "1:General Knowledge\n"
                "2:Entertainment: Books\n"
                "3:Entertainment: Film\n"
                "4:Entertainment: Music\n"
                "5:Entertainment: Musicals & Theatres\n"
                "6:Entertainment: Television\n"
                "7:Entertainment: Video Games\n"
                "8:Entertainment: Board Games\n"
                "9:Science & Nature\n"
                "10:Science: Computers\n"
                "11:Science: Mathematics\n"
                "12:Mythology\n\n"
               "Type here number of your pick:  ")
    if type not in category_pick:
        print("Wrong pick, try again")
    else:
        break

print("\n")

page=requests.get("https://opentdb.com/api.php?amount="+str(amount)+"&category="+str(int(type)+8)+"&type=boolean")
questions1=page.json()
results=questions1["results"]


question_bank=[Question(results[k]["question"],results[k]["correct_answer"]) for k in range(len(results))]
quiz=QuizBrain(question_bank)

while quiz.still_has_questions()==True:
    quiz.next_question()
    quiz.pointation()
    print("")

print(f"You've completed the quiz, your final score is {quiz.get_final_score()}")
