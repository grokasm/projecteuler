nums = xrange(101)
print sum(nums) ** 2  - sum(map(lambda x: x * x, nums))