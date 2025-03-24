class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if k == 10:
            base = str(n)
        else:
            base = ''
            while n:
                n, res = divmod(n, k)
                base = str(res) + base
            print(base)
        return sum(int(i) for i in base)