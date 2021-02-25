# 특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수
def sublist_max(profits):
    max_profit = 0
    for j in range(len(profits) - 1):
        # start = 0
        # end = 1
        for i in range(j + 1, len(profits) + 1):
            # print(i)
            # print(sum(profits[j:i]))
            # print("j: ", j, "i:", i)
            # if max_profit < sum(profits[j:i]):
            #    max_profit = sum(profits[j:i])
            max(max_profit, sum(profits[j:i]))
            # print(max_profit)
            # max_profit =sum(profits[start:end])
    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))


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


def find_same_number(some_list):



# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))