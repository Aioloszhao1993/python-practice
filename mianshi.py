def sum_time(time_list):
    sum = 0
    num_list = []
    for i in range(len(time_list)):
        num1 = time_list[i]
        for num2 in time_list[i + 2:]:
            if sum < num1 + num2:
                sum = num1 + num2
        num_list.append(sum)
        sum = 0
    max_num = 0
    for num in num_list:
        if max_num < num:
            max_num = num
    return max_num


if __name__ == "__main__":
    time_list = [1, 2, 3, 1, 7]
    max_num = sum_time(time_list)
    print("max_num:%s" % max_num)




