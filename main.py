#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator")
c_l=int(input("Enter how many letters you want add\t"))
c_n=int(input("Enter how many numbers you want add\t"))
c_s=int(input("Enter how many symbols you want add\t"))

password=[]

for char in range(1,c_l+1):
  random_l=random.choice(letters)
  password.append(random_l)

for num in range(1,c_n+1):
  random_n=random.choice(numbers)
  password.append(random_n)

for sym in range(1,c_s+1):
  random_s=random.choice(symbols)
  password.append(random_s)

print(password)
random.shuffle(password)
print(password)

password1= ""
for char in password:
  password1+=char

print(password1)





#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P