from Person import Person
from Computer import Computer
class Game:
    count=0   #Equalize
    person=Person()  #Object（Person）as attribute
    computer=Computer() #≈Objec（Computer）as attribute

    def start_game(self):
        print("---------------Fist guessing game starts ！----------------")

        while True:
            presult = self.person.punches()
            cresult = self.computer.punches()
            self.getResult(presult, cresult)
            option=input("Do you want to continue？y/n")
            if option.lower()=="n":
                break
            if self.person.score >= 5 or self.computer.score>= 5:
               option = input("Do you want to end the game？a/b")
            if option.lower() == "a":
                break
            if option.lower() == "b":
                self.count = 0
                self.person.score = 0
                self.computer.score = 0
                game.start_game()
            #output game results
        self.vs()
        print("Game Over!")
        # Score in this round

    def getResult(self, presult, cresult):
        if (presult == 1 and cresult == 2) or (presult == 2 and cresult == 3) or (presult == 3 and cresult == 1):
            self.person.score += 1
            print("YOU WIN!")
        elif presult == cresult:
            print("Equalize the score")
            self.count += 1
        else:
            self.computer.score += 1
            print("AI WIN!")

    def vs(self):
        print("-------YOU vs AI--------")
        print("you win {0} score".format(self.person.score))
        print("The computer won {0} score".format(self.computer.score))
        print("Equalize {0} score".format(self.count))
        if self.person.score>self.computer.score:
            print("YOU WIN!")
        elif self.person.score==self.computer.score:
            print("Equalize the score")
        else:
            print("AI WIN!")

game=Game()
game.start_game()