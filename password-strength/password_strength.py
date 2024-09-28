import math

'''
NOTE

https://nordvpn.com/blog/what-is-password-entropy/

https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords

'''


def pass_entropy(password):
    special_chars = "!@#$%^&*()-+?_=,<>/"
    special_chars_set = set(special_chars)

    length = len(password)
    charset_size = 0

    for char in password:
        if char.islower():
            charset_size += 26
        elif char.isupper():
            charset_size += 26
        elif char.isdigit():
            charset_size += 10
        elif char in special_chars_set:
            charset_size += 19

    
    return math.log2(charset_size) * length

def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        # Read all lines, strip any whitespace, and convert to a set
        common_passwords = set(line.strip() for line in file if line.strip())
    return common_passwords



def pass_strength(password):
    file_path = 'common_passwords.txt' 
    common_passwords_set = load_common_passwords(file_path)

    if password in common_passwords_set:
        print("Your password has been exposed, please choose a new one!")
    else:
        entropy = pass_entropy(password)
        if entropy <= 35:
            print(entropy, "This password is very weak, please use more distinguishing characters.")
        elif entropy <= 59:
            print(entropy, "This password is weak, please use more distinguishing characters.")
        elif entropy <= 119:
            print(entropy, "This password is relatively strong, but it could be stronger.")
        elif entropy > 120:
            print(entropy, "This is a strong password, good job!")


pass_strength('b9_Vdt^%6SsXT5E3')

        