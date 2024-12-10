
def open_input(filepath: str):
    with open(filepath, 'r') as f:
        return f.readlines()

def saftey_check(input: list) -> bool:
    diffs = [input[i + 1] - input[i] for i in range(len(input) - 1)]
    if (all(x < 0 and x in range(-3, 0) for x in diffs)) or \
        (all(x > 0 and x in range(1, 4) for x in diffs)):
        return True
    else:
        return False


if __name__ == "__main__":
    input = open_input("2024\Day 02\input.txt")

    total = 0
    for line in input:
        nums = [int(num.strip()) for num in line.split()]
        if saftey_check(nums):
            total += 1
        else:
            for i in range(len(nums)):
                temp_nums = nums.copy()
                temp_nums.pop(i)
                if saftey_check(temp_nums):
                    total += 1 
                    break

    print(total)

