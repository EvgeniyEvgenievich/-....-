def calculate_structure_sum(data):
    total_amount = 0
    for elements in data:
        if isinstance(elements, (int, float)):
            total_amount += elements
        elif isinstance(elements, (list, tuple, set)):
            total_amount += calculate_structure_sum(elements)
        elif isinstance(elements, str):
            total_amount += len(elements)
        elif isinstance(elements, dict):
            for key, value in elements.items():
                total_amount += calculate_structure_sum([key, value])

    return total_amount


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)