#**Игра "Угадай число"**
#Компьютер сам загадывает и сам угадывает число
import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,101) #загаданное число в диапазоне от 1 до 100 
        if number == predict_number:
            break #выход из цикла, если число угадали 
    return count
print(f'Количество попыток {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в срденем из 1000 подходов угадывает алгоритм

    Args:
        random_predict (_type_): Функция угадвания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []  #список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадывваем список чисел 
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))  #находим среднее количество попыток
    
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return (score)

if __name__ == '__main__':
    score_game(random_predict) #RUN