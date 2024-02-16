from collections import defaultdict as ddict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_s = [''.join(sorted(s)) for s in strs]
        
        answer = ddict(list)
        for i, s in enumerate(sorted_s):
            answer[s].append(strs[i])
        
        answer = list(answer.values())

        return answer