def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    level = 1
    x = 0
    y = 0
    last_add = 'y'
    for i in range(10):
        for j in range(len(input_list)):
            if input_list[j] == i:
                if last_add == 'y':
                    x += i * level
                    last_add = 'x'
                else:
                    y += i * level
                    last_add = 'y'
                    level *= 10

    print(f'x = {x}; y = {y}')
    return(x, y)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])