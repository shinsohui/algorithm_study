import sys
input = sys.stdin.readline
text = input()
text_lst = list(text)
result = [0]*(len(text_lst))

for j in range(len(text_lst)) :
    result[j] = text_lst[j:-1]

result_sorted = sorted(result)

for i in range(1,len(text_lst)) :
    print("".join(result_sorted[i]))