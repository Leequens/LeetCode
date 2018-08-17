# 问题分析:
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 编程实现:
```C++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target)
    {
        int sum=nums[0]+nums[1]+nums[2];
        int temp=abs(sum-target);
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-2;i++)
        {
            int left=i+1,right=nums.size()-1;
            while(left<right)
            {
                int newsum=nums[i]+nums[left]+nums[right];
                if(temp>abs(newsum-target))
                {
                    temp=abs(newsum-target);
                    sum=newsum;
                }
                if(newsum>target)
                    right--;
                else 
                    left++;
            }
        }
        return sum;
    }
};
```
# 总结体会:
这个题让寻找三个数,使得三个数的和与目标值的差值最小, 从头开始遍历,设置左右两个变量,每遍历一个值,就把三个值都加起来,将这个和与目标值作差取绝对值,与之前存储的差值比较,不断的更新差值和总和,最后返回这个和即可.