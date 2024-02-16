# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = defaultdict(int)
#         for n in nums:
#             counter[n] += 1
#         count = sorted(counter.values(), reverse=True)[:k]
        
#         answer = []
#         i = 0
#         while i < k:
#             for key in counter:
#                 if counter[key] == count[i]:
#                     answer.append(key)
#                     del(counter[key])
#                     break
#             i += 1
                    
#         return answer


# # 위 코드 단점: 계속해서 dictionary 전체 탐색을 해야됨
# # 해결: 우선 순위 큐
# import heapq
# class Solution:
#     def topKFrequent(self, nums, k):
#         counter = defaultdict(int)
#         for n in nums:
#             counter[n] += 1
        
#         hq = []
#         for key in counter:
#             heapq.heappush(hq, (-counter[key],key))
        
        
#         answer = []        
#         for i in range(k):
#             answer.append(heapq.heappop(hq)[1])
            
#         return answer
    

# 해결: dictionary sort
class Solution:
    def topKFrequent(self, nums, k):
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]
        answer = [k for k, v in sorted_counter]
        
        return answer