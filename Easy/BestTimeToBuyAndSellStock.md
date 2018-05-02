# 问题分析：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
# 编程实现：
```C++
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int m=prices.size(),i;
        if(m==0)
            return 0;            
        int curMin=prices[0];
        int ret=0;
        for(i=1;i<m;i++)
        {
            curMin=min(curMin, prices[i]);
            ret=max(ret,prices[i]-curMin);
        }
        return ret;
    }
};
```
# 总结体会：
题目需要遍历一次数组，寻找遍历过的数的最小值，然后每次计算当前值和这个最小值之间的差值最为利润，选择较大的利润来更新。遍历完成后当前利润即为所求，