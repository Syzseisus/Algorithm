# Algorithm
Solve algorithm test in Leet or Programmers, in MI Lab

LAB : algorithm study with whole lab people  
URS : algorithm study with Undergraduate Research Students

## Contents

1. LAB  
    1. [Leet222. Maximal Square](#leet222-maximal-square) (22.02.22)
    2. ...
2. URS
    1. [Binary Search](#binary-search) (22.03.04)
    2. ...
---

### Leet222. Maximal Square
<details>
  <summary>Details</summary>
  <div markdown="1">
    <p>https://leetcode.com/problems/maximal-square/</br>
  Given an <code>m x n</code> binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, <i>find the largest square containing only <code>1</code>'s and return its area.</i></br></p>
  </br>

**Example 1:**

![image](https://user-images.githubusercontent.com/76420366/155871990-1e3d2d83-05c1-4adb-a94f-f29661f4347d.png)

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

**Example 2:**

![image](https://user-images.githubusercontent.com/76420366/155872001-65acfd62-6566-4d23-85ba-425dcca9f01c.png)

```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

**Example 3:**

```
Input: matrix = [["0"]]
Output: 0
```

**Constraints**:
* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 300`
* `matrix[i][j] is '0' or '1'.`
  </div></details>
 

---
---
### Binary Search
#### 1. Leet441. Arranging Coins
<details>
    <summary>Details</summary>
    <div markdonw="1">
        <p>https://leetcode.com/problems/arranging-coins/</br>
    You have <code>n</code> coins and you want to build a staiircase with these coins. The staircase consists of <code>k</code> rows where the <code>i<sup>th</sup></code> row has exactly <code>i</code> coins. The last row of the staircase <b>may be</b> incomplete.</p></br>
    Given the integer <code>n</code>, return <i>the number of <b>complete rows</b> of the staircase you will build.</i></br>
    </br>
    
**Example 1:**

![image](https://user-images.githubusercontent.com/83002480/159166058-269c53e8-3456-41d4-b5e0-15c2ca45f394.png)  

```
Input: n = 5
Output: 2
Explanation: Because the 3<sup>rd</sup> row is incomplete,
             we return 2.
```

**Example 2:**

![image](https://user-images.githubusercontent.com/83002480/159166114-1342b593-029d-4d84-b728-82af3a1d779e.png)

```
Input: n = 8
Output: 3
Explanation: Because the 4<sup>th</sup> row is incomplete,
             we return 3.
```

**Constraints:**
- <code>1 <= n <= 2<sup>31</sup> - 1</code>
    </div></details>
