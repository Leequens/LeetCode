# 问题分析：

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 编程实现：
```C++
class Solution {
public:
    void rotate(vector<int>& nums, int k)
    {
        if (nums.empty()||(k%= nums.size())== 0)
            return;
        int n=nums.size(),start=0,i=0,cur=nums[i],cnt=0;
        while (cnt++<n)
        {
            i=(i+k)%n;
            int t=nums[i];
            nums[i]=cur;
            if (i==start) 
            {
                start++; 
                i++;
                cur=nums[i];
            } 
            else 
            {
                cur=t;
            }
        }
    }
};
```
# 总结体会：
复制一个和nums一样的数组，然后再不断的通过关系i=(i+k)%n来交换数字，最终得到目标数组。