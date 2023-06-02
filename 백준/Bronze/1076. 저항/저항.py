
result = ''


data = {'black' : '0', 'brown' : '1', 'red' : '2', 
        'orange' : '3', 'yellow' : '4', 'green' : '5',
        'blue' : '6', 'violet' : '7', 'grey' : '8', 'white' : '9'}


for i in range(3):
    a = input()
    if i <= 1:
        if i == 0:
            if a == 'black':
                continue
        result += data[a]
    if i == 2 and result != '':
        result = int(result)
        if a == 'black':
            result = result * 1
        elif a == 'brown':
            result = result * 10
        elif a == 'red':
            result = result * 100
        elif a == 'orange':
            result = result * 1000
        elif a == 'yellow':
            result = result * 10000
        elif a == 'green':
            result = result * 100000
        elif a == 'blue':
            result = result * 1000000
        elif a == 'violet':
            result = result * 10000000
        elif a == 'grey':
            result = result * 100000000
        else:
            result = result * 1000000000
    if i == 2 and result == '':
        print(0)
        exit()

print(result)