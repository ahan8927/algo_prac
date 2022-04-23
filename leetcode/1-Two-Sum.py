class Solution:
    def twoSum(self, nums, target):
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

a = Solution()
example = {
    "nums": [1,2,3,4,5,6],
    "target": 3
}
print(a.twoSum(example["nums"], example["target"]))