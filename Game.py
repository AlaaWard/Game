import os
def clearss():
    os.system("cls")
class Board:
    def __init__(self):
        self.board=["1","2","3","4","5","6","7","8","9"]
    def display_board(self):
        for i in range(0,9,3):
         print("|".join(self.board[i:i+3]))
         if i<9:
            print("_"*5)        
    def update_board(self,choice,symbol):
        if self.isvaledmove(choice):
           self.board[choice-1]=symbol
           return True
        return False
    def isvaledmove(self,choice):
        return self.board[choice-1].isdigit()
    def reset_board(self):
        self.board=["1","2","3","4","5","6","7","8","9"]              
class Player:
    def __init__(self):
        self.__name=""
        self.__symb=""
  
    
    def choice_name(self):
        while True:
            name=input("Enter your name ( only chars) :")
            if name.isalpha():
                self.name=name
                break
            else:    
                print("error reenter ")
    
    def choice_symbol(self):
        while True:
            symbol=input("Enter your symbol (just one char) :")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            else:    
                print("error reenter ")            
class Menu:
    def display_menu(self):
        print("welcome to my game ::")
        print("1-start game " )
        print("2-end game  ")
        while True:
            c=input("enter 1 or 2 : ")
            if c=='1' or c=='2' :
                break
            else:
                print("please choice 1 or 2 ")
        return c        
    def display_endgame(self):
        print("game over ")
        print("1-restart game " )
        print("2-end game  ")
        while True:
            c=input("enter 1 or 2 : ")
            if c=='1' or c=='2' :
                break
            else:
                print("please choice 1 or 2 ")
        return c 
class Game:
    def __init__(self):
        self.Players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.currentplayer_index=0
    def start_Game(self):
        choice=self.menu.display_menu()
        if int(choice)==1:    
            self.setup_players()
            self.playGame()
        else:
            self.Quit_game()
    def setup_players(self):
        for number, player in enumerate(self.Players, start=1):
            print(f"Plyaer {number} enter your detalis : ")
            player.choice_name()
            player.choice_symbol()
            clearss()
    def playGame(self):
        while True:
            self.play_turn()
            if self.chick_win() or self.chick_draw():
             choice=self.menu.display_endgame()
             print(choice)
             if choice=='1':
                clearss()
                self.restart_game()
             else:
                self.Quit_game()
                break
                            
                        
    def restart_game(self):
        self.board.reset_board()
        self.currentplayer_index=0
        self.playGame()
    def chick_win(self):
        win_states=[[0,1,2],[3,4,5],[6,7,8],   #rows
                    [0,3,6],[1,4,7],[2,5,8],   #culums
                    [0,4,8],[2,4,6]]          
        for state in win_states:
            if (self.board.board[state[0]]==self.board.board[state[1]]==self.board.board[state[2]]):
               the_winner_player_index=1-self.currentplayer_index 
               print(f"the player { self.Players[the_winner_player_index].name} is the Winner")
               return True
        return False    
    def chick_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
            
                        
    def play_turn(self):
        player=self.Players[self.currentplayer_index]    
        self.board.display_board()
        print(f"{player .name} your turn ( {player.symbol} )")  
        while True:
            try:
                cell=int(input(" choice a cell (1-9)"))
                if cell<=9 and cell>=1 and self.board.update_board(cell, player.symbol):
                    break
                else:
                 print("error try again! ")
            except ValueError:
                print(" please enter number between (1-9)")            
        self.switch_player() 
    def switch_player(self):
       self.currentplayer_index= 1- self.currentplayer_index              
    def Quit_game(self):
        clearss()
        print("thank you for Playing !")
game=Game()
game.start_Game()
    
                        