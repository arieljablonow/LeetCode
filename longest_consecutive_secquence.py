class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        longest = 1

        curr = 1
        length = len(nums)

        if (length == 0): return 0 

        for i in range(0, length-1):
            a = nums[i]+1
            b = nums[i+1]
            
            c = nums[i]
            d = nums[i+1]
            
            if(a == b):
                curr += 1
                print curr
                if (curr>longest):
                    longest = curr

            elif(c == d):
                #do nothing
                continue
            else:
                curr = 1

        return longest