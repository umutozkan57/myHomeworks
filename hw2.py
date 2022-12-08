num = int(input("Put a number: "))

while(True):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print(num)
            break

    num += 1
