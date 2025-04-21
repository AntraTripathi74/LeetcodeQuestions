class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v=nums.count(val)
        i=0
        while i<v:
            nums.remove(val)
            i+=1
        return len(nums)
            