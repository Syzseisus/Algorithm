class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        max_length = max(map(len, words))  # output 리스트 길이가 됨
        words = [f"{s:<{max_length}}" for s in words]
        # answer의 i번째 string은
        # 각 word의 i번째 character를 모두 합친 것
        answer = ["".join(w[i] for w in words).rstrip() for i in range(max_length)]
        return answer
