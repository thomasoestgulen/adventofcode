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

def similarity(a, b):
    tot = 0
    for num in a:
        tot += num * b.count(num)
    return tot

if __name__ == "__main__":
    input = open_input("../input.txt")
    a, b = parse_input(input)

    a.sort()
    b.sort()

    total = similarity(a, b)

    print(total)