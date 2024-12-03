PUZZLE_INPUT_URL = './files/puzzle-input.txt'

class Report():
    def __init__(self, levels: list):
        self.levels = [int(level) for level in levels]

    def __len__(self) -> int:
        return len(self.levels)
    
    @property
    def is_increasing(self) -> bool | None:
        if self.levels[0] == self.levels[1]:
            return None
        return self.levels[0] < self.levels[1]
    
    def is_safe(self) -> bool:
        MIN_RANGE = 1
        MAX_RANGE = 3

        if self.is_increasing == None:
            return False
        for index in range(len(self) - 1):
            if self.is_increasing:
                if self.levels[index] > self.levels[index + 1]:
                    return False
                diff = abs(self.levels[index] - self.levels[index + 1])
                if not MIN_RANGE <= diff <= MAX_RANGE:
                    return False
            else:
                if self.levels[index] < self.levels[index + 1]:
                    return False
                diff = abs(self.levels[index] - self.levels[index + 1])
                if not MIN_RANGE <= diff <= MAX_RANGE:
                    return False
        return True

def get_reports(file_url: str):
    with open(PUZZLE_INPUT_URL, 'r') as file:
        for line in file:
            yield Report(line.strip().split())

def can_fixed(report) -> bool:
    for index in range(len(report.levels)):
        modified_levels = report.levels.copy()
        del modified_levels[index]
        new_report = Report(modified_levels)
        if new_report.is_safe():
            return True
    return False

if __name__ == '__main__':
    # Part One
    safe_reports = [r for r in get_reports(PUZZLE_INPUT_URL) if r.is_safe()]
    print(len(safe_reports)) # Solution => 564

    # Part Two
    unsafe_reports = [r for r in get_reports(PUZZLE_INPUT_URL) if not r.is_safe()]
    fixable_reports = [r for r in unsafe_reports if can_fixed(r)]
    print(len(fixable_reports) + len(safe_reports))