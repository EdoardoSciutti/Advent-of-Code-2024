import os
import re

def main():
    print("Sciutti's solution to the first problem")
    findValidMuls()

def findValidMuls():
    pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')
    pattern_do = re.compile(r'do\(\)')
    pattern_dont = re.compile(r"don't\(\)")
    total = 0
    enabled = True
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
        content = file.read()

        pos = 0
        while pos < len(content):
            match_mul = pattern_mul.search(content, pos)
            match_do = pattern_do.search(content, pos)
            match_dont = pattern_dont.search(content, pos)

            next_match = min(
                [m for m in [match_mul, match_do, match_dont] if m],
                key=lambda m: m.start(),
                default=None
            )

            if not next_match:
                break

            pos = next_match.end()

            if next_match == match_mul:
                if enabled:
                    num1, num2 = int(match_mul.group(1)), int(match_mul.group(2))
                    total += num1 * num2
            elif next_match == match_do:
                enabled = True
            elif next_match == match_dont:
                enabled = False

    print(f"Totale: {total}")

main()
