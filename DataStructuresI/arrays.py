# Linear time iterate over all items
arr = [12, 23, 56, 87, 14] # n = 5
for num in arr: # O(n * 1) => O(n)
  print(num) #calling print is O(1) - constant time
# O(n) + O(1) = take the worst time complexity => O(n)

# constant time lookup
print(arr[3]) # O(1)

# quadratic time nested iteration
for x in arr: # O(N)
  for y in arr: # O(N) => O(n^2)
    print(x, y) # O(1) => O(1 * n^2)
# O(n^2) + O(n) + O(1 * n^2)
# O(2n^2) + O(n)
# O(n^2) + O(n)
# O(n^2)

# can we do better?

