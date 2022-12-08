n = int(input("Number: "))
while 0 in [n%i for i in range(2,n//2+1)]: n+=1
print(n)
