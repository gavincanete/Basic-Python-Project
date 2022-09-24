from string import ascii_lowercase, ascii_uppercase
from random import randint, sample

num = int(input("Input # of characters: "))

special_chars = "!#$%&"
digits = "0123456789"
letters_lowercase = list(ascii_lowercase)
letters_uppercase = list(ascii_uppercase)
numbers = list("0123456789")

#Make no of characters divisible by 4
num = num if num % 4 == 0 else num+(4 - num%4)
print(num)

# Generate number of repetition for each category  
repeater = int(num/4)

random_special_char = special_chars[randint(0,4)]*repeater
random_lowercase = letters_lowercase[randint(0,25)]*repeater
random_uppercase = letters_uppercase[randint(0,25)]*repeater
random_numbers = numbers[randint(0,9)]*repeater

base_password = list(random_special_char+random_lowercase+random_uppercase+random_numbers)
password_generated = sample(base_password, k=num)

print("".join(password_generated))