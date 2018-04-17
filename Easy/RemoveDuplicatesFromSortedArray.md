# 问题分析：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


# 编程实现：

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int i=0;
        if(nums.size()==0)
            return 0;
        while(i<nums.size()-1)
        {
            if(nums[i]==nums[i+1])
            {
                nums.erase(nums.begin()+i);
                continue;
            }
            else i++;              
        }
        return nums.size();        
    }
};
```

# 总结体会：
题目不难，判断数组中第一个数与第二个数是否相等，相等则使用vector中的erase删除第一个即可。
不过需要注意的有两点：
（1）删除元素后指针自动指向下一个元素，所以不能i++，continue即可。    
（2）需要判断数组为空时的情况，否则Leetcode提交会报错。
