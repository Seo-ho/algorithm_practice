# 선형 탐색 > O(n)
def linear_search(element, some_list):
    i=0
    n = len(some_list)

    while i < n:
        if some_list[i] == element:
            return i
        i += 1
    return -1


# 이진 탐색 > O(lg n)
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


# 선택 정렬 > O(n^2)
def selection_sort(test_list):
    for iteration1 in range(len(test_list) - 1):
        min_index = iteration1
        min_num = test_list[min_index]

        for iteration2 in range((iteration1 + 1), len(test_list)):
            if test_list[iteration2] <= min_num:
                min_index = iteration2
                min_num = test_list[min_index]
        test_list[iteration1], test_list[min_index] = test_list[min_index], test_list[iteration1]
    return test_list


list_text = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(selection_sort(list_text))


# 삽입 정렬 > O(n^2)
def insertion_sort(test_list):
    for index in range(1, len(test_list)):
        for position in range(index, 0, -1):
            if test_list[position - 1] > test_list[position]:
                test_list[position], test_list[position - 1] = test_list[position - 1], test_list[position]
    return test_list


print(insertion_sort([3, 4, 0, 1, 5, 2, 6]))
print(insertion_sort([3, 4, 0, 1, 5, 2, 6]))


# inv가 0이면 오름차순, 1이면 내림차순.
def insert_sorted(some_list, inv):
    # 코드를 작성하세요.
    for i in range(len(some_list)):
        for j in range(i, 0, -1):
            if (some_list[j] < some_list[j - 1]) ^ inv:
                some_list[j], some_list[j-1] = some_list[j-1], some_list[j]
            else:
                break

    return some_list


print(insert_sorted([3, 4, 0, 1, 5, 2, 6], 0))
print(insert_sorted([3, 4, 0, 1, 5, 2, 6], 1))