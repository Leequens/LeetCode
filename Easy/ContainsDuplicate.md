# 问题分析：

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
# 编程实现：
```C++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) 
    {
        int i;
        if(nums.size()==0) return false;  
        if(nums.size()==1) return false; 
        sort(nums.begin(),nums.end()); 
        for(i=1;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1])
                return 1;
        }
        return 0;
    }
};
```
# 总结体会：
先使用sort语句将vector数组排序，然后再遍历数组看有没有相邻元素重复的情况，有的话就返回true，没有的话就返回false。