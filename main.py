# main.py

import os
import shutil

from preprocessing.prepreprocess import preprocess_images
from classification.categorize_images import categorize_images
from analysis.analyze_surface import analyze_surface


# Пути к папкам
PROCESSED_DIR = os.path.join("data", "processed")
ROAD_ONLY_DIR = os.path.join(PROCESSED_DIR, "road_only")
SIDEWALK_ONLY_DIR = os.path.join(PROCESSED_DIR, "sidewalk_only")
ROAD_AND_SIDEWALK_DIR = os.path.join(PROCESSED_DIR, "road_and_sidewalk")
REJECTED_DIR = os.path.join("data", "rejected")



def clear_folder(folder_path):
    """Удаляет все файлы из указанной папки, не трогая саму папку."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Удаляем файл или ссылку
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Удаляем вложенную папку
        except Exception as e:
            print(f'Не удалось удалить {file_path}. Ошибка: {e}')

def clear_processed_folders():
    """Очищает папки 'road_only', 'sidewalk_only' и 'road_and_sidewalk'."""
    print("Очистка папок 'road_only', 'sidewalk_only', 'road_and_sidewalk'...")
    clear_folder(ROAD_ONLY_DIR)
    clear_folder(SIDEWALK_ONLY_DIR)
    clear_folder(ROAD_AND_SIDEWALK_DIR)
    clear_folder(PROCESSED_DIR)
    clear_folder(REJECTED_DIR)
    print("Очистка завершена.")



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
    clear_processed_folders()






