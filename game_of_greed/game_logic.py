from random import randint, sample
from collections import Counter
class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
   
    @staticmethod
    def calculate_score(roll_dice):
        """
        function will take a tuple of integers that represent a dice roll and return the srore of this roll 
        """
        score = 0

        counting = Counter(roll_dice)
        dice_common = counting.most_common()
        # return tuple(dice_common)
        if len(dice_common)== 6:
            score=1500
            return  score
        if len(dice_common)== 3:
            if dice_common[0][1]==2 and dice_common[1][1]==2 and dice_common[2][1]==2:
                 score=1500
                 return  score
        for i in dice_common:
            if i[1]<3:
                if i[0]==1:
                    score+=i[1]*100
                 
                elif  i[0]==5:
                    score+=i[1]*50
            if i[1]==3:
                if i[0]==1:
                    score+=1000
                else:
                    score+=i[0]*100
            if i[1]==4:
                if i[0]==1:
                    score+=2000
                else:
                    score+=i[0]*200
            if i[1]==5:
                if i[0]==1:
                    score+=3000
                else:
                    score+=i[0]*300
            if i[1]==6:
                if i[0]==1:
                    score+=4000
                else:
                    score+=i[0]*400
                 
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



class Game :
    def __init__(self,roll=None):
        self.roll = roll or GameLogic.roll_dice


    def play(self):
        
        print("Welcome to Game of Greed") 
        user_in=input("Wanna play?")
        if user_in=="n":
            print("OK. Maybe another time")
        elif user_in=="y":
            starting_round =1
            dice_num_remaining =6
            score = 0
            num_shelf = 0
            flag = True

            while score < 10000 and flag ==True:
                print(f"Starting round {starting_round}")
                while flag == True:
                    print(f"Rolling {dice_num_remaining} dice...")
                    rolled = self.roll(dice_num_remaining)
                    print(','.join([str(x) for x in rolled]))
                    dice_to_keep=input("Enter dice to keep (no spaces), or (q)uit: ") # "12"
                    if dice_to_keep == 'q':
                        print(f'Total score is {score} points')
                        print(f'Thanks for playing. You earned {score} points')
                        flag = False
                    else:
                        # dice_num_remaining-=1
                        new_list = list(dice_to_keep) ### Here ###
                        # print(new_list)
                        user_t=[]
                        for i in new_list :
                            user_t.append(int(i)) 
                        start_play = GameLogic()
                        banker = Banker()
                        num_shelf += start_play.calculate_score(tuple(user_t))
                        print(f'You have {num_shelf} unbanked points and {dice_num_remaining-len(new_list)} dice remaining')
                        next_input = input(f'(r)oll again, (b)ank your points or (q)uit ')
                        if next_input == 'q':
                            print(f'Total score is {score} points')
                            print(f'Thanks for playing. You earned {score} points')
                            flag = False
                        elif next_input == 'b':
                            dice_num_remaining = 6
                            banker.shelf(num_shelf)
                            banked = banker.bank()
                            num_shelf=0
                            score+=banked
                            print(f'You banked {banked} points in round {starting_round}')
                            print(f'Total score is {score} points')
                            starting_round+=1
                            break
                        elif next_input == 'r':
                            num_shelf+=banker.shelved
                            dice_num_remaining-=1
                            flag = True
        else:
            print("invalid input ")

if __name__ == '__main__':
    play = Game()
    play.play()
# print(roll.roll_dice(6))
# print(roll.calculate_score((3,3,5,5,6,6)))
# counting = Counter((1,1,3,3,5,5))
# dice_common = counting.most_common()
# print(dice_common)