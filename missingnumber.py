def missing_number_list(list1):
    missing_values_list=list()
    for i in range(1,10):
        if i not in list1:
            missing_values_list.append(i)

    return missing_values_list


if __name__ == '__main__':
    list1=[ 1, 2, 3, 5, 6, 7,9]
    print(missing_number_list(list1))





        