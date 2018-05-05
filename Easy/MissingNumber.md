# 问题分析：
给出一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。


# 编程实现：
```C++
class Solution {
public:
    int missingNumber(vector<int>& nums)
    {
        int sum=0,sum1=0,i;
        for(i=0;i<nums.size();i++)
        {
            sum=sum+i;
            sum1=sum1+nums[i];
        }
        return sum+nums.size()-sum1;
    }
};
```
#总结体会：
求出0到n之间所有的数字之和，然后再遍历数组算出给定数字的和，做减法，差值就是丢失的那个数字。