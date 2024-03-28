data = [5, -2, 10, 3, 0, 8, -4, 7]

def sort_data(data: list) -> list:
    n = len(data)
    if sum(data) / n > 0:
        first_third = sorted(data[:2 * n // 3])
        rest = data[2 * n // 3:][::-1]
        return first_third + rest

    else:
        first_third = sorted(data[:n // 3])
        rest = data[n // 3:][::-1]
        return first_third + rest

sorted_data = sort_data(data)

print(sorted_data)