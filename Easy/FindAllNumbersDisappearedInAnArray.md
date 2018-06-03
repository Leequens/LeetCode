# 问题分析：
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 编程实现：
```C++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) 
    {
        vector<int> res;
        int i,a;
        for (i=0;i<nums.size();i++) 
        {
            a=abs(nums[i])-1;
            nums[a]=(nums[a]>0)?-nums[a]:nums[a];
        }
        for(i=0;i<nums.size();i++) 
        {
            if (nums[i]>0) 
            {
                res.push_back(i+1);
            }
        }
        return res;
    }
};
```

# 总结体会：
对于每个数字nums[i]，如果其对应的nums[nums[i] - 1]是正数，就赋值为其相反数，如果已经是负数了，就不变了，最后只要把留下的整数对应的位置加入结果res中即可