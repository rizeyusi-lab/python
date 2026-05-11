A = [int(input()) for _ in range(5)]
B = A[:]
C = A[::-1]

print(C)

for _ in range(3):
    B.append(int(input()))
print(B)

print(A)