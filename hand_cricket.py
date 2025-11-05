import random
import time
computer_score=0
player_score=0
Count=0
#choosing
def assign(comp,player):
    if player=='Heads':
        comp='Tails'
    if player=='Tails':
        comp='Heads'
    return comp
player=int(input('0 = Heads\n1 = Tails\nHeads or Tails:'))
if player==0:
    player='Heads'
if player==1:
    player='Tails'
#toss
computer=assign(None,player)
toss=random.randint(0,1)
def Toss(toss):
    if toss==0:
        return 'Heads'
    if toss==1:
        return 'Tails'
a=Toss(toss)
#result
print(f'Computer is {computer}')
print(f'You are {player}')
time.sleep(1)
print(f'Toss is {a}')
def result():
    if a==player:
        print('--you won the toss--')
        return 0
    if a==computer:
        print('--Computer won the toss--')
        return 1
Result=result()
time.sleep(1)
#player's choice
if Result==0:
    def Choice(Result):
        player_choice=int(input('0 > Batting\n1 > Bowling:'))
        if player_choice==0:
            player_choice='Batting'
        if player_choice==1:
            player_choice='Bowling'
        return player_choice
    
    player_choice=Choice(Result)
    print(f'You choose {player_choice}')
    #Player batting
    if player_choice=='Batting':
        while True:
            computer_bowling=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_bowling}')
            Count+=1
            player_score+=player
            if Count==1 and computer_bowling==player:
                player_score-=player
                print(f"your'e score = {player_score}")
                break
            if computer_bowling==player:
                print(f'No.of balls = {Count}')
                player_score-=player
                print(f"your'e score = {player_score}")
                break
    # computer batting
        time.sleep(1)
        print("Now Computer is batting\nYou are bowling")
        CP='Batting'
        Count=0
        while True:
            computer_batting=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_batting}')
            Count+=1
            computer_score+=computer_batting
            if Count==1 and computer_batting==player:
                computer_score-=computer_batting
                print(f'Computer score = {computer_score}')
                break
            if computer_batting==player:
                print(f'No.of balls = {Count}')
                computer_score-=computer_batting
                print(f'Computer score = {computer_score}')
                if computer_score==player_score:
                    time.sleep(1)
                    print('--DRAW--')
                if computer_score>player_score:
                    time.sleep(1)
                    print("--Computer won--")
                if player_score>computer_score:
                    time.sleep(1)
                    print("--you won--")
                break
            if computer_score>player_score:
                time.sleep(1)
                print(f'No.of balls = {Count}')
                print(f'Computer score = {computer_score}')
                time.sleep(1)
                print("--Computer won--")
                break

    #Player bowling
    if player_choice=='Bowling':
        while True:
            computer_batting=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_batting}')
            Count+=1
            computer_score+=computer_batting
            if computer_batting==player:
                computer_score-=computer_batting
                print(f'No.of balls = {Count}')
                print(f'Computer score = {computer_score}')
                break
        print("Now your'e Batting\nComputer is Bowling")
    #computer bowling
        CP='Bowling'
        Count=0
        while True:
            computer_bowling=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_bowling}')
            Count+=1
            player_score+=player
            if computer_bowling==player:
                print(f'No.of balls = {Count}')
                player_score-=player
                print(f'Your score = {player_score}')
                if player_score==computer_score:
                    time.sleep(1)
                    print("--DRAW--")
                if player_score>computer_score:
                    time.sleep(1)
                    print("--you won--")
                if computer_score>player_score:
                    time.sleep(1)
                    print("--Computer won--")
                    break
            if player_score>computer_score:
                    time.sleep(1)
                    print(f'No.of balls = {Count}')
                    print(f'Your score = {player_score}')
                    time.sleep(1)
                    print("--you won--")
                    break
            
    #computer's choice
if Result==1:
    def cp(Result):
            comp=random.choice(['Batting','Bowling'])
            return comp
    CP=cp(Result)
    print(f'Computer is {CP}') 
    #computer batting
    if CP=='Batting':
        while True:
            computer_batting=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_batting}')
            Count+=1
            computer_score+=computer_batting
            if Count==1 and computer_batting==player:
                computer_score-=computer_batting
                print(f'Computer score = {computer_score}')
                break
            if computer_batting==player:
                print(f'No.of balls = {Count}')
                computer_score-=computer_batting
                print(f'Computer score = {computer_score}')
                break
    #Player batting
        time.sleep(1)
        print("Now you are Batting\nComputer is Bowling")
        player_choice='Batting'
        Count=0
        while True:
            computer_bowling=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_bowling}')
            Count+=1
            player_score+=player
            if Count==1 and computer_bowling==player:
                print('Player score = 0')
                break
            if player==computer_bowling:
                print(f'No.of balls = {Count}')
                player_score-=player
                print(f"your'e score = {player_score}")
                if computer_score==player_score:
                    time.sleep(1)
                    print('--DRAW--')
                if computer_score>player_score:
                    time.sleep(1)
                    print("Computer won")
                if player_score>computer_score:
                    time.sleep(1)
                    print("you won")
                break
            if player_score>computer_score:
                time.sleep(1)
                print(f'No.of balls = {Count}')
                print(f"your'e score = {player_score}")
                time.sleep(1)
                print("you won")
                break 
            
            
    #computer bowling
    if CP=='Bowling':
        while True:
            computer_bowling=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_bowling}')
            Count+=1
            player_score+=player
            if computer_bowling==player:
                player_score-=player
                print(f'No.of balls = {Count}')
                print(f'Your score = {player_score}')
                break
        time.sleep(1)
        print("Now Computer is Batting\nYour'e Bowling")
    # player bowling
        player_choice='Bowling'
        Count=0
        while True:
            computer_batting=random.randint(1,10)
            player=int(input('PLAYER:'))
            print(f'Comp = {computer_batting}')
            Count+=1
            computer_score+=computer_batting
            if computer_batting==player:
                print(f'No.of balls = {Count}')
                computer_score-=computer_batting
                print(f'Computer score = {computer_score}')
                if player_score==computer_score:
                    time.sleep(1)
                    print("--DRAW--")
                if player_score>computer_score:
                    time.sleep(1)
                    print("--you won--")
                if computer_score>player_score:
                    time.sleep(1)
                    print("--Computer won--")
                break
            if computer_score>player_score:
                    time.sleep(1)
                    print(f'No.of balls = {Count}')
                    print(f'Computer score = {computer_score}')
                    time.sleep(1)
                    print("--computer won--")
                    break