PUZZLE_INPUT_URL = 'src/files/demo-input.txt'

class Report():
    def __init__(self, levels: list):
        self.levels = [int(level) for level in levels]
    
    def is_safe(self):
        for index in range(len(self.levels[:len(self.levels) - 1])):
            pass # TODO


def get_reports(file_url: str):
    with open(PUZZLE_INPUT_URL, 'r') as file:
        for line in file:
            yield Report(line.strip().split())

if __name__ == '__main__':
    for report in get_reports(PUZZLE_INPUT_URL):
        report.is_safe()