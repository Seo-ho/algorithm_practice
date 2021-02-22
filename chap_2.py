# 재귀함수
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)


# 오름차순
def countup(n):
    if n>0:
        countup(n - 1)
        print(n)


# 내려갓다 올라갓다
def countdown_up(n):
    if n>0:
        print(n)
        countdown_up(n-1)
        print(n)


countdown(4)
countup(4)
countdown_up(4)


# 팩토리얼
def factorial(n):
    if n >= 0:
        if n == 1 or n == 0:
            return 1
        return n*factorial(n-1)


def factorial(n):
    if n == 0: # base case
        return 1
    # elif n > 0: # recursive case
    return n*factorial(n-1)


factorial(5)


# 그냥 sum 간결한 함수
def sum_generator(N):
    return sum(n for n in range(1, N + 1))