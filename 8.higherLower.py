import random
import higherLowerlogo
import higherlowerdata8
import os

print(higherLowerlogo.game_logo)
score=0
def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},{description}, from{country}"

def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else :
            return False
        
account2=random.choice(higherlowerdata8.data)        
continue_flag=True       
while continue_flag : 
    account1=account2
    account2=random.choice(higherlowerdata8.data)
    if account1==account2:
        account2=random.choice(higherlowerdata8.data)
    print(f"compare 1: {display_accountinfo(account1)}")
    print(higherLowerlogo.Vs)
    print(f"compare 2: {display_accountinfo(account2)}")

    guess=int(input("who hasMore followers ?  type 1 or 2:"))
    followers_count_1=account1["follower_Count"]
    followers_Count2=account2["follower_Count"]
    

    is_Correct =check_answer(guess,followers_count_1,followers_Count2)
    os.system('cls')
    print(higherLowerlogo.game_logo)   
    if  is_Correct==True:
        score +=1
        print(f"you are right.your score is :{score}")
    else:
        print(f"you are wrong.your score is:{score} ")
        continue_flag=False
    
    
display_accountinfo(account1)
display_accountinfo(account2)








