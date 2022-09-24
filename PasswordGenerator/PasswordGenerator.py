from string import ascii_lowercase, ascii_uppercase
from random import randint, sample

class PasswordGenerator():
    def __init__(self):
        self.special_chars = "!#$%&"
        self.digits = "0123456789"
        self.letters_lowercase = list(ascii_lowercase)
        self.letters_uppercase = list(ascii_uppercase)
        self.numbers = list("0123456789")

    def make_password(self, num):
        #Make no of characters divisible by 4
        num = num if num % 4 == 0 else num+(4 - num%4)
        print(num)

        # Generate number of repetition for each category  
        repeater = int(num/4)

        random_special_char = self.special_chars[randint(0,4)]*repeater
        random_lowercase = self.letters_lowercase[randint(0,25)]*repeater
        random_uppercase = self.letters_uppercase[randint(0,25)]*repeater
        random_numbers = self.numbers[randint(0,9)]*repeater

        base_password = list(random_special_char+random_lowercase+random_uppercase+random_numbers)
        password_generated = sample(base_password, k=num)

        return "".join(password_generated)
        
    
    def __str__(self):
        return "Created PassWordGenerator"