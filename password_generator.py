import random
import string

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

def generate_passwords(num_passwords, password_length):
    passwords = []
    for i in range(num_passwords):
        passwords.append(generate_password(password_length))
    return passwords

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')
    print('Passwords saved to file:', filename)

if __name__ == '__main__':
    num_passwords = 5
    password_length = 8
    passwords = generate_passwords(num_passwords, password_length)
    for password in passwords:
        print('Generated Password:', password)
    save_passwords_to_file(passwords, 'passwords.txt')
