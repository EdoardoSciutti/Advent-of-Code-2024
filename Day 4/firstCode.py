import os

def main():
    print("Sciutti's solution to the first problem:")
    find_xmas_occurrences()

def find_xmas_occurrences():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    result = count_xmas(grid)
    print(f"XMAS appears {result} times")

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    count += 1
    
    return count

main()