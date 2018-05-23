# 问题分析：
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 编程实现：
```C++
class Solution {
public:
    string reverseVowels(string s)
    {
        int left=0,right=s.size()-1;
        while (left<right) 
        {
            if (judge(s[left])&&judge(s[right])) 
            {
                swap(s[left],s[right]);
                left++;
                right--;
            } 
            else if(judge(s[left]))
            {
                right--;
            } 
            else if(judge(s[right]))
            {
                left++;
            }
            else
            {
                left++;
                right--;
            }
        }
        return s;
    }
    bool judge(char c) 
    {
        return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
    }
};
```
# 总结体会：
写一个子函数来判断字符是否为元音字母，大写的也算，如果两边都是元音，就交换，如果左边的不是，向右移动一位，如果右边的不是，则向左移动一位，如果都不是，就都移动。