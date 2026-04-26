import random
small_letters=['a', 'b', 'c',' d', 'e','f', 'g', 'h',' i', 'j', 'k', 'l',' m', 'n',' o', 'p', 'q', 'r','s', 't','u', 'v','w','x',' y', 'z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['@','#','$','%','&','*']

print("welcome to random password generator")
nr_small_letter=int(input("how many small letters would you like in your password?\n"))
nr_capital_letter=int(input("how many Capital letters would you like in your password?\n"))
nr_number=int(input("how many numbers would you like in your password?\n"))
nr_symbol=int(input("how many symbols would you like in your password?\n"))

password_list=[]
for char in range(0,nr_small_letter):
    password_list.append(random.choice(small_letters))
for char in range(0,nr_capital_letter):
    password_list.append(random.choice(capital_letters))
for char in range(0,nr_number):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbol):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char

print(f"your password is {password}")
