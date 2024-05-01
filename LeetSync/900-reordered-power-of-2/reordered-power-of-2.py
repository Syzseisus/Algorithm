from collections import defaultdict as ddict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = ddict(list)
        power = 1
        while power <= 1000000000:
            power_str = ''.join(sorted(str(power)))
            powers[len(power_str)].append(power_str)
            power *= 2

        for k, v in powers.items():
            powers[k] = set(v)

        n = ''.join(sorted(str(n)))
        n_digit = len(n)
        return n in powers[n_digit]
        