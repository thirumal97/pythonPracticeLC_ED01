n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(n, 1, -3):
    print(pie)
    for j in range(n, 0, -1):
        sum += 1

print(sum)


# time complexity, two loops
# inner loop n
# outer loop n/3

# together takes O(n^2)