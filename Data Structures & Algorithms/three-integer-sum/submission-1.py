class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        rezultat = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            suma = 0

            while left < right:
                suma = nums[i] + nums[left] + nums[right]
                if suma < 0:
                    left += 1
                elif suma > 0:
                    right -= 1
                else: 
                    rezultat.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return rezultat