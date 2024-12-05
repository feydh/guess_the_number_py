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
    random_int = np.random.randint(minimal,maximal)
    
    while True:
        count +=1
        
        if random_int > number:
            maximal = random_int
            random_int = np.random.randint(minimal,maximal)
        elif random_int < number:
            minimal = random_int
            random_int = np.random.randint(minimal,maximal)
        else:
            return count

def score_game(random_predict) -> int:
    """Подсчитать среднее количество попыток за 1000 раз

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Количество попыток в среднем
    """
    np.random.seed(1) #нужен ли он здесь?
    counts = []
    rand_ints = np.random.randint(1,101, size=(1000))
    
    for number in rand_ints:
        counts.append(random_predict(number))
        
    score = int(np.mean(counts))
    return score
    
if __name__ == "__main__":
    print(score_game(random_predict))


