# Starter
starter = input("Are you ready?")

if starter == "y" or starter == "Y":
    print("Let's go!")
else:
    quit()

# Questions database
q_dict = {"1": "Who is the most handsome teacher in mapleleaf?\nA. Mr. Lee\nB. Mr. Berg\nC. Mr. Lycan",
          "2": "Did Jerry eat a lot every day?\nA. Yes\nB. Not at all",
          "3": "How tall of Mr.Lee?\nA. 150cm\nB. 160cm\nC. 170cm\nD. 180cm"}

a_dict = {"1": "a",
          "2": "b",
          "3": "d"}

# Number initialization
q_right = 0
q_wrong = 0

# Body
for q_n in range(1, len(q_dict) + 1):
    print("\n", q_dict[str(q_n)])
    answer = input()
    if answer == a_dict[str(q_n)]:
        q_right = q_right + 1
        print("\nYou are right!")
    else:
        q_wrong = q_wrong + 1
        print("\nYou are wrong! The right answer is", a_dict[str(q_n)])
else:
    print("Your got", q_right, "answer right",
          q_wrong, "answer wrong, Well done!")
