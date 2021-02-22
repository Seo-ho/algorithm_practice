# 실습과제1
# 거꾸로 읽어도 똑같은 단어를 palindrome이라고 하는데
# 단어가 palindrome인지 확인하는 함수

# 1번
def is_palindrome(word):
    length = len(word)
    b = ""
    for i in range(1, length + 1):
        b += word[length - i]
    return b == word


# 2번
def is_palindrome2(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True


# 3번
def is_palindrome3(word):
    list_word = list(word)
    reversed_word = ''.join(reversed(list_word))


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))


# 어떤 원소가 리스트 안에 포함되어 있는지 확인
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None


# 2번
def linear_search(element, some_list):
    for num in some_list:
        if element == num:
            return some_list.index(element)
    return None


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))


# 이진탐색 - log(n)
# 정렬된 리스트를 전제로 함.
# 1번
def binary_search(element, some_list):
    start = 0
    end = len(some_list) - 1
    while True:
        median_index = (start + end) // 2
        if median_index == start and median_index == end:
            return None

        if some_list[median_index] == element:
            return median_index
        elif some_list[median_index] > element:
            end = median_index
        else:
            start = median_index


def binary_search(element, some_list):
    start = 0
    end = len(some_list) - 1
    while start <= end:
        median_index = (start + end) // 2
        if some_list[median_index] == element:
            return median_index
        elif some_list[median_index] > element:
            end = median_index - 1
        else:
            start = median_index + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


# 피보나치 수열 > O(2^n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    # else:
    return fib(n - 1) + fib(n - 2)


for i in range(1, 11):
    print(fib(i))


# n번째 삼각수 > 1부터 n까지의 합
def triangle_number(n):
    if n == 1:
        return 1
    return n + triangle_number(n - 1)


for i in range(1, 11):
    print(triangle_number(i))


# n의 각 자릿수의 합을 return 해주는 함수
def sum_digits(n):
    num = str(n)
    # print(n[0])
    # print(int(num[0]))
    length = len(num)
    # print("len: ", length)
    if length == 1:
        return n
    return (int(num[0])) + int(sum_digits(num[1:]))


# 2번
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# 리스트 뒤집기 >> O(n^2)
def flip(some_list):
    length = len(some_list)
    if length < 2:
        return some_list
    # return [some_list[-1]] + flip(some_list[:-1])
    # 이것도 맞지만 리스트로 다시 만들어야 하는 불편
    # 자동으로 리스트로 만들기
    return some_list[-1:] + flip(some_list[:-1])


# 2번
def flip(some_list):
    minddle_index = len(some_list) // 2
    if len(some_list) == 1:
        return some_list
    return flip(some_list[minddle_index:]) + flip(some_list[:minddle_index])


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


# 이진 탐색 재귀로 구해보기
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
        # print("end", end_index)
    # print("start_index:", start_index, "end_index:", end_index)
    if start_index > end_index:
        return None
    median_index = (start_index + end_index) // 2
    # print("me:", median_index)
    if some_list[median_index] == element:
        # print(some_list[median_index])
        return median_index
    elif some_list[median_index] < element:
        return binary_search(element, some_list, median_index + 1, end_index=end_index)
    else:
        return binary_search(element, some_list)

    # return binary_search(element, some_list, 0, median_index-1) + binary_search(element, some_list[median_index+1:], median_index+1, len(some_list) - 1)
    # return binary_search(element, some_list[:median_index - 1]) + binary_search(element, some_list[median_index + 1])


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
print(binary_search(7, [2, 3, 5, 7, 11]))


# 하노이 탑
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    # move_disk(1, start_peg, end_peg)
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)


hanoi(3, 1, 3)


# 카드 뭉치 최대 조합
def max_product(left_cards, right_cards):
    max_num = 0
    for i in left_cards:
        for j in right_cards:
            if i * j > max_num:
                max_num = i * j
    return max_num


def max_product(left_cards, right_cards):
    max_num = 0
    for i in left_cards:
        for j in right_cards:
            max_num = max(max_num, i * j)
    return max_num


print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    num = 1
    min_num = 100
    for i in coordinates:
        for j in coordinates[num:]:
            dis = distance(i, j)
            if min_num > dis:
                min_num = dis
                output = [i, j]
        num += 1
    return output


test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


# 강남역 폭우
def trapping_rain(buildings):
    max_num = 0


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# 1부터 n까지 더하는 함수
def consecutive_sum(start, end):
    median_num = (start + end) // 2
    # print("median:", median_num, "start", start)
    if median_num == start and median_num == end:
        ## if start == end:
        return start
    return consecutive_sum(start, median_num) + consecutive_sum(median_num + 1, end)


print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

"""
def merge(list1, list2):
    length_1 = len(list1)
    length_2 = len(list2)
    if length_1 <= 1 and length_2 <= 1:
        output = []
        for i in length_1:
            for j in length_2:
                if i<j:
                    output.append(i)
                    break
                elif j<i:
                    output.append(j)
                    break
        return output
    if length_1 <= 1 and length_2 <= 1:
        return
    median_1 = length_1 // 2
    median_2 = length_2 // 2
    return merge()
"""


# merge
def merge(list1, list2):
    i = 0
    j = 0

    output_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            output_list.append(list2[j])
            j += 1
        else:
            output_list.append(list1[i])
            i += 1
    if i == len(list1):
        output_list += list2[j:]
    elif j == len(list2):
        output_list += list1[i:]
    return output_list


print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))


# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    median = len(my_list) // 2
    # if len(my_list) <= 2:
    #    return merge(my_list[:median], my_list[median:])
    if len(my_list) < 2:
        return my_list
    output1 = merge_sort(my_list[:median])
    output2 = merge_sort(my_list[median:])
    return merge(output1, output2)


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p = my_list[end]
    i, b = start, start
    for index in range(start, end):
        # while i < end:
        #    if my_list[i] > p:
        if my_list[index] > p:
            i += 1
        else:
            swap_elements(my_list, i, b)
            i += 1
            b += 1
    swap_elements(my_list, b, end)

    # 같은 값이 있으면 이렇게 했을 때 p의 index가 섞일 수 있네
    # return my_list.index(p)
    return b


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)


def quicksort(my_list, start, end):
    if end - start < 1:
        return
    p_index = partition(my_list, start, end)
    pivot = my_list[p_index]
    # print("my_list", my_list)
    quicksort(my_list, start, p_index - 1)
    quicksort(my_list, p_index + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)


def quicksort(my_list, start=0, end=None):
    if end is None:  # end == None
        end = len(my_list) - 1
    if end - start < 1:
        return
    p_index = partition(my_list, start, end)
    pivot = my_list[p_index]
    quicksort(my_list, start, p_index - 1)
    quicksort(my_list, p_index + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)  # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)  # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)  # start, end 파라미터 없이 호출
print(list3)


# memoization 방식의 fib_memo
def fib_memo(n, cache):
    if n == 1 or n == 2:
        cache[n] = 1
        return cache[n]
    # fib_memo(n - 1, cache)
    # fib_memo(n - 2, cache)
    if cache.get(n) is None:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        return cache[n]
    return cache[n]


def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))


# tabulation방식 fib
def fib_tab(n):
    cache = {}
    #print(cache)
    for i in range(1, n+1):
        if i < 3:
            cache[i] = 1
        else:
            cache[i] = cache[i-1] + cache[i-2]
        #print("cache: ", cache)
    return cache[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

