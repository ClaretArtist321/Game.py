class Person(object):
    #attribute：name,score
    #method：punches
    def __init__(self,score=0):
        self.score=score

    #Fist guessing method
    def punches(self):
        type=None #To expand the scope, declare this variable outside the loop
        while True:
            print("Please punch：")
            type=input("1.Rock 2.scissor 3.paper")
            if type.isdigit():
                type=int(type)
                if type == 1:
                    print("Your fist is Rock")
                    break
                elif type == 2:
                    print("Your fist is scissor")
                    break
                elif type == 3:
                    print("Your fist is paper")
                    break
                else:
                    print("Input error")
            else:
                print("Only numbers can be entered")
        return type  #When calling other classes, you need to get the result of punching