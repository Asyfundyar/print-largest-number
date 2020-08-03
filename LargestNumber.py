nums = (901, 938, 823, 2000, 1, 98301) #This python program will work with this list of numbers.
largest = nums[0] 
for num in nums:
    if num > largest:
        largest = num
print(largest)
