# 问题分析：
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
# 编程实现：
```C++
class Solution {
public:
    int distributeCandies(vector<int>& candies) 
    {
        int count=1,n=candies.size();
        sort(candies.begin(),candies.end());
        for(int i=1;i<n;i++)
            if(candies[i]!=candies[i-1])
                count++;
        return min(n/2,count);  
    }
};
```
# 总结体会：
发现sort是真滴好用，先把糖果排序，计算出糖果的种类，因为是两个人分，一人一半，如果糖果种类小于一半，那么妹妹肯定是要每种糖会拥有，所以直接返回count就ok，如果糖果种类大于总数的一半，因为是两个人平均分，所以妹妹最多就是每种糖各来一个，返回总数的一半就ok