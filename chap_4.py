# 특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수
def sublist_max(profits):
    max_profit = 0
    print(len(profits))
    for j in range(len(profits) - 1):
        for i in range(j + 1, len(profits) + 1):
            # if max_profit < sum(profits[j:i]):
            #    max_profit = sum(profits[j:i])
            print(profits[j:i])
            max_profit = max(max_profit, sum(profits[j:i]))
    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
a = [4, 3, 8, -2, -5, -3, -5, -3]


# sublist_max를 divide and conquer 방식으로. 시간복잡도는 O(nlgn)이 되어야 함.
def sublist_max(profits, start, end):
    if end == start:
        print(profits[start])
        return profits[start]
    mid = (start + end) // 2

    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)

    return max_profit


def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2
    left_sum = 0
    left_max = profits[mid]

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)
    right_sum = 0
    right_max = profits[mid + 1]

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))


# O(n) 으로 줄이기
def sublist_max(profits, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(profits)
    mid = (start + end) // 2







# 거듭 제곱 빠르게 계산하기
def power(x, y):
    # base case
    if y == 0:
        return 1
    result_sub = power(x, y // 2)
    if y % 2 == 0:
        return result_sub * result_sub
    else:
        return x * result_sub * result_sub
    return x * power(x, y - 1)


# 최대한 적은 약수터 들리기
def select_stops(water_stops, capacity):
    index = 0
    output = []
    max_water = capacity
    while index < len(water_stops):
        if water_stops[index] == max_water:
            output.append(water_stops[index])
            max_water = water_stops[index] + capacity
            # capacity += capacity
            index += 1
        elif water_stops[index] > max_water:
            output.append(water_stops[index - 1])
            max_water = water_stops[index - 1] + capacity
        else:
            index += 1
    output.append(water_stops[index - 1])
    return output


def select_stops(water_stops, capacity):
    stop_list = []
    prev_stop = 0
    for i in range(len(water_stops)):
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))


# 중복되는 수 찾기
def find_same_number(some_list):
    sort_list = sorted(some_list)
    i = 0
    while i < len(some_list) - 1:
        if sort_list[i] == sort_list[i + 1]:
            return sort_list[i]
        i += 1


def find_same_number(some_list):
    elements_seen_so_far = {}

    for element in some_list:
        if element in elements_seen_so_far:
            return element
        elements_seen_so_far[element] = 1


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

