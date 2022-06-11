def calc():
    result = 0
    while True:
        x = (yield result)
        str = list(x.split())
        num1 = int(str[0])
        num2 = int(str[2])
        oper = str[1]
        
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        else:
            result = num1 / num2

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()