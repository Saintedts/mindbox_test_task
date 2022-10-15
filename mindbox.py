def sum_of_digs(n):
    s = 0

    while n > 0:
        digit = n % 10
        s = s + digit
        n = n // 10

    return s

def groups_qty_from_zero(n_customers):
    result_dict = {}

    for i in range(0, n_customers):
        i_dig_sum = sum_of_digs(i)

        res_from_dict = result_dict.get(i_dig_sum)
        if res_from_dict is None:
            result_dict[i_dig_sum] = 1
        else:
            result_dict[i_dig_sum] += 1

    return result_dict

def groups_qty_from_n(n_first_id, n_customers):
    result_dict = {}

    for i in range(n_first_id, n_customers):
        i_dig_sum = sum_of_digs(i)

        res_from_dict = result_dict.get(i_dig_sum)
        if res_from_dict is None:
            result_dict[i_dig_sum] = 1
        else:
            result_dict[i_dig_sum] += 1

    return result_dict

print(groups_qty_from_zero(15))
print(groups_qty_from_n(0, 15))