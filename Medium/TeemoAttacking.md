# 问题分析：
在《英雄联盟》的世界中，有一个叫“提莫”的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。

你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
# 编程实现：
```C++
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration)
    {
        if(timeSeries.size()==0)
            return 0;
        int res=0,i;
        for(i=1;i<timeSeries.size();i++)
        {
            if(timeSeries[i]-timeSeries[i-1]>=duration)
                res=res+duration;
            else 
                res=res+timeSeries[i]-timeSeries[i-1];
        }
        return res+duration;
    }
};
```
# 总结体会：
挑了一个Medium难度的题做，发现有个关于小提莫的毒的题目，还真是啥题都有。这个题是Medium中比较简单的一道题，用res来存储艾希中毒的时间，当提莫攻击的两个时间点相隔的时间差小于duration的时候，就累加这个时间差大于duration的时候，就加上duration，要注意的是最后还要加上一个duration，因为最后一次攻击肯定会使艾希中毒duration秒。