# 问题分析：
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。
# 编程实现：
```C++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums)
    {
        int i,j,res=0,index=nums.size(),n=nums.size(),temp;
        for(i=1;i<n;i++) 
        {
            if(nums[i]<nums[i-1])
            {
                j=i;
                while(j>0&&nums[j]<nums[j-1])
                {
                    temp=nums[j];
                    nums[j]=nums[j-1];
                    nums[j-1]=temp;
                    j--;
                }
                if (index>j) 
                    index=j;
                res=max(res,i-index+1);
            }
        }
        return res;
    }
};
```
# 总结体会：
这个题主要是找出无序数组的起始位置，定义一个变量index来保存起始位置，如果某个数字比前面的数字小，就要把这个数字移动到正常排序的位置，用j来保存移动后的位置，如果此时的index比j要大，那么就要更新index的值，确定好了index，数组的大小就很好确定了。