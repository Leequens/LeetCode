# 问题分析：
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

#编程实现：

```C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        int i=0;
        if(nums.empty())
            return 0;
        while(i<nums.size())
        {
            if(nums[i]==val)
            {
              nums.erase(nums.begin()+i);
              continue;
            }
            i++;
        }
        return nums.size();
    }
};
```

# 总结体会：

和昨天的题类似。相同则删除，并且要先判断空数组的情况。
