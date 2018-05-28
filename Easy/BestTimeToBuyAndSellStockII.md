# 问题分析：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 编程实现：
```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int res=0,n=prices.size(),i;
        for (i=0;i<n-1;i++) 
        {
            if(prices[i]<prices[i+1])
            {
                res=res+prices[i+1]-prices[i];
            }
        }
        return res;
    }
};
```
# 总结体会：
这个题可以无限次买入和卖出，所以从第二天开始，如果当前价格比之前价格高，则把差值加入利润中，若明日价更高的话，今日买入，明日再抛出，遍历完数组即可得到答案。