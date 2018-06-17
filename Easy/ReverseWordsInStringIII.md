# 问题分析：
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 编程实现：
```C++
class Solution {
public:
    string reverseWords(string s)
    {
        int start=0,end=0,n=s.size(),i,j;
        while(start<n&&end<n) 
        {
            while (end<n&&s[end]!=' ') 
                end++;
            for (i=start,j=end-1;i<j;i++,j--) 
            {
                swap(s[i],s[j]);
            }
            start=++end;
        }
        return s;
    }
};
```
# 总结体会：
用两个指针，分别指向每个单词的开头和结尾位置，确定了单词的首尾位置后，再用两个指针对单词进行首尾交换即可。


