PUZZLE_INPUT_URL = './files/puzzle-input.txt'
TARGET_WORD = 'XMAS'

def get_letter_soup(file_url: str) -> list[list[str]]:
    with open(PUZZLE_INPUT_URL, 'r') as file:
        return [list(line.strip()) for line in file]
    
def count_words(letter_soup: list[list[str]], target_word: str) -> int:
    def get_matches(row: int, col: int) -> int:
        def horizontal_check() -> int:
            regular_check = True
            backsward_check = True
            for index, char in enumerate(target_word):
                try:
                    if letter_soup[row][col + index] != char:
                        regular_check = False
                except IndexError:
                    regular_check = False
                try:            
                    if letter_soup[row][col - index] != char or col - index < 0:
                        backsward_check = False
                except IndexError:
                    backsward_check = False
                if not regular_check and not backsward_check:
                    break
            return regular_check + backsward_check

        def vertical_check() -> int:
            top_check = True 
            bottom_check = True
            for index, char in enumerate(target_word):
                try:
                    if letter_soup[row + index][col] != char:
                        bottom_check = False
                except IndexError:
                    bottom_check = False
                try:
                    if letter_soup[row - index][col] != char or row - index < 0:
                        top_check = False
                except IndexError:
                    top_check = False
                if not top_check and not bottom_check:
                    break
            return top_check + bottom_check

        def diagonal_check() -> int:
            top_left_check = True
            top_right_check = True
            bottom_left_check = True
            bottom_right_check = True
            for index, char in enumerate(target_word):
                try:
                    if letter_soup[row - index][col - index] != char or col - index < 0 or row - index < 0:
                        top_left_check = False
                except IndexError:
                    top_left_check = False
                try:
                    if letter_soup[row - index][col + index] != char or row - index < 0:
                        top_right_check = False
                except IndexError:
                    top_right_check = False
                try:
                    if letter_soup[row + index][col - index] != char or col - index < 0:
                        bottom_left_check = False
                except IndexError:
                    bottom_left_check = False
                try:
                    if letter_soup[row + index][col + index] != char:
                        bottom_right_check = False
                except IndexError:
                    bottom_right_check = False
                
            return top_left_check + top_right_check + bottom_left_check + bottom_right_check
        
        return horizontal_check() + vertical_check() + diagonal_check()
    
    result = 0
    for row in range(len(letter_soup)):
        for col in range(len(letter_soup[row])):
            if letter_soup[row][col] == target_word[0]:
                result += get_matches(row, col)
    return result
                


if __name__ == '__main__':
    LETTER_SOUP = get_letter_soup(PUZZLE_INPUT_URL)
    xmas_count = count_words(LETTER_SOUP, TARGET_WORD)
    print(xmas_count) # Solution => 2613

    
