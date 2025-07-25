import random
import string

def generate_password():
    
    length=int(input("enter the lenth of the password: "))
    include_specialcharacters=input("do you need to include special characters in your password? (yes/no) ")
    include_uppercase=input("do you need to include uppercase characters in your password? (yes/no) ")
    include_digits=input("do you need to include digits in your password? (yes/no) ")
    
    if length<4:
        print("password length cannot be less than 4")
        return
    
    lower=string.ascii_lowercase
    uppercase=string.ascii_uppercase if include_uppercase=="yes" else ""
    special_character=string.punctuation if include_specialcharacters=="yes" else ""
    digits=string.digits if include_digits=="yes" else ""
    all_character=lower+uppercase+special_character+digits
    
    add_characters=[]
    
    if include_specialcharacters=="yes":
        add_characters.append(random.choice(special_character))
    if include_uppercase=="yes":
        add_characters.append(random.choice(uppercase))
    if include_digits=="yes":
        add_characters.append(random.choice(digits))
    
    password=add_characters
    remaining_length=length-len(add_characters)
    
    for _ in range(remaining_length):
        character=random.choice(all_character)
        password.append(character)
    random.shuffle(password)
    str_password=''.join(password)
    return str_password

password=generate_password()
print(password)
    