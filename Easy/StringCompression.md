# 问题分析：
给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。
# 编程实现：
```C++
class Solution {
public:
    int compress(vector<char>& chars) {
        int n=chars.size(),cur=0,i,j;
        for (i=0,j=0;i<n;i=j)
        {
            while(j<n&&chars[j]==chars[i]) 
                j++;
            chars[cur++]=chars[i];
            if(j-i==1) 
                continue;
            for(char c:to_string(j-i)) 
                chars[cur++]=c;
        }
        return cur;
    }
};
```
# 总结体会：
用j来找重复的字符串的个数，用一个while循环，最终j指向的是第一个和i指向字符不同的地方，然后我们判断j是否比i正好大一个，将重复个数转为字符串，然后提取出来修改chars数组即可。	