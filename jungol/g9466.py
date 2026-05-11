N = int(input())

def print_square(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
            num += 1
        
        print()

print_square(N)