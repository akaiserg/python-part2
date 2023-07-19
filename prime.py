for n in range(2,100):
    for value in range(2,n):
        if n % value == 0:
            print(f"{n} equals to  {value} * {n//value}")
            break
        
    else:
        print(f"{n} is a prime number.")