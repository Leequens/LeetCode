# 问题分析：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

# 编程实现：
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target)
    {
        int i,j,n;
        n=nums.size();
        if(nums[0]>target)
            return 0;
        if(nums[n-1]<target)
            return n;
        for(i=0;i<n;i++)
        {
            if(nums[i]==target)
            {
                return i;
                break;
            }
        }
        for(j=0;j<n;j++)
        {
            if(nums[j]<target&&nums[j+1]>target)
                return j+1;          
        }
    }
};
```
# 总结体会：
先判断，如果目标值小于数组中的第一个值，则返回0，如果大于最后一个值，则返回n（数组的长度）。
然后再遍历数组，看是否有与目标值相等的，如果没有相等的，再寻找一个比目标值大的元素，一个比目标值小的元素，将目标值插入其中。
