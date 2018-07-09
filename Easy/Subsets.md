# 问题分析：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
# 编程实现 ：
```C++
// Non-recursion
class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) 
    {
        vector<vector<int> > res(1);
        sort(S.begin(), S.end());
        for (int i = 0; i < S.size(); i++)
        {
            int size = res.size();
            for (int j = 0; j < size; j++)
            {
                res.push_back(res[j]);
                res.back().push_back(S[i]);
            }
        }
        return res;
    }
};
```
# 总结体会：
可以一位一位的网上叠加，首先是空数组，然后先加上第一个元素，得到res[s[0]]，然后再把自身的空集和新得到的都加上第二个元素...以此类推，就能得到最后答案。