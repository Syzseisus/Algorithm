'''
[1,4], 2
-> 1:
    -1 < 1 => [1, 3], 2
-> 4:
    3 < 4 => [4, 6], 4
return 4

[1,2], 2
-> 1:
    [1, 3], 2
-> 2:
    3 > 2 => [1, 4], 3
return 3
'''

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        before_s = -1
        before_e = -1
        before_p = 0
        for attack in timeSeries:
            print(before_s, before_e, attack)
            if attack > before_e:
                answer += duration
                before_s = attack
                before_p = duration
                print("A", answer)
            else:
                answer -= before_p
                after_e = attack + duration
                answer += (after_e - before_s)
                before_p = (after_e - before_s)
                print("B", answer)
            before_e = attack + duration
        
        return answer
                