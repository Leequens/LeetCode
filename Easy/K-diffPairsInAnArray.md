# 问题分析：
给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.
# 编程实现：
```C++
class Solution {
public:
    int findPairs(vector<int>& nums, int k)
    {
        if(nums.size()==0)
            return 0;
        int count=0;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++)
        {
            for(int j=i+1;j<nums.size();j++)
            {
                if(nums[j]-nums[i]==k)
                {
                    count++;
                    break;
                }
            }
            while(nums[i]==nums[i+1])
                i++;    
        }
        
        return count;
    }
};
```
# 总结体会：
看到题目就想到要遍历两次数组来实现，首先判断输入空数组的情况。如果数组非空，则设置一个计数器count，将数组排序，然后遍历数组，将每个数字与后面的数字求差，如果差为K，则计数器+1，一旦得到差值为K的数字后要立刻break，这样能节省时间。最后要删去相同的元素，否则得到的count会比真正答案大。