import os
import re

def main():
    print("Sciutti's solution to the first problem:")
    findValidMuls()

def findValidMuls():
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    total = 0
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
        content = file.read()
        matches = pattern.findall(content)
        for match in matches:
            num1, num2 = int(match[0]), int(match[1])
            total += num1 * num2
    print(f"Totale: {total}")

main()
