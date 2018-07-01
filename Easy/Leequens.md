# 问题分析：
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
```
# 总计体会：
的答复大师傅染发大师傅艾尔　大师傅大发嗯嗯ｅ
２２２