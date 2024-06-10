class GuessingGame():
    def __init__(self, answer):
        self.answer = answer 
        self.result = False 

    def guess(self,user_guess):
        if user_guess > self.answer:
            self.result = False 
            return "high"
        elif user_guess < self.answer:
            self.result = False
            return "low"
        elif user_guess == self.answer:
            self.result = True
            return "correct"
    
    def solved(self):
        return self.result 
    
