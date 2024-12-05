import numpy as np

def random_predict(number: int=1) -> int:
    """Компьютер угадывает число

    Args:
        number (int, optional): Загаданное число. (По умолчанию 1)

    Returns:
        int: Количество попыток
    """
    count = 0 
    minimal, maximal = 1, 101 
    random_int = np.random.randint(minimal,maximal) #генерируем рандомное число
    
    while True:
        count +=1
        # если рандомное число больше загаданного, то граница максимального числа изменяется и создается новое рандомное число
        if random_int > number:
            maximal = random_int
            random_int = np.random.randint(minimal,maximal)
        # если рандомное число меньше загаданного, то граница минимального числа изменяется и создается новое рандомное число
        elif random_int < number:
            minimal = random_int
            random_int = np.random.randint(minimal,maximal)
        # в противном случае возвращаем количество попыток
        else:
            return count

def score_game(random_predict) -> int:
    """Подсчитать среднее количество попыток за 1000 раз

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Количество попыток в среднем
    """
    np.random.seed(1)
    counts = []
    rand_ints = np.random.randint(1,101, size=(1000)) #генерируем рандомное число
    # добавляем количество попыток в список
    for number in rand_ints:
        counts.append(random_predict(number))
    # высчитываем среднее число
    score = int(np.mean(counts))
    return score
    
if __name__ == "__main__":
    print(score_game(random_predict))


