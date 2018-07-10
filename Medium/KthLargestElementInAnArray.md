# 问题分析：
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 编程实现：
```C++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        sort(nums.begin(),nums.end());
        return nums[nums.size()-k];
    }
};
```
# 总结体会：
题目要找第K个最大的元素，既然数组是未排序的，那么就给数组排个序，然后直接返回第K个数就好了