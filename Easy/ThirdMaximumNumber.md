# 问题分析：
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

# 编程实现：
```C++
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long m1=LONG_MIN,m2=LONG_MIN,m3=LONG_MIN;
        int i;
        for (i=0;i<nums.size();i++)
        {
            if (nums[i]>m1) {
                m3=m2;
                m2=m1;
                m1=nums[i];
            } 
            else if(nums[i]>m2&&nums[i]<m1)
            {
                m3=m2;
                m2=nums[i];
            } 
            else if(nums[i]>m3&&nums[i]<m2) 
            {
                m3= nums[i];
            }
        }
        if(m3==LONG_MIN||m3==m2) return m1;
        else return m3;
    }
};                                                                                                                                                    
```

# 总结体会：
用三个变量m1,m2,m3来分别保存第一大，第二大，和第三大的数，然后遍历数组，如果数字大于当前第一大的数，那么三个变量各自错位赋值，如果当前数字大于m2，小于m1，那么就更新m2和m3，如果当前数字大于m3，小于m2，那就只更新m3，最后判断返回即可。