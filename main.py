import art
from game_data import data
import random
print(art.logo)

def format(account):
    acc_name= account["name"]
    acc_desc = account['description']
    acc_country = account['country']

    return f"{acc_name},a {acc_desc} from {acc_country}"
def check_answer(guess_ans,accounta,accountb):

    if accounta["follower_count"] > accountb["follower_count"]:
        if guess_ans == 'A':
            return True
        elif guess_ans == 'B':
            return False

    else:
        if guess_ans == 'B':
            return True
        elif guess_ans == 'A':
            return False

def higher_acc(accounta,accountb):
    if accounta["follower_count"] > accountb["follower_count"]:
        return accounta
    else:
        return accountb
score = 0
random_data1= random.choice(data)
is_correct = True

while is_correct == True:
    random_data2= random.choice(data)
    #print(f"Compare B: {random_data2["name"]},{random_data2['description']}"
         # f" from {random_data2['country']}.")

    if random_data1 == random_data2:
        random_data2 = random.choice(data)

    print(f"Compare A: {format(random_data1)}")
    print(art.vs)
    print(f"Compare B: {format(random_data2)}")
    print("acc a",random_data1["follower_count"])
    print("acc b",random_data2["follower_count"])
    guess=input("Who has more followers? Type 'A' or 'B': ").upper()
    is_correct = check_answer(guess,random_data1,random_data2)
    if is_correct== True:
        score= score+1
    print("score, ", score)

    random_data1 =    higher_acc(random_data1,random_data2)