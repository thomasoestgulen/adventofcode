
def open_input(filepath: str):
    with open(filepath, 'r') as f:
        return f.readlines()

def parse_input(input):
    a = []
    b = [] 
    for line in input:
        a.append(int(line.split()[0].strip()))
        b.append(int(line.split()[1].strip()))
    return [a, b]    

def compare(a, b):
    tot = 0
    for i in range(0, len(a)):
        tot += abs(b[i] - a[i])
    return tot

if __name__ == "__main__":
    input = open_input("2024\Day 01\input.txt")
    a, b = parse_input(input)

    a.sort()
    b.sort()

    total = compare(a, b)

    print(total)



