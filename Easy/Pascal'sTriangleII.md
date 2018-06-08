# 问题分析：
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
# 编程实现：
```C++
class Solution {
public:
    vector<int> getRow(int rowIndex)
    {
        vector<int> out;
        if (rowIndex<0) 
            return out;        
        out.assign(rowIndex+1,0);
        for (int i = 0; i <= rowIndex; ++i) 
        {
            if ( i == 0) 
            {
                out[0] = 1;
                continue;
            }
            for (int j = rowIndex; j >= 1; --j)
            {
                out[j] = out[j] + out[j-1];
            }
        }
        return out;
    }
};
```
# 总结体会：
因为杨辉三角中除了第一个和最后一个数字之外，其他的数字都是上一行左右两个值之和。那么只需要两个for循环，除了第一个数为1之外，后面的数都是上一次循环的数值加上它前面位置的数值之和，不停地更新每一个位置的值，便可以得到第n行的数字。