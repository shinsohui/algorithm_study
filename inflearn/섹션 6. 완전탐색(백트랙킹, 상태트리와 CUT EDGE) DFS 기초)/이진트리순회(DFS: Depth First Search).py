def DFS(v):
    if v > 7:
        return
    else:
        # print(v, end=' ')
        DFS(v * 2)
        # print(v, end=' ')
        DFS(v * 2 + 1)
        print(v, end=' ')


if __name__ == "__main__":
    DFS(1)
