import random
import time
import string


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def generate_random_string(length: int) -> str:
    value = [random.choice(string.ascii_lowercase) for _ in range(length)]
    return "".join(value)