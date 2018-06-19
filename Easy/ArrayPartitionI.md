# 问题分析：

给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
# 编程实现：
```C++
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int res=0,n=nums.size(),i;
        sort(nums.begin(),nums.end());
        for (i=0;i<n;i=i+2)
        {
            res=res+nums[i];
        }
        return res;
    }
};
```
# 总结体会：
给数组排个序，然后按顺序的每两个就是一对，取出每对中的第一个数即为较小值累加起来，就能得到想要的答案。