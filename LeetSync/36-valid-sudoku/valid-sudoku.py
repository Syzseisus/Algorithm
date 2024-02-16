# # 기본 골자: set으로 만들었을 때 len이 줄어드느냐
# # 무지성 for 문 사용
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             row = board[i]
#             row = [r for r in row if r != "."]
#             if len(row) != len(set(row)):
#                 return False
            
#             col = []
#             for j in range(9):
#                 row = board[j]
#                 v = row[i]
#                 col.append(v)
#             col = [c for c in col if c != "."]
#             if len(col) != len(set(col)):
#                 return False
        
#         for r in range(0, 9, 3):
#             rows = board[r:r+3]
#             for c in range(0, 9, 3):
#                 box = []
#                 for row in rows:
#                     for v in row[c:c+3]:
#                         if v != ".":
#                             box.append(v)
#                 if len(box) != len(set(box)):
#                     return False
                
#         return True

# # 기본 골자: set으로 만들었을 때 len이 줄어드느냐
# # numpy array 사용 - 개 오래 걸림
# from numpy import array
# class Solution:
#     def isValidSudoku(self, board):
#         board = array(board)
#         for i in range(9):
#             # row
#             row = board[i, :]
#             row = [r for r in row if r != "."]
#             if len(row) != len(set(row)):
#                 return False
            
#             # col
#             col = board[:, i]
#             col = [c for c in col if c != "."]
#             if len(col) != len(set(col)):
#                 return False
            
#         for r in range(0, 9, 3):
#             for c in range(0, 9, 3):
#                 box = board[r:r+3, c:c+3].flatten()
#                 box = [b for b in box if b != "."] 
#                 if len(box) != len(set(box)):
#                     return False
        
#         return True


from collections import defaultdict as dd
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rdd = dd(set)
        cdd = dd(set)
        bdd = dd(set)
        
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                elif v in rdd[r] or v in cdd[c] or v in bdd[(r//3,c//3)]:
                    return False
                else:
                    rdd[r].add(v)
                    cdd[c].add(v)
                    bdd[(r//3, c//3)].add(v)
        return True