
seed = "4610211 4 0 59 3907 201586 929 33750"
test_seed = "125 17"

start_seed = seed.split()

def rules(num: int):
    s = str(num)
    l = len(s)

    if s == "0":
        return 1
    elif l % 2 == 0:
        return [int(s[0:l//2]), int(s[l//2:l])]
    else: 
        return num * 2024

if __name__ == "__main__":
    res_list = start_seed
    blinks = 25
    i = 0
    while i < blinks:
        temp = []
        for num in res_list:
            x = rules(int(num))
            if isinstance(x, list):
                temp.extend(x)
            else:
                temp.append(x)

        res_list = temp
        i += 1
    print(f'Antall steiner etter {blinks} blunk: {len(res_list)}')

