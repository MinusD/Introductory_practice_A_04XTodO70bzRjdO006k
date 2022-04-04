# В классе 6 столов. На первом столе 1 яблоко, на втором - 2 яблока, на третьем - 3 и так далее.
# Дети входят в класс по одному. Они должны сесть за тот стол, за которым они получают больше всего шоколада. 
# Если есть выбор между двумя столами, они предпочтут сесть за стол, ближайший к двери 
# (первый стол - самый близкий, а шестой - самый дальний от двери).
# Написать функцию apple_share(n), которая для заданного числа детей n вернет список, показывающий, 
# сколько детей сидит за каждым столом. 
#  
# Пример
# apple_share(10) ==> [0, 1, 1, 2, 3, 3] 
# Ребенок 1 садится за стол 6 (6 яблок). Ребенок 2 садится за стол 5 (5 яблок).
# Ребенок 3 садится за стол 4 (4 яблока). Ребенок 4 садится за стол 3 (3 яблока).
# Ребенок 5 садится за стол 6 (двое по 3 яблока). Ребенок 6 садится за стол 5 (двое по 2.5 яблока)
# Ребенок 7 садится за стол 2 (2 яблока). Ребенок 8 садится за стол 4 (двое по 2 яблока).
# Ребенок 9 садится за стол 6 (трое по 2 яблока). Ребенок 10 садится за стол 5 (трое по 1 и 2/3 яблока)


import traceback


def apple_share(n):
    tables_data = [0, 0, 0, 0, 0, 0]  # В списке хранится количество детей за определённым столиком
    how_get = [1, 2, 3, 4, 5, 6]  # Храним сколько получит каждый ребёнок, если ещё один сядет за определённый стол
    for i in range(n):
        current_max = max(how_get)  # Сколько максимум может получит следующий ребёнок
        # Так как если ребёнок получит одинаковое кол-во на двух столах, нам нужно выбрать первый стол
        for j in range(6):
            if how_get[j] == current_max:
                tables_data[j] += 1  # Записываем, куда сел ребёнок
                how_get[j] = (j + 1) / (tables_data[j] + 1)
                break  # Как нашли, выходим из цикла
        '''Обновляем информацию о столе, куда только что сел ребёнок, что бы узнать, 
        сколько получит следующий ребёнок, нам нужно узнать, сколько яблок лежит на столе, а это индекс + 1
        и делим это на (число уже сидящих за столом + 1)
        '''


    return tables_data


# Тесты
try:
    assert apple_share(1) == [0, 0, 0, 0, 0, 1]
    assert apple_share(4) == [0, 0, 1, 1, 1, 1]
    assert apple_share(10) == [0, 1, 1, 2, 3, 3]
    assert apple_share(50) == [2, 5, 7, 10, 12, 14]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
