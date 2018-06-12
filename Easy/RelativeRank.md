# 问题分析：
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)
# 编程实现：
```
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums)
    {
        int n=nums.size();
        vector<int>idx(n);
        vector<string>res(n, "");
        for (int i=0;i<n;i++) 
            idx[i]=i;
        sort(idx.begin(),idx.end(),[&](int a, int b){return nums[a]>nums[b];});
        for (int i=0;i<n;i++)
        {
            if (i == 0) res[idx[i]]="Gold Medal";
            else if (i == 1) res[idx[i]]="Silver Medal";
            else if (i == 2) res[idx[i]]="Bronze Medal";
            else res[idx[i]]=to_string(i+1);
        }
        return res;
    }
};
```
# 总结体会：
建立一个分数数组，一个坐标数组，对分数进行高低排序，各自的索引要对应好，然后前三名的分别给金牌、银牌和铜牌，后面的给名次数。