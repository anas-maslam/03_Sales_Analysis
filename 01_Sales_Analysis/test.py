def skip_indices(lst):
    index = 0
    skip = 1
    fin_sum = 0

    while index < len(lst):
        fin_sum += lst[index]
        skip += 1
        index += skip
    return fin_sum


if __name__ == '__main__':
    sum_num = skip_indices([1,0,0,3,6,1,0,2,0,1])

    print(sum_num)
