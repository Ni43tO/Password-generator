
# Basic passwords generation tools using the data provides as a input by user .


from itertools import permutations 

# Selecting length for password

min_length = 6 
max_length = 25

# Taking Inputs

first_names = []

first_name = input ("Enter first name : ")
while len(first_name) > 10 or not first_name.replace(" ","").isalpha(): # Taking only strings whose length is less than 10 as a first name

    first_name = input ("Enter first name (Only text): ")

first_name = first_name.lower()    
first_name_capital = first_name.capitalize() 
first_names.extend([first_name , first_name_capital])

last_name = input ("Enter last name : ")
while len(last_name) > 10 or not last_name.replace(" ","").isalpha():
    last_name = input ("Enter last name (Only text): ")
    

yearof_birth = (input("Enter year of birth;eg 2001 : "))
while len(yearof_birth) != 4 or not yearof_birth.isdigit() :
    print("Enter the correct yearof Birth ; eg 2000 or 2001")
    yearof_birth = input("Enter year of birth;eg 2001 : ")

dateof_birth = input ("Enter date of birth (eg : 0101 )") 
while len(dateof_birth) != 4 or not dateof_birth.isdigit():
   dateof_birth = input("Enter the correct date of birth (eg : 0101 )")
   

phone_num = (input("Enter few digits of ph number;eg first four or last four : "))
while len(phone_num) != 4 or not phone_num.isdigit():
    print("Enter only first four or last four digits from phone number")
    phone_num = input("Enter few digits of ph number;eg first four or last four : ")


# Define the symbols used in password generation 
# You can add or remove symbols according to your need

symbols = []
symbol_1 = "@"
symbol_2 = "#"
symbols.extend([symbol_1,symbol_2])

other_text= input("Enter others text or number if there are else skip : ")

passwords = set()

# Creating passwords 

items = [last_name,yearof_birth,dateof_birth,phone_num,other_text]
items.extend (first_names )
items.extend (symbols)
for number in range(2,9):
    for pair in permutations(items,number):
     pw= "".join(pair)
     pw = pw.replace(" ","")
     if len(pw)>=min_length and len(pw)<=max_length :
      if (pw[0] in symbols and pw [1]in symbols) or (first_name in pw and first_name_capital in pw ):
             continue
      passwords.add(pw)

# Adding passwords which we created to a file named Password.txt
file = open("Password.txt", "w")
for password in passwords :
    file.write (password + "\n")

file.close()

length_of_pass = len(passwords)
print (str(length_of_pass) + "passwords have been generated")