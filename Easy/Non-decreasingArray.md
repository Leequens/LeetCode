# 问题分析：
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
# 编程实现：
```C++
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt=1,n=nums.size();
        for(int i=1;i<n;i++)
        {
            if(nums[i]<nums[i-1]) 
            {
                if (cnt= 0) 
                    return false;
                if (i==1||nums[i]>=nums[i-2])
                    nums[i-1]=nums[i];
                else 
                    nums[i]=nums[i-1];
                cnt--;
            } 
        }
        return true;
    }
};
```
# 总结体会：
当后面的数字小于前面的数字时，或者修改大数，或者修改小数，和前面的前面的那个数有关系。用一个变量cnt，初始化为1，修改数字后cnt自减1，当下次再需要修改时，如果cnt已经为0了，直接返回false。遍历结束后返回true。