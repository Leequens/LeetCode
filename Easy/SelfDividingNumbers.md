# 问题分析：
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
# 编程实现:
```C++
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right)
    {
        vector<int> res;
        int i,n;
        for (i=left,n=0;i<=right;i++) 
        {
            for (n=i;n>0;n=n/10)
            {
                if(n%10==0||i%(n%10)!=0) 
                    break;
            }
            if (n==0) res.push_back(i);
        }
        return res;
    }
};
```
# 总结体会：
使用两个For循环，一个遍历整个数组，一个for循环来判断当前数是否为自除数，如果是的话就存入东外数组，最终得到答案。