# 问题分析：
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。 

如果没有两个连续的 1，返回 0 。

# 编程实现：
```C++
class Solution {
public:
    int binaryGap(int N) {
        int maxx=0, tmp=0;
        vector<int> asd;
        for(int i = 0; N != 0; i++)
        {
            int a = N%2;
            asd.insert(asd.begin(), a);
            N/=2;
        }
        for(int i = 0; i < asd.size(); i++)
        {
            if(asd[i] == 1)
            {
                maxx = max(maxx, i - tmp);
                tmp = i;
            }
        }
        return maxx;
    }
};
```
# 总结体会：
先根据十进制转二进制的方法将给定的十进制数转为二进制数。然后从二进制数的最高位开始比较，如果当前为1，求当前所取最大距离与当前1和上一个1的距离的最大值。遍历结束后即可得到结果。