"""Угадай число
Компьютер сам загадывает и угадывае число"""
import numpy as np 
def random_predict(number:int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predick_number = np.random.randint(1,101)
        if number == predick_number:
            break
    return(count)
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм


    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = [] #Список для сохранения количества потыток
    np.random.seed(1) # Фиксирует сид для воспроизводительности
    random_array = np.random.randint(1,101, size = (1000)) # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # Находим среднее количество потыток
    print(f'Ваш алгоритм угадывает число за {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)