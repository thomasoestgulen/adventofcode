from pathlib import Path

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input_path = Path(r"C:\Users\thooes\OneDrive - Norconsult Group\Documents\_GITHUB\adventofcode_input\2024\input_day04.txt")
    input = read_input(input_path)

    a = [list(row.strip()) for row in input]

    terms = []
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i <= len(a) - 4:                                                                   # |
                terms.append("".join([a[i][j],a[i+1][j],a[i+2][j],a[i+3][j]]))              
            if j <= len(a) - 4:                                                                   # -
                terms.append("".join([a[i][j],a[i][j+1],a[i][j+2],a[i][j+3]]))              
                if i >= 3:                                                                          # /
                    terms.append("".join([a[i][j],a[i-1][j+1],a[i-2][j+2],a[i-3][j+3]]))    
            if j >= 3 and i >= 3:                                                                   # \
                terms.append("".join([a[i][j],a[i-1][j-1],a[i-2][j-2],a[i-3][j-3]]))        

    tot = 0
    tot += terms.count("XMAS")
    tot += terms.count("SAMX")

    print(f'Antall ganger XMAS finnes i matrisen: {tot}')