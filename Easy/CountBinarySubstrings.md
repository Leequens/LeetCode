# 问题分析：
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。
# 编程实现：
```C++
class Solution {
public:
    int countBinarySubstrings(string s) {
        int count0=0,count1=0,res=0;
         if(s[0]=='0') 
                    count0++;
                else
                    count1++;
        for (int i = 1; i < s.size(); ++i)
        {
        
            if (s[i]=='1')
            {
                if(s[i-1]=='1') 
                    count1++;
                else
                    count1=1;
                if(count0>=count1)
                    res++;
            } 
            else if (s[i]=='0') 
            {
                if(s[i-1]=='0') 
                    count0++; 
                else
                    count0=1;
                if(count1>=count0) 
                    res++;
            }
        }
        return res;
    }
};

```
# 总结体会：
这道题要判断字符串中连续0和1数量相同的子串的个数，因为必须是连续的，所以当前数字如果与前一个数字不相同的时候，该数字的计数器加就要置1。   
   
根据这个方法。首先判断第一个数字是什么，因为如果从第一个数字开始遍历，就不能与前一个数字相比较，第一个数字为1，count1++，否则count0++；随后开始从第二个字符遍历字符串，如果当前字符是1，看前一个字符，如果也是1，就count1++，否则count1置1；因为当前字符是1，所以只要目前的count0大于或者等于count1，就说明前面有与1相同个数的0;，此时res++；当前字符为0的时候方法类似。   
   
遍历完之后就可以得想要的答案。