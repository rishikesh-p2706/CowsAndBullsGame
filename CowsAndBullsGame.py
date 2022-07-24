import random

def num_generator():
    '''THIS FUNCTION GENERATES THE NUMBER FOR THE GAME'''
    com_num=random.sample("0123456789",4)
    com_num="".join(com_num)
    return com_num

def player_input():
    '''THIS FUNCTION TAKES THE INPUT FROM THE USER AND
    COMPARES IT AGAINST ALL POSSIBLE ERRORS'''
    while(True):
        try:
            global player_num
            z=player_num=input("ENTER YOUR NUMBER: ")
            z=int(z)
            '''THIS CONDITION CHECKS WHETHER 
            THE NUMBER IS OF 4 DIGIT'''
            if (len(player_num)!=4):
                print("ENTER A 4 DIGIT NUMBER: ")
                continue
        except ValueError:
            '''THIS BLOCK HANDLES THE ERROR 
            IF ALPHABETS ARE ENTERED INSTEAD OF NUMBERS '''
            print("THE VALUE YOU ENTERED YOU IS NOT A NUMBER")
        else:
            x=0
            for i in range(0,4):
                x+=player_num.count(player_num[i])
                '''THIS CONDITION CHECKS WHETHER 
                THE NUMBER HAS ANY REPETIONS OR NOT'''
            if (x!=4):
                print("ENTER THE NUMBER WITH DIFFERENT DIGITS")
            else:
                return

def num_comparision(a,b):
    '''THIS FUNCTION CALCULATES
    THE NUMBER OF COWS AND BULLS COUNT'''
    a=str(a)
    b=str(b)
    for i in range(0,4):
        for j in range(0,4):
            if i==j and a[i]==b[j]:
                global cow_count
                cow_count+=1
            elif i!=j and a[i]==b[j]:
                global bull_count
                bull_count+=1
            else:
                pass

print("------COWS AND BULLS GAME------")
print("RULES:\n"
      "1. THE NUMBER YOU HAVE ENTERED MUST HAVE ONLY 4 DIFFERENT DIGITS\n"
      "2. IF THE PLACE VALUE OF A NUMBER IS SAME AS THAT OF COMPUTER'S NUMBER THAT IS COUNTED AS A COW\n"
      "3. IF THE PLACE VALUE IS DIFFERENT THEN IT IS BULL")
print("Have fun...")
player_num=0
user_choice=True
while(user_choice):
    cow_count=0
    bull_count=0
    game_num=num_generator()
    score_counter=0
    while(True):
        player_input()
        score_counter+=1
        num_comparision(game_num,player_num)
        if cow_count==4:
            print("YOU WON"
                  "TOU HAVE COMPLETED GAME IN",str(score_counter),"CHANCES")
            print("DO YOU WANT TO PLAY THE AGAIN"
                  "ENTR \"y\" TO PLAY AGAIN"
                  "ELSE ENTER ANY KEY TO EXIT")
            choice=input("ENTER YOUR CHOICE: ")
            if choice=="y":
                user_choice=True
            else:
                user_choice=False
            break
        else:
            print("cow_count",cow_count)
            print("bull_count",bull_count)
            cow_count=0
            bull_count=0