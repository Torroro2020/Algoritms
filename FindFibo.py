def findFibo(x):
    Even_numbers = [0]
    listNumbers = [0, 1]
    i = 0
    while True:
        if len(Even_numbers) == x:
            return Even_numbers
            break
        else:
            a = listNumbers[i] + listNumbers[i + 1]
            if a % 2 == 0:
                Even_numbers.append(a)
                listNumbers.append(a)
            else:
                listNumbers.append(a)
        i += 1


x = int(input('Enter an integer: '))

result = findFibo(x)

print(*result)
