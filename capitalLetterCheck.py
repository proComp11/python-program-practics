#How would you check if each word in a string begins with a capital letter
str1 = 'Pralay Mondal'
str2 = 'pralay mondal'
flag = 0
for s in str1:
    if s.istitle():
        print(str1+ ' is a string start with uppercase')
        flag = 1
        break
if flag == 0:
    print(str2+ ' is a string that does\'t start with uppercase')
    
if str2.istitle():
    print(str2 + ' start with uppercase letter')
else:
    print(str2 + ' does\'t start with uppercase')
