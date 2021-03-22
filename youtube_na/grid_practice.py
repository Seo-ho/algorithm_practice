def practice_1(N, k):
    count = 0
    while N > 1:
        if N % k == 0:
            N = N / k
        else:
            N -= 1
        count += 1
    return count


practice_1(25, 5)
practice_1(17, 4)
practice_1(25, 3)

# 이 방법이 시간 복잡도를 많이 줄일 수 있음
# N, k를 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0
while True:
    # N이 k로 나누어 떨어지는 수가 될 때까지 빼기
    # n//k >> 몫구하기.
    target = (n // k) * k
    result += (n - target)
    n = target
    print("target: ", target, "result: ", result, "n: ", n)
    # N이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)


# 이게 좋은 방식
def practice_2(str):
    result = int(str[0])
    for i in str[1:]:
        i = int(i)
        if i <= 1 or result <= 1:
            result += i
        else:
            result *= i
    return result


def practice_2_2(str):
    n = 0
    prev = int(str[0])
    # cur = int(str[0])
    while n < len(str):
        n += 1
        # prev = cur
        cur = int(str[n])
        if prev <= 1 or cur <= 1:
            prev = prev + cur
        else:
            prev = prev * cur
    return prev


practice_2('02984')
practice_2('567')


def practice_3(N, afraid):
    afraid.sort()
    count = 0
    while True:
        print("len: ", len(afraid))
        if afraid[afraid[0] - 1] <= N:
            count += 1
            N -= afraid[0]
            afraid = afraid[afraid[0]:]

        else:
            break
        print("afraid: ", afraid, "count: ", count)


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수
for i in data:
    count += 1
    if count >= i:  # 현재 그룹에 포함된 모함가의 수가 현재의 공포도 이상이라면
        result += 1
        count = 0
print(result)


# 프로그래머스 Greedy 1번
def solution(n, lost, reserve):
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN = sorted(lostN, reverse=True)
    for i in lostN:
        front = i - 1
        back = i + 1

        # if i in reserve:
        #    reserve.remove(i)
        # count += 1
        if back in reserveN:
            reserveN.remove(back)
            # count += 1
        elif front in reserveN:
            reserveN.remove(front)
            # count += 1

        else:
            n -= 1
    return n


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [])

for i in range(1, 5):
    print(i)
# 상하좌우 문제
def practice_4(N, lst):
    nx = 1
    ny = 1
    length = len(lst)
    for i in range(length):
        if lst[i] == 'R':
            if ny != N:
                ny += 1
        elif lst[i] == 'L':
            if ny != 1:
                ny -= 1
        elif lst[i] == 'U':
            if nx != 1:
                nx -= 1
        elif lst[i] == 'D':
            if nx != N:
                nx += 1

    return (nx, ny)
practice_4(5, ['R', 'R', 'R', 'U', 'D', 'D'])


n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny