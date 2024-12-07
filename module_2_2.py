first = int(input('Введите целое число:'))
ssecond = int(input('Введите целое число:'))
third = int(input('Введите целое число:'))
if first  == ssecond and first == third and ssecond == third:
    print(3)
elif first  == ssecond :
    print(2)
elif first  == third :
    print(2)
elif ssecond  == third :
    print(2)
else:
    print("Данные числа не равны между собой")