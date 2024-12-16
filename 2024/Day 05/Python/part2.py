from pathlib import Path

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as f:
        return f.read().split("\n")


def check_order(pageset, rules):
    while len(pageset) > 0:
        x = pageset.pop(-1)

        if len([y for y in pageset if y in rules[x]]) > 0:
            return False
    return True
    

if __name__ == "__main__":
    input_path1 = Path(r"C:\Users\thooes\OneDrive - Norconsult Group\Documents\_GITHUB\adventofcode_input\2024\input_day05_part1.txt")
    input_path2 = Path(r"C:\Users\thooes\OneDrive - Norconsult Group\Documents\_GITHUB\adventofcode_input\2024\input_day05_part2.txt")
    ordering_rules_input = read_input(input_path1)
    updates_input = read_input(input_path2)

    ordering_rules = [r.split('|') for r in ordering_rules_input]
    updates = [u.split(',') for u in updates_input]

    order = {}
    for rule in ordering_rules:
        page_rule = int(rule[0])
        page_after = int(rule[1])
        order.setdefault(page_rule, []).append(page_after)
    
    # print(order[35])
    # check = 46 in order[35]
    # print(f'Skal 35 være før side 46: {check}')

    tot = 0
    skipped = []
    for update in updates:
        pageset = list(map(int, update))
        if check_order(pageset[:], order):
            tot += pageset[len(pageset) // 2]
        else:
            skipped.append(update)
            

    print(skipped) 




