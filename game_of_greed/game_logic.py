from random import randint
from collections import Counter

class GameLogic:
    def __init__(self) :
        counter=0

    @staticmethod
    def roll_dice(num_dice):
        return tuple([randint(1,6) for _ in range(0,num_dice)])
   
    @staticmethod
    def get_scorers(roll_dice):
        """
        function will take a tuple of integers that represent a dice roll and return the srore of this roll 
        """
        score = 0
        counting = Counter(roll_dice)
        dice_common = counting.most_common()
        # return tuple(dice_common)
        if len(dice_common)== 6:
            score=1500
            # self.counter+=6
            return  score
        if len(dice_common)== 3:
            if dice_common[0][1]==2 and dice_common[1][1]==2 and dice_common[2][1]==2:
                score=1500
                # self.counter+=6
                return  score

        for i in dice_common:
            if i[1]<3:    #[(1,2)]
                if i[0]==1:
                    score+=i[1]*100
                    # self.counter+=1*i[1]
                 
                elif  i[0]==5:
                    score+=i[1]*50
                    # self.counter+=1*i[1]
            if i[1]==3:
                if i[0]==1:
                    score+=1000
                    # self.counter+=1*i[1]
                else:
                    score+=i[0]*100
                    # self.counter+=1*i[1]
            if i[1]==4:
                if i[0]==1:
                    score+=2000
                    # self.counter+=1*i[1]
                else:
                    score+=i[0]*200
                    # self.counter+=1*i[1]
            if i[1]==5:
                if i[0]==1:
                    score+=3000
                    # self.counter+=1*i[1]
                else:
                    score+=i[0]*300
                    # self.counter+=1*i[1]
            if i[1]==6:
                if i[0]==1:
                    score+=4000
                    # self.counter+=1*i[1]
                else:
                    score+=i[0]*400
                    # self.counter+=1*i[1]
                 
        return score
        
class Banker :
    def __init__(self):
        self.shelved=0
        self.balance=0

    def shelf (self,points):
        self.shelved+=points
    def bank(self):
        self.balance=0
        self.balance+=self.shelved
        self.shelved=0
        return self.balance

    def clear_shelf (self):
        self.shelved=0