def abc(num : int):
    abcd = str(num)[::-1]
    sum = 0
    for i in abcd:
        sum += int(i)
    return sum
inputnum = input()
result = abc(inputnum)
print(result)
