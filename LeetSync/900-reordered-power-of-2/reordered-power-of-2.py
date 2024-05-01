from collections import defaultdict as ddict
# 전략: 10^9보다 작은 2의 거듭제곱은 몇 개 안 됨
# 따라서 이를 모두 set으로 지정하고, 있는지 없는지를 보려고함

class Solution:
#     def reorderedPowerOf2(self, n: int) -> bool:
#         powers = ddict(list)
#         power = 1
#         while power <= 1000000000:
#             power_str = ''.join(sorted(str(power)))
#             powers[len(power_str)].append(power_str)
#             power *= 2

#         for k, v in powers.items():
#             powers[k] = set(v)

#         n = ''.join(sorted(str(n)))
#         n_digit = len(n)
#         return n in powers[n_digit]
        
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = set()
        power = 1
        while power <= 1000000000:
            power_str = ''.join(sorted(str(power)))
            powers.add(power_str)
            power *= 2

        n = ''.join(sorted(str(n)))
        n_digit = len(n)
        return n in powers
        