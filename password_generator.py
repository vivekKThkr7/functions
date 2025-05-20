def generate_password(length=12, include_numbers=True, include_special=True):
    import random
    import string
    
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += string.punctuation
        
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Generate a 16-character password with numbers and special characters
print(generate_password(16))
