'''
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = {0: homepage}
        self.curr_pg = 0
        self.max_num = 0

    def visit(self, url: str) -> None:
        # print("current page:", self.curr_pg)
        # print("current state:", self.history)
        self.curr_pg += 1
        self.max_num = self.curr_pg
        self.history[self.curr_pg] = url
        # print("updated page:", self.curr_pg)
        # print("updated state:", self.history)
        # print()

    def back(self, steps: int) -> str:
        # print("current page:", self.curr_pg)
        # print("current state:", self.history)
        self.curr_pg -= steps
        if self.curr_pg < 0:
            self.curr_pg = 0
        # print("updated page:", self.curr_pg)
        # print("updated state:", self.history)
        # print()
        return self.history[self.curr_pg]

    def forward(self, steps: int) -> str:
        # print("current page:", self.curr_pg)
        # print("current state:", self.history)
        next_pg = self.curr_pg + steps
        if next_pg <= self.max_num:
            self.curr_pg = next_pg
        else:
            self.curr_pg = self.max_num
        # print("updated page:", self.curr_pg)
        # print("updated state:", self.history)
        # print()
        return self.history[self.curr_pg]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)