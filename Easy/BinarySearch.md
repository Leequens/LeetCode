# 问题分析：
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 编程实现：
```C++
class Solution {
public:
    int search(vector<int>& nums, int target) 
    {
        int left=0,right=nums.size()-1,mid;

        while(left<=right)
        {
            mid=(left+right)/2;
            if(target==nums[mid])
                return mid;
            if(target<nums[mid])
                right=mid-1;
            if(target>nums[mid])
                left=mid+1;
        }
        return -1;
    }
};
```
# # 总结体会：
这道题就是普通的二分查找法