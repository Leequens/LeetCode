# 问题

给定一个整数数列，找出其中和为特定值的那两个数。你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

# 程序

```C
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.count(target - nums[i])) {
                return {i, m[target - nums[i]]};
            }
            m[nums[i]] = i;
        }
        return {};
    }
};
```
