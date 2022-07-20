# ▣ 입력설명
# 첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.
#
# ▣ 출력설명
# 첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.
#
# ▣ 입력예제 1
# 7
#
# ▣ 출력예제 1
# 21


def DFS(len):
    # 이미 저장된 값을 호출하기
    if dy[len] > 0:
        return dy[len]

    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))
