# 问题分析：
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
# 编程实现：
```C++
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c)
    {
        int m=nums.size(),n=nums[0].size();
        if (m*n!=r*c) 
            return nums;
        vector<vector<int>>res(r,vector<int>(c));
        for (int i=0;i<r;i++) 
        {
            for (int j=0;j<c;j++) 
            {
                int k=i*c+j;
                res[i][j]=nums[k/n][k%n];
            }
        }
        return res;
    }
};
```
# 总结体会：
判断能否转换为要求的矩阵，可以通过元素个数是否相同来判断，然后新建一个目标大小的数组，可以把原数组拉直成一个一维数组，开始遍历，然后再算出在原数组中的对应位置赋值过来即可。