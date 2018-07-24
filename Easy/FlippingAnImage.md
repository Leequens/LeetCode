# 问题分析：
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
# 编程实现：
```C++
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A)
    {
        int temp;
        for(int i=0;i<A.size();i++)
        {
            for(int l=0,r=A[0].size()-1;l<r;l++,r--)
            {
                temp=A[i][r];
                A[i][r]=A[i][l];
                A[i][l]=temp;    
            }
        }
        for(int i=0;i<A.size();i++)
        {
            for(int j=0;j<A[0].size();j++)
            {
                if(A[i][j]==1)
                    A[i][j]=0;
                else
                    A[i][j]=1;
            }
        }
        return A;
    }
};
```
# 总结体会：
这道题先让水平翻转，水平翻转其实就是逆序，用一个temp中间值即可完成，随后再把0变为1，1变为0即可。