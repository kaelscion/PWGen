from random import randint

class PWGen():
    def __init__(self, pw_len=25, print_to_console=False):
        self.generate(pw_len, print_to_console)

    def coin_flip(self):
        i = randint(1, 2)
        if i == 2:
            return True
        return False

    def generate(self, pw_len, print_to_console):
        characters = ['a', 'b', 'c', 'd',
                      'e', 'f', 'g', 'h', 
                      'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x',
                      'y', 'z', '0', '1',
                      '2', '3', '4', '5',
                      '6', '7', '8', '9',
                      '!', '@', '#', '$',
                      '%', '^', '&', '*',
                      '(', ')']
        i=1
        temp_pass = []
        try:
            while i <= pw_len:
                char_index = randint(0, len(characters)-1)
                char = characters[char_index]
                if self.coin_flip():
                    char = characters[char_index].upper()
                temp_pass.append(char)
                i+=1
                pw = ''.join(temp_pass)
            if print_to_console:
                print(pw)
            return pw

        except Exception as e:
            print(e, e.message)
