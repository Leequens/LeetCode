# 问题分析：

给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
# 编程实现：
```C++
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums)
    {
        vector<int> res(findNums.size());
        for (int i=0;i<findNums.size();i++) 
        {
            int j=0,k=0;
            for (j=0;j<nums.size();j++) 
            {
                if (nums[j]==findNums[i]) 
                    break;
            }
            for (k=j+1;k<nums.size();k++) 
            {
                if (nums[k]>nums[j]) 
                {
                    res[i] = nums[k];
                    break;
                }
            }
            if (k==nums.size()) res[i]=-1;
        }
        return res;
    }
};
```
# 总结体会：
首先遍历子集合中的每一个数字，然后在原数组中找到这个数字，然后向右遍历，找到第一个大于该数字的数即可。