from sys import stdin
import heapq as hq


class dual_priority_queue:
    def __init__(self):
        self.size = 0
        self.visited = [False] * 1000001
        self.deleted = set()
        self.min_hq, self.max_hq = [], []

    def input(self, num, id_):
        hq.heappush(self.min_hq, (int(num), id_))
        hq.heappush(self.max_hq, (-int(num), id_))
        self.visited[id_] = True
        self.size += 1

    def delete_max(self):
        if self.size == 0:
            return
        self.size -= 1
        while self.max_hq and not self.visited[self.max_hq[0][1]]:
            hq.heappop(self.max_hq)
        
        if self.max_hq:
            self.visited[self.max_hq[0][1]] = False
        return hq.heappop(self.max_hq)

    def delete_min(self):
        if self.size == 0:
            return
        self.size -= 1
        while self.min_hq and not self.visited[self.min_hq[0][1]]:
            hq.heappop(self.min_hq)
        
        if self.min_hq:
            self.visited[self.min_hq[0][1]] = False
        return hq.heappop(self.min_hq)

    def peek_max(self):
        while self.max_hq and not self.visited[self.max_hq[0][1]]:
            hq.heappop(self.max_hq)
        return -self.max_hq[0][0]

    def peek_min(self):
        while self.min_hq and not self.visited[self.min_hq[0][1]]:
            hq.heappop(self.min_hq)
        return self.min_hq[0][0]
        

for _ in range(int(stdin.readline())):
    dpque = dual_priority_queue()
    for i in range(int(stdin.readline())):
        op, num = stdin.readline().rstrip().split()
        if op == "I":
            dpque.input(num, i)
        elif num == "1":
            dpque.delete_max()
        elif num == "-1":
            dpque.delete_min()
    
    answer = f"{dpque.peek_max()} {dpque.peek_min()}" if dpque.size else "EMPTY"
    print(answer)
