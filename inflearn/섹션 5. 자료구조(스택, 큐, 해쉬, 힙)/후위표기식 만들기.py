# ▣ 입력설명
# 첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
# 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
#
# ▣ 출력설명 후위표기식을 출력한다.
#
# ▣ 입력예제 1
# 3+5*2/(7-2)
#
# ▣ 출력예제 1
# 352*72-/+
#
# ▣ 입력예제 2
# 3*(5+2)-9
#
# ▣ 출력예제 2
# 352+*9-

a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():
        res += x  # 숫자라면 바로 출력
    else:
        if x == '(':  # 여는 괄호 만나면 stack에 push
            stack.append(x)
        elif x == '*' or x == '/':
            # stack의 마지막 값이 '*'이나 '/'이라면 pop
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # stack이 마지막 값이 '('가 아니라면 pop
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')': # 닫는 괄호라면 여는 괄호 나올 때까지 출력
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)
