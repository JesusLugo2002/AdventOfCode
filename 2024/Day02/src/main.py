PUZZLE_INPUT_URL = 'src/files/demo-input.txt'

class Report():
    def __init__(self, levels: list):
        self.levels = [int(level) for level in levels]
    
    def __len__(self) -> int:
        return len(self.levels)


def get_reports(file_url: str):
    with open(PUZZLE_INPUT_URL, 'r') as file:
        for line in file:
            yield Report(line.strip().split())

if __name__ == '__main__':
    for report in get_reports(PUZZLE_INPUT_URL):
        report.is_safe()