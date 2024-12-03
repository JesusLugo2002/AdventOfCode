import re

PUZZLE_INPUT_URL = './files/demo-input.txt'

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

def separate_instructions(text: str) -> tuple:
    # TODO
    first_section = re.findall(r'(.*)do\(\)|don\'t\(\)', text)
    print(first_section)
    invalid_sections = re.findall(r'don\'t\(\)(.*)(?:do\(\))', text)
    valid_sections = re.findall(r'do\(\)(.*)(?:don\'t\(\))?', text)
    return first_section + valid_sections, invalid_sections

if __name__ == '__main__':
    # Part One
    text = get_file_content(PUZZLE_INPUT_URL)
    valid_parts = get_valid_parts(text)
    mul_result = multiply_parts(valid_parts)
    print(mul_result) # Result => 175015740

    # Part Two
    sections = separate_instructions(text)
