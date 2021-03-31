import numpy as np


def game_core_custom(number):
    """Ищем искомое число методом бисекции"""
    count = 0
    segment_start = 1
    segment_end = 100
    while True:
        count += 1
        predict = segment_end - (segment_end - segment_start) // 2
        if predict == number:
            return count
        elif predict > number:
            segment_end = predict - 1
            if segment_start == segment_end:
                return count  # последнее оставшееся число и есть искомый номер
        else:
            segment_start = predict + 1
            if segment_start == segment_end:
                return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed()  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_custom)
