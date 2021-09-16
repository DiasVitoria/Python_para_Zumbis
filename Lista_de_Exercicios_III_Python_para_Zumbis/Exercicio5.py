n1 = int(input("primeiro número: "))
n2 = int(input("segundo número: "))
mdc = 1
divisor = 2
while divisor <= n1 or divisor <= n2:
    if n1>1 and n2>1 and n1 % divisor == 0 and n2 % divisor ==0:
        print(int(n1),int(n2),'|',divisor)
        n1 = n1/divisor
        n2 = n2/divisor
        mdc = mdc * divisor 
    elif n1>1 and n2>1 and n1 % divisor == 0 or n2 % divisor ==0:
        while divisor <= n1 or divisor <= n2:
            if n1 % divisor == 0:
                print(int(n1),int(n2),'|',divisor)
                n1 = n1/divisor
                mdc = mdc * divisor
            elif n2 % divisor == 0:
                print(int(n1),int(n2),'|',divisor)
                n2 = n2/divisor
                mdc = mdc * divisor
            break
    else:
        divisor += 1
print('1,1')
print('mdc: ',mdc)

