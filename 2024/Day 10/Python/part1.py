from pathlib import Path

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as f:
        return f.read()

def parse_input(input: str) -> list:
    output = []
    for line in input:
        output.append(int(line.strip()))
    return output


if __name__ == "__main__":
    input_path = r"C:\Users\thooes\OneDrive - Norconsult Group\Documents\_GITHUB\adventofcode_input\2024\input_day10.txt"
    input = read_input(input_path)
    
    print(input)


    pass