import heapq as hq


class Solution:
    '''
    i번째 치즈의 실제 reward는 reward1[i] - reward2[i]이다.
    1번쥐가 k개 먹고 2번쥐가 나머지 모두를 먹는 게 조건이다.
    따라서 반대로, 2번쥐가 전체를 먹고, (reward1[i] - reward2[i])이 큰 값,
    즉 1번쥐가 먹는 게 더 이득인 치즈들을 k개 가져오면 된다.
    '''
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward_diff = []
        for i, r1 in enumerate(reward1):
            hq.heappush(reward_diff, (reward2[i]- r1))
        answer = sum(reward2)
        for _ in range(k):
            a = hq.heappop(reward_diff)
            answer -= a
        
        return answer
