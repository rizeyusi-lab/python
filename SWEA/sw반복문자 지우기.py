T = int(input())

for t in range(1, T + 1):

    s = input().strip()
    stack = []

    for char in s:

        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char) 
            
    print(f"#{t} {len(stack)}")