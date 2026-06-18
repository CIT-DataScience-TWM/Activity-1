class Solution(object):
    def plusOne(self, digits):
        a=len(digits)
        b=''
        c=[]
        for i in digits:
            b+=str(i)
        b=str(int(b)+1)
        for j in b:
            c.append(int(j))
        digits[:]=c
        return digits
