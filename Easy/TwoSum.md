# 问题分析：
两数之和：
给定一个整数数列，找出其中和为特定值的那两个数。你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

# 编程实现：
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
   {
        vector<int> a;
        int i,j;
        for(i=0;i<nums.size();i++)
        {
            for(j=i+1;j<nums.size();j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    a.push_back(i);
                    a.push_back(j);
                }
            }
        }
        return a;
    }
};
```
# 总结体会：
寻找这两个特定的数，用两个for循环遍历数组即可，再用条件语句寻找符合题目要求的两个数的下标，存入新的数组。
