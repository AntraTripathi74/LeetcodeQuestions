class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash={}
        l=len(nums)
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        new=list(hash.keys())
        for i in range(len(hash)):
            nums[i]=new[i]
        return len(hash)

        




        