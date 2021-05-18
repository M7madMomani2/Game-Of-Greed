from collections import Counter
from game_of_greed.game_logic import GameLogic,Banker

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.game = GameLogic()
        self.banker = Banker()
        self.starting_round = 1
        self.dice_num_remaining = 6
        self.score = 0
        self.num_shelf = 0
        self.flag = False
      
    def play(self,roller):
        print('Welcome to Game of Greed')
        user_input = input("(y)es to play or (n)o to decline\n> ")
        if user_input == 'n':
            print('OK. Maybe another time')
        elif user_input == 'y':
            self.start_round()

    def start_round(self):
        while self.score < 10000 and self.flag == False:
            print(f'Starting round {self.starting_round}')
            self.dice_num_remaining = 6
            self.roll_again()

    def quitter(self):
        print(f'Total score is {self.score} points')
        print(f'Thanks for playing. You earned {self.score} points')
        self.flag = True
        
    def validate_in(self, user_in, roller):
        roll_saved = Counter(tuple([int(x) for x in roller]))
        saved_inputs = Counter(tuple([int(x) for x in user_in]))
        check = True
        for i in saved_inputs:
            if saved_inputs[i] > roll_saved[i]:
                check = False
        return check
        
    def valid_cases(self, new_list):
        self.dice_num_remaining = self.dice_num_remaining - len(new_list)
        print(f'You have {self.num_shelf} unbanked points and {self.dice_num_remaining} dice remaining')
        next_input = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
        if len(new_list) == 6 and self.num_shelf > 0:
            self.dice_num_remaining = 6            
        if next_input == 'b':
            self.banked()
        elif next_input == 'q':
            self.quitter()
        elif next_input == 'r':
            self.num_shelf += self.banker.shelved
            self.roll_again()

    def banked(self):
        self.banker.shelf(self.num_shelf)
        banked = self.banker.bank()
        self.num_shelf = 0
        self.score += banked
        print(f"You banked {banked} points in round {self.starting_round}")
        self.starting_round += 1
        print(f'Total score is {self.score} points')

    def zilch(self,validate):
        print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
        print(f'You banked {validate} points in round {self.starting_round}')
        print(f'Total score is {self.score} points')
        self.starting_round += 1
        self.dice_num_remaining = 6
        print(f'Starting round {self.starting_round}')
        self.roll_again()  

    def roll_again(self):

        print(f'Rolling {self.dice_num_remaining} dice...')
        roller = self.roller(self.dice_num_remaining)
        print(f"***{' '.join([str(i) for i in roller])}***")
        new_list = list(roller)
        validate = self.game.get_scorers(tuple([int(x) for x in new_list]))

        if validate != 0:   
            dice_to_keep = input("Enter dice to keep, or (q)uit:\n> ")

            if dice_to_keep == 'q':
                self.quitter()
            else :
                valid = self.validate_in(dice_to_keep, roller)

                while valid == False:
                    print('Cheater!!! Or possibly made a typo...')
                    print(f"***{' '.join([str(i) for i in roller])}***")
                    dice_to_keep = input("Enter dice to keep, or (q)uit:\n> ")
                    if dice_to_keep == 'q':
                        self.quitter()
                        break
                    else:
                        valid = self.validate_in(dice_to_keep, roller)

                new_list = list(dice_to_keep)
                total = self.game.get_scorers(tuple([int(x) for x in new_list]))
                self.num_shelf += total
                self.valid_cases(new_list)

        elif  validate == 0: 
            self.zilch(validate)

if __name__ == '__main__':
    game = Game()
    game.play()