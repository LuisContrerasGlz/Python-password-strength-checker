import getpass
import string

TOTAL_CATEGORIES = 5

def get_password():
    return getpass.getpass('Enter your password: ')

def count_character_types(password):
    # Initialize counts for different character categories
    counts = {
        'lowercase': 0,
        'uppercase': 0,
        'digits': 0,
        'whitespace': 0,
        'special characters': 0,
    }

    # Count lowercase letters
    for char in password:
        if char.islower():
            counts['lowercase'] += 1

    # Count uppercase letters
    for char in password:
        if char.isupper():
            counts['uppercase'] += 1

    # Count digits
    for char in password:
        if char.isdigit():
            counts['digits'] += 1

    # Count whitespace characters
    for char in password:
        if char.isspace():
            counts['whitespace'] += 1

    # Count special characters
    for char in password:
        if char in string.punctuation:
            counts['special characters'] += 1

    return counts


def calculate_strength_score(counts):
    strength = sum(count > 0 for count in counts.values())
    return strength / TOTAL_CATEGORIES

def display_results(counts, strength_score, remarks):
    print('Your password contains:')
    for category, count in counts.items():
        print(f'{count} {category} characters')
    print(f'Password Strength: {strength_score:.2%}')
    print(f'Remarks: {remarks}')

def check_password_strength(password):
    counts = count_character_types(password)

    strength_score = calculate_strength_score(counts)

    if strength_score == 0:
        remarks = 'Please enter a password.'
    elif strength_score == 1:
        remarks = 'This is a very weak password. Consider changing it.'
    elif strength_score == 0.2:
        remarks = 'Your password is weak. Strengthen it for better security.'
    elif strength_score == 0.4:
        remarks = 'The password is moderate, but there is room for improvement.'
    elif strength_score == 0.6:
        remarks = 'Your password is strong, but you can make it even more secure.'
    else:
        remarks = 'Congratulations! Your password is exceptionally strong. Hackers will struggle to guess it!'

    display_results(counts, strength_score, remarks)

if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')

    while True:
        password = get_password()
        check_password_strength(password)

        choice = input('Do you want to check another password\'s strength (yes/no): ')
        if choice.lower() != 'yes':
            print('Exiting...')
            break
