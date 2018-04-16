# 问题分析：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

# 编程实现：

```C++
class Solution {
public:
    bool isValid(string s)
    {
        stack<char>a;
        int i;
        for (i = 0; i < s.size();i++) 
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
                a.push(s[i]);
            else {
                if (a.empty()) return false;
                if (s[i] == ')' && a.top() != '(') return false;
                if (s[i] == ']' && a.top() != '[') return false;
                if (s[i] == '}' && a.top() != '{') return false;
                a.pop();
            }
        }
        return a.empty();
    }
};
```
# 总结体会：
使用stack来解决，stack是一个想先进后出的栈，如果遇到左括号就压入栈中，遇到右括号就与栈顶比较，top正好是最近一次压入的左括号，如果不相等就返回false。如果相等就删除栈中刚刚被匹配的左括号。如果所有括号匹配，最后正好删除完栈中所有元素，所以判断栈是否为空，就判断了输入的括号是否匹配。