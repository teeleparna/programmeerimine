
import random
from pathlib import Path


def get_random_value(file_path):
    path = Path(__file__).parent / file_path

    with open(path, "r", encoding="utf-8") as file:
        values = [line.strip() for line in file if line.strip()]

    return random.choice(values)
