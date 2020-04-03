from sys import argv

script, user_name = argv

prompt = "?>>>>>>"

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you few questions..")
print(f"DO you Like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input("?????")

print(f"What KInd of computer do you have ?")
computer = input(prompt)

print(f"""
	alright, So you said {likes} about liking me , 
	You lives in {lives}. Not sure where it is and you have {computer} computer. 
	NIce""")

