# 혼합하였을 때 특성값이 0에 가까워지는 두 용액을 구하라
# 산성만 있을 수도 있고 알카리만 있을 수도 있음

# 입력값 받기
N = int(input())
solutions_list = list(map(int, input().split()))

# 용액 오름차순 정렬하기
solutions_list.sort()

# 투 포인터 설정
start = 0
end = N-1

# 정답
answer = 2000000000 # 기준점
solutions = []

# 투 포인터 진행
while start < end:
    start_solution = solutions_list[start]
    end_solution = solutions_list[end]

    mixed_solution = start_solution + end_solution
    # 두 용액의 합이 0에 더 가까울 때
    if abs(mixed_solution) < answer:
        answer = abs(mixed_solution)
        solutions = [start_solution, end_solution]

    # 두 용액의 합이 0보다 작을 때, 시작 포인터를 +1
    if mixed_solution < 0:
        start += 1

    # 두 용액의 합이 0 보다 클 때, 끝 포인터를 -1
    else:
        end -= 1

print(solutions[0], solutions[1])