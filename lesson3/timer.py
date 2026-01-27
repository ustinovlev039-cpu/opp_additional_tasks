"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

import time


class Timer:

    def __enter__(self):
        self.start = time.perf_counter()
        self.elapsed_time = 0.0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed_time = self.end - self.start
        print(f"Executed time {self.elapsed_time}")
        return False





if __name__ == "__main__":
    with Timer() as timer:
        # блок кода

    # код для проверки
        print("Execution time:", timer.elapsed_time)



