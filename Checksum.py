def twoSum(nums, target) : 
    for i in range(0,len(nums)): 
        for z in range(i+1,len(nums)): 
            if nums[i] + nums[z] == target: return i, z

print (twoSum([2,4,6,8,10,12],10))