n = 10 
sum = 0
pie = 3.14

for var in range(1, n, 3):
    print(pie)
    for j in range(1, n, 2):
        sum += 1
        print(sum)

# time complexity here is, there are two loops, outer loop and inner loop 
# inner loop takes floor(n/2) and that takes us n 
# outer loop takes floor(n/3) and that takes us n 

# total time complexity is O(n^2)
