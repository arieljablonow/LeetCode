class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        ret_arr =[]
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                ret_arr.append(str("FizzBuzz"))
            elif(i%3==0):
                ret_arr.append(str("Fizz"))
            elif(i%5==0):
                ret_arr.append(str("Buzz"))
            else:
                ret_arr.append(str(i))

        return ret_arr