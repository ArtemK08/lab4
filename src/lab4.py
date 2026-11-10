import re
from collections import Counter
import datetime

#  Функції для базових операцій з рядками

def find_substring(text, substring):

    #Пошук підрядка в тексті.Повертає індекс першого входження або -1, якщо підрядок не знайдено.

    return text.find(substring)

def replace_substring(text, old, new):

    #Заміна підрядка в тексті.

    return text.replace(old, new)

def split_text(text, delimiter=' '):

    #Розділення тексту за роздільником.

    return text.split(delimiter)

def format_string_f(name, age):
    #Форматування рядка з використанням f-string.

    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    #Форматування рядка з використанням методу .format().

    return "Мене звати {} і мені {} років.".format(name, age)


#  Функції для роботи з регулярними виразами

def extract_emails(text):

    #Витяг email адрес з тексту.

    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def validate_phone_number(number):

    #Валідація українського телефонного номера або специфічного формату.


    # Підтримуємо стандартний український формат +380xxxxxxxxx або формат з тексту
    pattern = r'^\+380\d{9}$|^\+\d{4}-\d{3}-[A-Z-]+$'
    return bool(re.match(pattern, number))

def extract_hashtags(text):

    #Витяг хештегів з тексту.

    pattern = r'#\w+'
    return re.findall(pattern, text)

def extract_mentions(text):

    #Витяг згадувань користувачів з тексту (напр. @user).

    pattern = r'@\w+'
    return re.findall(pattern, text)


#  Функції для аналізу тексту

def count_words(text):
    #Підрахунок кількості слів у тексті.

    # Знаходимо всі слова (ігноруючи знаки пунктуації)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    #Підрахунок кількості речень у тексті.

    # Розбиваємо за знаками кінця речення (. ! ?)
    sentences = re.split(r'[.!?]+', text)
    # Фільтруємо порожні елементи
    valid_sentences = [s.strip() for s in sentences if s.strip()]
    return len(valid_sentences)

def word_frequency(text):
    #Підрахунок частоти слів у тексті.Повертає об'єкт Counter.

    # Приводимо до нижнього регістру для коректного підрахунку
    words = re.findall(r'\b[а-яА-Яа-яіієюєїґҐa-zA-Z]+\b', text.lower())
    return Counter(words)

def analyze_text(text):

    #Комплексний аналіз тексту.
    #Повертає словник з результатами аналізу.

    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'word_frequency': word_frequency(text),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text),
        'mentions': extract_mentions(text)
    }

def format_analysis_results(results):

    #Форматування результатів аналізу.

    output = "=== Результати аналізу тексту NeoTerra 3000 ===\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n"
    output += f"Знайдені Email-адреси: {', '.join(results['emails']) if results['emails'] else 'Немає'}\n"
    output += f"Знайдені хештеги: {', '.join(results['hashtags']) if results['hashtags'] else 'Немає'}\n"
    output += "\nТоп-5 найчастіших слів:\n"
    for word, count in results['word_frequency'].most_common(5):
        output += f"  - {word}: {count} разів(а)\n"
    return output


#  Функція для вилучення даних за варіантом

def extract_variant_data(text, variant_pattern):

    #Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    #Для вилучення моделей термоядерних реакторів (наприклад, FR-1000).

    return re.findall(variant_pattern, text)


# Головна частина програми

def read_file_content(filepath):
    #Читає вміст файлу.

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    #Головна функція, що керує виконанням програми.

    print("Ласкаво просимо до аналізатора тексту!")

    text_filepath = 'data/neoterra_text.txt'

    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом (Моделі реакторів)")
            print("4. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації (наприклад, +380671234567): ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                # Патерн для пошуку моделей термоядерних реакторів типу FR-1000
                reactor_pattern = r'\b[A-Z]{2}-\d{3,4}\b'
                variant_data = extract_variant_data(text_to_analyze, reactor_pattern)
                print(f"Знайдені моделі термоядерних реакторів: {variant_data}")

            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()
