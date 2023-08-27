class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        arr = []

        if(num % 3 == 0):
            arr.append((num/3 -1))
            arr.append(num/3)
            arr.append(num/3+1)


        print(arr)

        return arr