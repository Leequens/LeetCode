# 问题分析：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


# 编程实现：
```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i=0,j=0;
        while(j<nums.size())
        {
            if(nums[j]!=0)
            {
                swap(nums[i],nums[j]);
                i++;
            }
            j++;
        }
    }
};
````
# 总结体会：
建立一个下标，不停的往后遍历，寻找到非零位置，就和前面那个交换位置，交换使用swp函数，最终0都会移到末尾。