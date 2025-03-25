# solution...

from collections import defaultdict as ddict

class Solution:
    def get_count(self, s: str, idx: int) -> str:
        count = ""
        while idx < len(s) and s[idx].isdigit():
            count += s[idx]
            idx += 1

        count = int(count) if count else 1
        return count, idx

    def countOfAtoms(self, formula: str) -> str:
        index = 0
        stack = [ddict(int)]

        while index < len(formula):
            s = formula[index]
            if s == "(":
                stack.append(ddict(int))
                index += 1
            elif s == ")":
                count, index = self.get_count(formula, index + 1)
                curr_tmp = stack.pop()
                curr_tmp = {k: v * count for k, v in curr_tmp.items()}
                prev_tmp = stack[-1]
                for k, v in curr_tmp.items():
                    prev_tmp[k] += v
            elif s.isupper():
                index += 1
                atom = s
                while index < len(formula) and formula[index].islower():
                    atom += formula[index]
                    index += 1
                
                count, index = self.get_count(formula, index)
                prev_tmp = stack[-1]
                prev_tmp[atom] += count

        sorted_tmp = sorted([f"{atom}" if count == 1 else f"{atom}{count}" for atom, count in stack[-1].items()])
        return "".join(sorted_tmp)


# solution...

from collections import Counter

class Solution:
    def get_count(self, s: str, idx: int) -> str:
        count = ""
        while idx < len(s) and s[idx].isdigit():
            count += s[idx]
            idx += 1

        count = int(count) if count else 1
        return count, idx

    def countOfAtoms(self, formula: str) -> str:
        index = 0
        stack = [Counter()]

        while index < len(formula):
            s = formula[index]
            if s == "(":
                stack.append(Counter())
                index += 1
            elif s == ")":
                count, index = self.get_count(formula, index + 1)
                curr_tmp = stack.pop()
                curr_tmp = Counter({k: v * count for k, v in curr_tmp.items()})
                prev_tmp = stack[-1]
                stack[-1] = curr_tmp + prev_tmp
            elif s.isupper():
                index += 1
                atom = s
                while index < len(formula) and formula[index].islower():
                    atom += formula[index]
                    index += 1
                
                count, index = self.get_count(formula, index)
                prev_tmp = stack[-1]
                prev_tmp[atom] += count

        sorted_tmp = sorted([f"{atom}" if count == 1 else f"{atom}{count}" for atom, count in stack[-1].items()])
        return "".join(sorted_tmp)