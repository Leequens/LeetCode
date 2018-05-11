# 问题分析：
给定一个二进制数组， 计算其中最大连续1的个数。

# 编程实现：
```C++
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums)
    {
        int i,res=0,a=0;
        for(i=0;i<nums.size();i++)
        {
            if(nums[i]==1)
                a++;
            if(nums[i]==0)
            {
                if(a>res)
                    res=a;
                a=0;
            }
        }
        return max(a,res);
    }
};
```
# 总结体会：
设置一个变量res储存遍历过的连续1的最多数目，a储存当前所在的1的数目，当num等于0时比较，如果a大于res，则res等于a。最后返回res和a中最大的数，这是为了防止连续1最大的个数在数组的结尾处。