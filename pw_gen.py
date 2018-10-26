import string
from random import choice

class PWGen():
    def __init__(self, pw_len=25, print_to_console=False):
        self.generate(pw_len, print_to_console)

    def coin_flip(self):
        i = randint(1, 2)
        if i == 2:
            return True
        return False
    
   

    def generate(self, pw_len, print_to_console):
        '''This password generator uses random() to select a random character
        from a list and append it to a temporary password. For added "randomness",
        the coin_flip function is used to randomly decide to capitalize or lowercase a 
        character if that character is a letter'''
        
        temp_pass = []
        all_chars = list(string.ascii_letters +string.punctuation)
        try:
            for i in range(all_chars):
                char = random.choice(all_chars)
                if self.coin_flip():
                    char  = char.upper()
                else:
                    char = char.lower()
                temp_pass.append(char)
                pw = ''.join(temp_pass)
            if print_to_console:
                print(pw)
            return pw

        except Exception as e:
            print(e, e.message)
