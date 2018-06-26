# 问题分析：
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 编程实现：
```C++
class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        int count,n=nums.size(),num;
        for(int i=0;i<n;i++)
        {
            num=nums[i];
            count=0;
            for(int j=0;j<n;j++)
            {
                if(nums[i]==nums[j])
                {
                    count++;
                }
            }
            if(count==1)
            {
                break;     
            }
        }
        return num;
    }
};
```
# 总结体会：
开始分类复习做题，首先是数组的题，题目要求找到数组中只出现了一次的数，于是从第一个数字开始遍历，将当前数字存入新的遍历num中，并设置一个为0的计数器count，再从头遍历数组，查询这个num出现的次数，如果遍历完次数为1，直接break结束循环返回num即可。感觉自己的方法不是很高效，看了网上一些大神的解法， 有个最牛的是使用异或来解决，真是很难想到。