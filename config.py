# config.py

# Конфигурационный файл с указанием основных директорий и параметров
import os

# Пути к основным папкам
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Корневая директория проекта
DATA_DIR = os.path.join(BASE_DIR, "data")  # Папка с данными

# Пути к папкам с фотографиями
RAW_DIR = os.path.join(DATA_DIR, "raw")  # Папка с исходными фотографиями
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")  # Принятые фотографии (после предобработки)
REJECTED_DIR = os.path.join(DATA_DIR, "rejected")  # Отклоненные фотографии (размытые и т.д.)
RESULTS_DIR = os.path.join(DATA_DIR, "results")  # Папка для финальных результатов анализа

# Пути для хранения фотографий после модуля классификации
ROAD_ONLY_DIR = os.path.join(PROCESSED_DIR, "road_only")  # Фото только с дорогой
SIDEWALK_ONLY_DIR = os.path.join(PROCESSED_DIR, "sidewalk_only")  # Фото только с тротуаром
ROAD_AND_SIDEWALK_DIR = os.path.join(PROCESSED_DIR, "road_and_sidewalk")  # Фото с дорогой и тротуаром

# Параметры для предобработки
PREPROCESS_ACCEPTANCE_RATE = 0.8  # Процент принятия фотографий (имитация)

# Параметры для классификации
CLASSIFICATION_THRESHOLD = 0.5  # Порог уверенности для классификации (значение от 0 до 1)
