def get_values_from_file(file_url: str) -> tuple:
    left_values = []
    right_values = []

    with open(file_url, 'r') as file:
        for line in file:
            num1, num2 = line.strip().split()
            left_values.append(int(num1))
            right_values.append(int(num2))
    return sorted(left_values), sorted(right_values)

def get_distance_values(sorted_values: tuple) -> list:
    result = [abs(num1 - num2) for num1, num2 in zip(*sorted_values)]
    return result

def get_similarity_values(sorted_values: tuple) -> list:
    left_values, right_values = sorted_values
    result = [num * right_values.count(num) for num in left_values]
    return result


if __name__ == '__main__':
    # Part one
    PUZZLE_INPUT_URL = 'src/files/puzzle-input.txt'

    values = get_values_from_file(PUZZLE_INPUT_URL)
    distance_values = get_distance_values(values)
    total_distance = sum(distance_values)
    print(total_distance) # Part one result => 1197984

    # Part two
    similarity_values = get_similarity_values(values)
    similarity_score = sum(similarity_values)
    print(similarity_score) # Part two result => 23387399