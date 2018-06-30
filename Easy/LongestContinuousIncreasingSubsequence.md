# 问题分析：
给定一个未经排序的整数数组，找到最长且连续的的递增序列。
# 编程实现：
```C++
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) 
    {
        int count=0,res=0,i;
        for(i=0;i<nums.size();i++)
        {
            if(i==0||nums[i-1]<nums[i])
            {
                count++;
                res=max(res,count);
            }
            else
                count=1;
        }
        return res;
    }
};
```
# 总结体会：
我首先定义一个变量count来保存当前所遇到的递增序列的长度，res来保存目前为止最大的递增序列长度，判断当前数是否大于前一个数，如果大于的话，就讲count自增，并判断是否大于res，如果大的话就讲count保存到res中，需要注意的是，当i为0时没有前一个数，所以此时也要自增1。