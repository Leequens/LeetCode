# 问题分析：
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

# 编程实现：
```C++
class Solution {
public:
    int pivotIndex(vector<int>& nums) 
    {
        int sum=0,n=nums.size();
        for(int i=0;i<n;i++)
            sum=sum+nums[i];
        int a=0;
        for(int i=0;i<n;i++)
        {
            if(sum-nums[i]==2*a) 
                return i;
            a=a+nums[i];
        }
        return -1;
    }
};
```
# 总结体会：
这个比较简单，首先需要求出数组的总和，再用一个变量a来存储当前数组的和，遍历到某一个数字的时候，用总和减去这个数字，看看得到的答案是不是a的两倍，如果是两倍的话，那么这个数字就是中枢点。