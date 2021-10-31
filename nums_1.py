nums = list(map(int, input('Введите числа: ').split()))
def find_missing_nums(nums):
    n = len(nums)
    c = []
    for i in nums:
        if i > len(nums):
            print('Вы должны были ввести список с числами, значение каждого'
                  ' из которых было бы меньше или равно длине списка')
            return
    for i in range(1, len(nums) + 1):
        if i not in nums:
            c.append(i)
    if c != []:
        print('Недостающие числа ',c)
    else:
        print('Нечего добавлять, недостающих чисел нет')
find_missing_nums(nums)
