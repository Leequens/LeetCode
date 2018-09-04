# 问题分析：
给定一个Excel表格中的列名称，返回其相应的列序号。
# 编程实现：
```C++
class Solution {
public:
    int titleToNumber(string s) {
        int n = s.size();
        int res = 0;
        int tmp = 1;
        for (int i = n; i >= 1; --i) {
            res += (s[i - 1] - 'A' + 1) * tmp; 
            tmp *= 26;
        }
        return res;
    }
};
```
# 总结体会：
相当于将二十六进制转换为十进制，一位位的转换即可。