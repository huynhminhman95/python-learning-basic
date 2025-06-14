# tinh luy thua cua 1 so
# 2^3 = 8
# 3^2 = 9
# print(2**3) cach tinh luy thua

def calculate_power(base_number, exponent):
    result = 1
    for index in range(exponent):
        result = result * base_number
        # base_number = 2, exponent = 3
        # 1 * 2 = 2
        # 2 * 2 = 4
        # 4 * 2 = 8
    return result

print(calculate_power(3, 3))