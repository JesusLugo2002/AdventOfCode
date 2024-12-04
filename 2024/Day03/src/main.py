import re

PUZZLE_INPUT_URL = './files/puzzle-input.txt'

def get_file_content(file_url: str) -> str:
    result = ''
    with open(PUZZLE_INPUT_URL, 'r') as file:
        for line in file:
            result += line.strip()
    return result

def get_valid_parts(text: str) -> list[str]:
    PATTERN = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(PATTERN, text)

def multiply_parts(parts: list[str]) -> int:
    result = 0
    for part in parts:
        values = re.search(r'(\d{1,3}),(\d{1,3})', part)
        result += int(values[1]) * int(values[2])
    return result

def get_valid_instructions(text: str) -> list:
    return re.findall(r'(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)', text)

if __name__ == '__main__':
    # Part One
    text = get_file_content(PUZZLE_INPUT_URL)
    valid_parts = get_valid_parts(text)
    mul_result = multiply_parts(valid_parts)
    print(mul_result) # Result => 175015740

    # Part Two
    text = ''.join(get_valid_instructions(text))
    mul_result = multiply_parts(get_valid_parts(text))
    print(mul_result) # Result => 112272912
