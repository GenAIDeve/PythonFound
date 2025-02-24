"""
This problem sovles project euler problem 1
"""
result = 0
limit = 10
index = 1
while index < limit:
    if index % 3 == 0 or index % 5 == 0:
        result += index
    index += 1

print(result)