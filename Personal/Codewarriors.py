def iq_test(numbers) -> str:
    evens = []
    odds = []
    for no in numbers:
        no = int(no)
        if no % 2 == 0:
            evens.append(int(no))
        else:
            odds.append(int(no))
    if len(evens) == 1:
        return str(numbers.index(evens[0]) + 1)
    else:
        return str(numbers.index(odds[0]) + 1)

print(iq_test([1,1,3,4,5]))
