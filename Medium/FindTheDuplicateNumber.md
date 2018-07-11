# 问题分析：
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
# 编程实现：
```C++
class Solution {
public:
    int findDuplicate(vector<int>& nums)
    {
        sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++)
            if(nums[i]==nums[i-1])
                return nums[i];
    }
};
```
# 总结体会：
要找重复的数字，就直接排个序，然后从第二个数字开始遍历，返回与前一个元素相同的元素即可。