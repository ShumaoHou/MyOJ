'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    elif len(s) % 2 != 0:
        return False
    stack = []
    for i in range(len(s)):
        ch = s[i:i + 1]
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            s_peek = stack[len(stack) - 1]
            if (s_peek == "(" and ch == ")") or (s_peek == "[" and ch == "]") or (s_peek == "{" and ch == "}"):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("(]"))