class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        summ = 1
        for i in range(2, floor(num ** 0.5) + 1):
            if num % i:
                continue
            summ += i
            print(i)
            if i != (num //i):
                summ += (num // i)
                print(num // i)
        
        return summ == num