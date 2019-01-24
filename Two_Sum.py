class Solution:
    def twoSum(self, nums, target):
        self.target=target
        self.nums=nums
        dic={}
        
        for i in range(len(nums)):
            if (target-nums[i]) in dic.values():
                c=[nums.index(target-nums[i]),i]
                return c
            dic[i]=nums[i]
            i=i+1
