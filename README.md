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

#### 2. P43238. 입국심사
<details>
    <summary>Details</summary>
    <div markdonw="1">
        https://programmers.co.kr/learn/courses/30/lessons/43238#</br>
    <code>n</code>명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는 데 걸리는 시간은 다릅니다.</br>
    처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.</br>
    모든 사람이 심사를 받는 데 걸리는 시간을 최소로 하고 싶습니다.</br>
    입국심사를 기다리는 사람 수 <code>n</code>, 각 심사관이 한 명을 심사하는 데 걸리는 시간이 담긴 배열 <code>times</code>가 매개변수로 주어질 때, 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값을 <code>return</code>하도록 <code>solution</code> 함수를 작성해주세요.</br>
    </br>
    
**제한사항**  
* 입국심사를 기다리는 사람은 <code>1</code>명 이상 <code>1,000,000,000</code>명 이하입니다.
* 각 심사관이 한 명을 심사하는 데 걸리는 시간은 <code>1</code>분 이상 <code>1,000,000,000</code>분 이하입니다.
* 심사관은 <code>1</code>명 이상 <code>100,000</code>명 이하입니다.
</br>    
    
**입출력 예**
<table>
    <tr>
        <thead>
            <td>n</td>
            <td>times</td>
            <td>return</td>
        </thead>
    </tr>
    <tr>
        <tbody>
            <td>6</td>
            <td>[7, 10]</td>
            <td>28</td>
        </tbody>
    </tr>
</table>
</br>

<p><b>입출력 예 설명</b></p>
<p>가장 첫 두 사람은 바로 심사를 받으러 갑니다.</br>
7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.</br>
10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.</br>
14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.</br>
20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.</p>

[출처](http://hsin.hr/coci/archive/2012_2013/contest3_tasks.pdf)
    </div></details>
