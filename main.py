# main.py

from preprocessing.prepreprocess import preprocess_images
from classification.categorize_images import categorize_images
from analysis.analyze_surface import analyze_surface



def main():
    print("Запуск проекта по анализу дорожных покрытий")
    print("=" * 40)

    # 1. Запуск модуля предобработки фотографий
    print("[Главный модуль] Запуск предобработки фотографий...")
    preprocess_images()  # В этом модуле создаются папки processed и rejected

    # 2. Запуск модуля классификации фотографий
    print("[Главный модуль] Запуск классификации фотографий...")
    categorize_images()  # Используются только фотографии из папки processed

    # 3. Запуск модуля анализа покрытия
    print("[Главный модуль] Запуск анализа покрытия...")
    analyze_surface()

    print("=" * 40)
    print("Код проекта по анализу дорожных покрытий завершил работу")


if __name__ == "__main__":
    main()
