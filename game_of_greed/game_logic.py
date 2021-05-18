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
    starting_round =1
    dice_num_remaining =6
    score = 0
    num_shelf = 0
    flag = True
    banker = Banker()

    def __init__(self,roll=None):
        self.roll = roll or GameLogic.roll_dice


    def welcome(self):
        print("Welcome to Game of Greed") 
        user_in=input("Wanna play?")
        if user_in=="n":
            print("OK. Maybe another time")
        elif user_in=="y":
            self.play()
        else:
            print("invalid input ")



    def start_round(self):
        while self.flag == True:
            print(f"Rolling {self.dice_num_remaining} dice...")
            rolled = self.roll(self.dice_num_remaining)
            print(','.join([str(x) for x in rolled]))
            dice_to_keep=input("Enter dice to keep (no spaces), or (q)uit: ") # "12"        
            if dice_to_keep == 'q':
                self.quitter()      
            else:
                copy_rolled=list(rolled)
                new_list = list(dice_to_keep) ### Here ###
                counter_checker=0       
                for x in new_list:
                    for y in range(len(rolled)):
                        if int(x)==copy_rolled[y]:
                            copy_rolled[y]=0
                            counter_checker+=1
                            break
                if counter_checker==len(new_list):
                    user_t=[]
                    for i in new_list : 
                        user_t.append(int(i)) 
                    start_play = GameLogic()
                    self.num_shelf += start_play.calculate_score(tuple(user_t))
                    print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining-len(new_list)} dice remaining')
                    next_input = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    if next_input == 'q':
                        self.quitter()                    
                    
                    elif next_input == 'b':
                        self.save_bank()                        
                        break
                    elif next_input == 'r':
                        self.roll_again(new_list)                        
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining} dice remaining')
                    print(','.join([str(x) for x in rolled]))
            dice_to_keep=input("Enter dice to keep (no spaces), or (q)uit: ") # "12"        
            if dice_to_keep == 'q':
                self.quitter()      
            else:
                copy_rolled=list(rolled)
                new_list = list(dice_to_keep) ### Here ###
                counter_checker=0       
                for x in new_list:
                    for y in range(len(rolled)):
                        if int(x)==copy_rolled[y]:
                            copy_rolled[y]=0
                            counter_checker+=1
                            break
                if counter_checker==len(new_list):
                    user_t=[]
                    for i in new_list : 
                        user_t.append(int(i)) 
                    start_play = GameLogic()
                    self.num_shelf += start_play.calculate_score(tuple(user_t))
                    print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining-len(new_list)} dice remaining')
                    next_input = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    if next_input == 'q':
                        self.quitter()                    
                    
                    elif next_input == 'b':
                        self.save_bank()                        
                        break
                    elif next_input == 'r':
                        self.roll_again(new_list)                        
                else:
                    # rewrite function to pick Cheaters 
                    print("Cheater!!! Or possibly made a typo...")
                    print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining} dice remaining')
                    print(','.join([str(x) for x in rolled]))



                    next_input = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    copy_rolled=list(rolled)
                    new_list = list(dice_to_keep) ### Here ###
                    counter_checker=0       
                    for x in new_list:
                        for y in range(len(rolled)):
                            if int(x)==copy_rolled[y]:
                                copy_rolled[y]=0
                                counter_checker+=1
                                break
                    if counter_checker==len(new_list):
                        user_t=[]
                        for i in new_list : 
                            user_t.append(int(i)) 
                        start_play = GameLogic()
                        self.num_shelf += start_play.calculate_score(tuple(user_t))
                        print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining-len(new_list)} dice remaining')
                        next_input = input(f'(r)oll again, (b)ank your points or (q)uit ')
                        if next_input == 'q':
                            self.quitter()                    
                        
                        elif next_input == 'b':
                            self.save_bank()                        
                            break
                        elif next_input == 'r':
                            self.roll_again(new_list)                        
                       
                
                       



    

    def quitter(self):
        print(f'Total score is {self.score} points')
        print(f'Thanks for playing. You earned {self.score} points')
        self.flag = False


    def save_bank(self):
        self.dice_num_remaining = 6
        self.banker.shelf(self.num_shelf)
        banked = self.banker.bank()
        self.num_shelf=0
        self.score+=banked
        print(f'You banked {banked} points in round {self.starting_round}')
        print(f'Total score is {self.score} points')
        self.starting_round+=1
    
    def roll_again(self,new_list):                        
        self.num_shelf+=self.banker.shelved
        self.dice_num_remaining-=len(new_list)
        self.flag = True        


    def play(self):
        while self.score < 10000 and self.flag ==True:
            print(f"Starting round {self.starting_round}")
            self.start_round()



    

if __name__ == '__main__':
    play = Game()
    play.welcome()
# print(roll.roll_dice(6))
# print(roll.calculate_score((3,3,5,5,6,6)))
# counting = Counter((1,1,3,3,5,5))
# dice_common = counting.most_common()
# print(dice_common)