from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcode):
        n = len(barcode)

        cnt = Counter(barcode)
        answer = [0] * n
        sorted_code = []

        max_freq_code = max(cnt, key=cnt.get)
        sorted_code.extend([max_freq_code]*cnt[max_freq_code])
        cnt[max_freq_code] = 0
        for i in cnt.keys():
            sorted_code.extend([i] * cnt[i])

        iter_code = iter(sorted_code)
        for i in range(0,n,2):
            answer[i] = next(iter_code)
        for i in range(1,n,2):
            answer[i] = next(iter_code)

        return answer