import random

# --- Player Class
class Player:
    def __init__(self, name):
        self._name = name
        self._wincount = 0
        self._hand = None
    
    def result(self, result):
        if True == result:
            self._wincount += 1
    
    # randomly generate hand function
    def generate_hand(self):
        return random.randint(0, 2)
    
    def get_wincount(self):
        return self._wincount
    
    def get_name(self):
        return self._name
    
    def get_hand(self):
        while True:
            try:
                choice = int(input("Enter your choice (0 for Goo, 1 for Choki, 2 for Par): "))
                if choice in [0, 1, 2]:
                    self._hand = choice
                    return self._hand 
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    

# --- Judge Class
class Judge:      
    # function to convert number to string
    def hand_to_string(hand):
        return ["Goo", "Choki", "Par"][hand]
    
    # function to determine winner
    def judge(player1, player2):
        # define
        winner = None
        p1_hand = player1.get_hand()
        #p2_hand = player2.get_hand()
        p2_hand = player2.generate_hand()
        
        # print
        print(f'{player1.get_name()} : {Judge.hand_to_string(p1_hand)}')
        print(f'{player2.get_name()} : {Judge.hand_to_string(p2_hand)}') 
        
        # judge
        if p1_hand == p2_hand:
            pass
        elif (p1_hand == 0 and p2_hand == 2) or (p1_hand == 1 and p2_hand == 0) or (p1_hand == 2 and p2_hand == 1):
            winner = player1
        else:
            winner = player2
        
        return winner
    
    def judge_finalwinner(player1,player2):
        # define
        winner = None
        player1Wincount = player1.get_wincount()
        player2Wincount = player2.get_wincount()
        
        # judge
        if player1Wincount > player2Wincount:
            winner = player1
        elif player2Wincount > player1Wincount:
            winner = player2
            
        return winner


# --- Simulate the game
def main():
    playerA = Player(input("Enter your name: "))
    playerB = Player('cpu')
    
    print('--- start ---')
    for n in range(3):
        print(f'--- round {n} ---')      
        winner = Judge.judge(playerA, playerB)
        if winner != None:
            print(winner.get_name(),'wins')
            winner.result(True)
        else:
            print('draw')
    
    print('\n--- result ---')
    finalWinner = Judge.judge_finalwinner(playerA, playerB)
    print(f'{playerA.get_name()} : {playerA.get_wincount()}, {playerB.get_name()}, {playerB.get_wincount()}')
    if finalWinner != None:
        print(finalWinner.get_name(),'wins')
    else:
        print('draw')
    
    return 0

if __name__ == '__main__':
    main()