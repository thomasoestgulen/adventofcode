from pathlib import Path

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as f:
        return f.readlines()


'''
M . M |   S . S |   M . S |   S . M
. A . |   . A . |   . A . |   . A .
S . S |   M . M |   M . S |   S . M
'''


if __name__ == "__main__":
    input_path = Path(r"C:\Users\thooes\OneDrive - Norconsult Group\Documents\_GITHUB\adventofcode_input\2024\input_day04.txt")
    input = read_input(input_path)

    a = [list(row.strip()) for row in input]

    tot = 0
    for i in range(1, len(a)-1):
        for j in range(1, len(a)-1):
            if a[i][j] == "A":  # finn alle A'er
                if ((a[i-1][j-1] == 'M' and a[i-1][j+1] == "M" and a[i+1][j-1] == 'S' and a[i+1][j+1] == "S") or    # alt 1
                    (a[i-1][j-1] == 'S' and a[i-1][j+1] == "S" and a[i+1][j-1] == 'M' and a[i+1][j+1] == "M") or    # alt 2
                    (a[i-1][j-1] == 'M' and a[i-1][j+1] == "S" and a[i+1][j-1] == 'M' and a[i+1][j+1] == "S") or    # alt 3
                    (a[i-1][j-1] == 'S' and a[i-1][j+1] == "M" and a[i+1][j-1] == 'S' and a[i+1][j+1] == "M")):     # alt 4
                    tot += 1

    print(f'Antall ganger XMAS finnes i matrisen: {tot}')