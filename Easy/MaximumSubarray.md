# 问题分析：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 编程实现：
```C++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int a=INT_MIN,b=0,i;
        for (i=0;i<nums.size();i++)
        {
            if(b+nums[i]>nums[i])
                b=b+nums[i];
            else 
                b=nums[i];
            if(b>a)
                a=b;
            else
                a=a;
        }
        return a;
    }
};
```
# 总结体会：
设定变量b=0，每遍历一个数字，就把b加该数字的和与该数字比大小，大的存入b中，定义a为int型最小值，再把a和b比大小，大的存入a。遍历完后a的值就是连续子数组的最大值。