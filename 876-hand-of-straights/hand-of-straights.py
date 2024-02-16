from collections import defaultdict as ddict

class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        cnt = 0
        remain = ddict(lambda: 0)
        for card in hand:
            remain[card] += 1
            cnt += 1
            if cnt == gs:
                cnt = 0

        if cnt:
            return False

        hand.sort()
        for card in hand:
            if not remain[card]:
                continue

            for i in range(gs):
                if not remain[card + i]:
                    return False
                
                remain[card + i] -= 1

        return True