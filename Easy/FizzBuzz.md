# 问题分析：

写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 编程实现:
```C++
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        int i;
        for(i=1;i<=n;i++)
        {
            if(i%15 == 0) res.push_back("FizzBuzz");
            else if(i%3==0) res.push_back("Fizz");
            else if(i%5==0) res.push_back("Buzz");
            else res.push_back(to_string(i));
        }
        return res;
    }
};
```

# 总结体会：
设定一个新的动态数组存储答案，分情况压入不同的字符，当不是3也不是5高的倍数的时候，要用to_string()函数把in转换为string型变量。
最后返回数组即可。