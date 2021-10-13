nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print(nums[:5])
print(nums[:8])
print([nums[i_elem] for i_elem in range(10) if i_elem % 2 == 0])
print([nums[i_elem] for i_elem in range(10) if i_elem % 2 != 0])
print(nums[::-1])
print(nums[9::-2])
