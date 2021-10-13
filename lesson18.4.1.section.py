nums = [x for x in range(101) if x % 10 == 0]

nums[:3] = [1, 1, 1]
print(nums)

nums[:3] = [1]
print(nums)
