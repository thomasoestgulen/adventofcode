import re

def open_input(filepath: str):
    with open(filepath, 'r') as f:
        return f.read()
    

if __name__ == "__main__":
    input = open_input("2024\Day 03\input.txt")

    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    print(sum([int(match[0])*int(match[1]) for match in matches]))