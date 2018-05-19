# 问题分析：
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 编程实现：
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0,r=numbers.size()-1,sum;
        while(l<r)
        {
            sum=numbers[l]+numbers[r];
            if (sum==target) 
                return {l+1,r+1};
            else if(sum<target) 
                l++;
            else r--;
        }
    }
};
```
# 总结体会：
因为数组的元素是按从小到大排列的，所以可以建立两个变量，分别指向数组的最左与最右，如果这两个元素和为目标值，返回它们即可，如果小了，就把左元素右移，如果大于目标值，就把右元素向左移，最终肯定能找到这两个元素。