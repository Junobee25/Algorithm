
string = input()

result = ''

flag = True
reverse_str = ''

if '<' and '>' not in string:
    string = string.split(' ')
    for i in range(len(string)):
        print(string[i][::-1],end = " ")
    exit()

for i in range(len(string)):
    if string[i] == '<':
        flag = False
        result += string[i]
    if string[i] == '>':
        flag = True
        result += string[i]
    if flag == False and string[i] != '<' and string[i] != '>':
        result += string[i]
    if flag == True and string[i] != '>' and string[i] != ' ':
        reverse_str += string[i]
    if flag == True and string[i] != '>' and string[i] == ' ':
        result += reverse_str[::-1]
        result += ' '
        reverse_str = ''
    if i == len(string)-1 and flag == True:
        result += reverse_str[::-1]
    if i != len(string)-1 and string[i+1] == '<':
        result += reverse_str[::-1]
        reverse_str = ''
print(result)