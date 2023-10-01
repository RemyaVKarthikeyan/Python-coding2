import random
lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)

fortune_text = ''
if fortune_number == 1:
    fortune_text = "You will have a great day"
if fortune_number == 2:
    fortune_text = "Keep calm, everything will be alright"
if fortune_number == 3:
    fortune_text = " You are going to be lucky"
print(f'{fortune_text}! Your lucky number is :{lucky_number}')