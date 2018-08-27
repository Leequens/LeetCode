# 问题分析：
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。
# 程序实现：
```C++
class Solution {
public:
    int majorityElement(vector<int>& nums)
    {
        int n,i,j;
        if(nums.size()==1)
            return nums[0];
        n=nums[0];
        j=1;
        for(i=1;i<nums.size();i++)
        {
            if(nums[i]==n)
                j++;
            else if(j==0)
            {
                n=nums[i];
                j=1;
            }        
            else
                j--;
        }
        return n;
    }
};
```
# 总结体会：
如果遍历两遍数组从头开始求数字出现的次数并与n/2比较的话，会超出时间限制。所以要采用其他的方法，先假设第一个数就是众数，设置一个变量存储“众数”所出现的次数，如果出现与此数相同的数，就加1，不同减1，当计数器等于0时，此时的数设为新的“众数”，并且将计数器设置为1。遍历结束后即可求得。

