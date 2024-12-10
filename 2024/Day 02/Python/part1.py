
def open_input(filepath: str):
    with open(filepath, 'r') as f:
        return f.readlines()
    

def parse_input(input: str) -> list:
    output = []
    for line in input:
        output.append([int(num.strip()) for num in line.split()])
    return output

def saftey_check(input: list) -> bool:
    diffs = [input[i + 1] - input[i] for i in range(len(input) - 1)]
    if (all(x < 0 and x in range(-3, 0) for x in diffs)) or \
        (all(x > 0 and x in range(1, 4) for x in diffs)):
        return True
    else:
        return False

# x for i in range(len(input))


if __name__ == "__main__":
    input = open_input("2024\Day 02\input.txt")
    data = parse_input(input)

    total = 0
    for line in data:
        if saftey_check(line):
            total += 1

    print(total)

