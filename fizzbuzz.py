class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        
        ret =[]
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                ret.append(str("FizzBuzz"))
            elif(i%3==0):
                ret.append(str("Fizz"))
            elif(i%5==0):
                ret.append(str("Buzz"))
            else:
                ret.append(str(i))

        return ret
