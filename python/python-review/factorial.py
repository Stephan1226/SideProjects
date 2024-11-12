n = int(input('정수입력'))
result = 1
for item in range(1, n):
    result += result*item
print(result)