import random
class Computer(object):
    name="AI"
    score=0   #score
    #computer play
    def punches(self):
        rd=random.randint(1,3)
        if rd==1:
            print("AI dispaly is Rock")
        elif rd==2:
            print("AI dispaly is scissor")
        else:
            print("AI dispaly is paper")
        return rd