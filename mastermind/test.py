def count_common_elements(list1, list2):
    count = 0
    same_position = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and i != j:
                count += 1
                break
            elif list1[i] == list2[j] and i == j:
                same_position += 1
                break
    return count, same_position