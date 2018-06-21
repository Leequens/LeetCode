# 问题分析：
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 编程实现：
```C++
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k)
    {
        int n=nums.size(),i;
        vector<int>sums=nums;
        for (i=1;i<n;i++)
        {
            sums[i]=sums[i-1]+nums[i];
        }
        double mx=sums[k-1];
        for (i=k;i<n;i++)
        {
            mx=max(mx,(double)sums[i]-sums[i-k]);
        }
        return mx/k;
    }
};
```
# 总结体会：
可以计算出任意一个长度为K的数组，然后来不断的更新res，最终就可以找到最大的那个答案。