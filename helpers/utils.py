import random

def generate_random_account(length: int = 10) -> str:
    # Generates a string of random digits
    return "".join(str(random.randint(0, 9)) for _ in range(length))