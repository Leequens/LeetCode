# 问题分析：
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1

11

21

211

111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
# 编程分析：
```C++
class Solution {
public:
    string countAndSay(int n)
    {
        int i,cnt;
        if(n<=0) 
            return "";
        string cur,res="1";
        while(--n)
        {
            cur="";
            for(i=0;i<res.size();i++)
            {
                cnt=1;
                while(i+1<res.size()&&res[i]==res[i+1])
                {
                    cnt++;
                    i++;
                }
                cur=cur+to_string(cnt)+res[i];
            }
            res=cur;
        }
        return res;
    }
};
```
# 总结体会：
对于前一个数，找出相同元素的个数，把个数和该元素存到新的string里，最终就会得到答案。
