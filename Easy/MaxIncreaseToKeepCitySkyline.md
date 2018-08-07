# 问题分析：
在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。

最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。

建筑物高度可以增加的最大总和是多少？

# 编程实现：
```C++
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) 
    {
        int m = grid.size(), n = grid[0].size(), res = 0;
        vector<int> row(m, 0), col(n, 0);
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                row[i] = max(row[i], grid[i][j]);
                col[j] = max(col[j], grid[i][j]);
            }
        }
        for (int i = 0; i < m; ++i) 
        {
            for (int j = 0; j < n; ++j)
            {
                res += min(row[i]-grid[i][j],col[j]-grid[i][j]);
            }
        }
        return res;
    }
};
```
# 总结体会：
首先需要求出各行各列的最大值，然后就遍历每个建筑，每个高度都可能影响该行或者该列的天际线，那么该行该列中的较小值应该是该建筑物的极限，如果超过了这个值，原来的天际线就会被破坏，所以极限值和当前的高度之差就是可以增加的高度，我们累计所有建筑的可增加的高度，就是所求的最大增高。