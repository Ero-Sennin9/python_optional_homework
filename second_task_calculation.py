import random

import matplotlib.pyplot as plt
import pandas as pd
from benchmark_calculation import benchmark_calculation
import matplotlib
matplotlib.use('TkAgg')

import sys
import platform

def get_system_info():
    return {
        "Python Version": sys.version,
        "Python Implementation": platform.python_implementation(),
        "System": platform.system(),
        "Release": platform.release(),
        "Processor": platform.processor(),
        "Machine": platform.machine()
    }
def test_methods(number):
    benchmark_results = benchmark_calculation(number)

    with open("benchmark_calculation_results_for_plot.txt", "w") as f:
        # Запись результатов для графика
        for name, time in benchmark_results.items():
            f.write(f"{name},{time}\n")

    with open("benchmark_calculation_results.txt", "w") as f:
        # Запись результатов
        f.write("Результаты:\n")
        for name, time in benchmark_results.items():
            f.write(f"{name},{time}\n")

        # Запись системной информации
        f.write("\nСистемная информация:\n")
        for key, value in get_system_info().items():
            f.write(f"{key}: {value}\n")


def plot_results():
    data = pd.read_csv("benchmark_calculation_results_for_plot.txt", header=None, names=["Method", "Time"])

    data = data.sort_values("Time", ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(data["Method"], data["Time"], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
            f'{height:.2f} сек',
            ha='center', va='bottom')

    plt.title(f"Сравнение методов парсинга (Факторизация большого числа)", fontsize=14)
    plt.xlabel("Метод", fontsize=12)
    plt.ylabel("Время выполнения (сек)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("benchmark_parsing_results.png")
    plt.show()


if __name__ == "__main__":
    number1 = random.randint(10 ** 9, 10 ** 10)
    number2 = random.randint(10 ** 9, 10 ** 10)
    number = number1 * number2
    test_methods(number)
    plot_results()