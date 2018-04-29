# 问题分析：
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 编程实现：
```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        int n,a,i,j;
        for(i=0;i<nums.size();i++)
        {
            a=nums[i];
            n=1;
            for(j=0;j<nums.size();j++)
            {
                if(nums[i]==nums[j])
                {
                    n++;
                }
            }
            if(n==2)
            {
                break;     
            }
        }
        return a;
    }
};
```
# 总结体会：
从头到尾遍历两遍数组，如果某个数一共只出现了两次，则相当于该数在数组中只出现了一次，返回该值即可。