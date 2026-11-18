class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        prefix = 1
        for i in range (length):
            left[i] = prefix
            prefix *= nums[i]

        right = [1] * length
        suffix = 1
        for i in range (length-1, -1, -1):
            right[i] = suffix
            suffix *= nums[i]
        output = [1] * length
        for i in range (length):
            output[i] = right[i] * left[i]
        return output