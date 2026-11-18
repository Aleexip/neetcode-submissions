class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        maxim = 0
        for num in set_list: 
           if (num - 1) not in set_list:
                valid = 1
                
                while (num + valid) in set_list:
                    valid += 1
                    
                if valid > maxim:
                    maxim = valid


        return maxim
                    