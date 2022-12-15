print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
love_score = 0

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
t_count = lower_case_name1.count("t") + lower_case_name2.count("t")
r_count = lower_case_name1.count("r") + lower_case_name2.count("r")
u_count = lower_case_name1.count("u") + lower_case_name2.count("u")
e_count = lower_case_name1.count("e") + lower_case_name2.count("e")
true_count = str(t_count + r_count + u_count + e_count)

l_count = lower_case_name1.count("l") + lower_case_name2.count("l")
o_count = lower_case_name1.count("o") + lower_case_name2.count("o")
v_count = lower_case_name1.count("v") + lower_case_name2.count("v")
e_count = lower_case_name1.count("e") + lower_case_name2.count("e")
love_count = str(l_count + o_count + v_count + e_count)

true_love = true_count + love_count
love_score = int(true_love)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
