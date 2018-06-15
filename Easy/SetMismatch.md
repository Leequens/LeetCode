# 问题分析：
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

# 编程实现：
```C++
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums)
    {
        vector<int>res(2,0),cnt(nums.size(),0);
        for (int num:nums) cnt[num-1]++;
        for (int i=0;i<cnt.size();i++)
        {
            if(res[0]!=0&&res[1]!=0) 
                return res;
            if(cnt[i]==2) 
                res[0]=i+1;
            else if(cnt[i]==0) 
                res[1]=i+1;
        }
        return res;
    }
};
```
# 总结体会：
先统计每个数字出现的次数，然后再遍历次数数组，如果某个数字出现了两次就是重复数，如果出现了0次，就是缺失数。