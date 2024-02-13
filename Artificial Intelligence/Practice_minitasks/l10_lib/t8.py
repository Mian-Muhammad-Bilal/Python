import random
import string


def generate_random_password():
    # Combine letters and digits
    characters = string.ascii_letters + string.digits
    # Generate a random password of length 8 from characters
    password = ''.join(random.choice(characters) for _ in range(8))
    return password


print(f"Generated random password: {generate_random_password()}")
