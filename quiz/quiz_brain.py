class QuizBrain():
    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.points=0

    def next_question(self):
        self.answer=input(f"Q.{self.question_number+1} {self.question_list[self.question_number].text} (True/False)?: ")
        self.question_number +=1

    def still_has_questions(self):
        return self.question_number<=len(self.question_list)-1

    def pointation(self):
        if self.answer.lower()==self.question_list[self.question_number-1].answer.lower():
            self.points+=1
            print("You got it right!")
        else:
            self.points=self.points
            print("Not this time...")
        print(f"{self.points}/{self.question_number}")

    def get_final_score(self):
        return f"{self.points}/{self.question_number}"

class Question():
    def __init__(self,text , answer):
        self.text=text
        self.answer=answer