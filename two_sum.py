class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
    def twoSum_hash(self,nums,target):
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in dict and dict[complement]!=i:
                return [i,dict[complement]]

                


a=Solution()
print(a.twoSum([2,7,11,15],18))


print(a.twoSum_hash([2,7,11,15],18))
