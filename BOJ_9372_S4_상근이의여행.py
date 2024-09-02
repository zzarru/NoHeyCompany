# 최소한의 비행기 종류를 이용하여 모든 나라를 여행하라

# 입력 받기
tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split()) # N개의 나라, M개 종류의 비행기
    for _ in range(M):
        a, b = map(int, input().split())

    # 주어지는 비행 스케쥴은 항상 연결 그래프를 이룬다.
    # 따라서 간선의 최소 개수는은 (노드 - 1)를 이룬다.
    print(N-1)