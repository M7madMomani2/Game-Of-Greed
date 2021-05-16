from random import randint, sample
class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
   
    @staticmethod
    def calculate_score(self):
        first_roll=self.roll_dice(6)

class Banker :
    def __init__(self) -> None:
        pass

    def shelf (self):
        pass
    def bank(self,point):
        pass 

    def clear_shelf (self):
        pass