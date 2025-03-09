class Solution:
    def reverse(self, a: int) -> int:
        b=str(a)
        if (a==0):
            return 0

        elif(a>0):
            b=int(b[::-1])
            if(b <= (-2**31)) or (b >= ((2**31) -1)):
                return 0
            return b

        else:
            c=abs(a)
            c=str(c)
            c=c[::-1]
            c= (-1)*int(c)
            if(c <= (-2**31)) or (c >= ((2**31) -1)):
                return 0
            return c

     