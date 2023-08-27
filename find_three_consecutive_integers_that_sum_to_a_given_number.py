class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        ret = []

        if(num % 3 == 0):
            ret.append((num/3 -1))
            ret.append(num/3)
            ret.append(num/3+1)


        return ret

