import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  s = [0 for _ in range(N)] # 0으로 인원만큼 초기화
  count = 1 # 한명은 무조건 뽑기 때문에 1로 초기화 한다.

  for _ in range(N):
    resume, interview = map(int, input().split())
    s[resume-1] = interview

  min = s[0]

  for i in range(1, N):
    if s[i] < min: # 최솟값이 더 클경우 1을 증가시킨다.
      count += 1
      min = s[i]

  print(count)