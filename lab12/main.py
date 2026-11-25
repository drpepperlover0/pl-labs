import json
from pathlib import Path

import logic
import storage

folder = Path(__file__).resolve().parent
data_path = folder / "data.json"

def show_menu():
    print("\n~~~ Меню ~~~")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")

def show_records(records):
    if not records:
        print("Нет записей")
        return
    sorted_records = sorted(records, key=lambda r: r["id"])
    for record in sorted_records:
        status = 'Выполнено' if record["completed"] else 'Не выполнено'
        print(f"ID: {record['id']} | {record['title']} | Категория: {record['category']} | Участников: {record['amount']} | Статус: {status}")

def add_record_ui(records):
    while True:
        title = input("Введите название: ").strip()
        if title:
            break
        print("Ошибка, название не должно быть пустым!")
    while True:
        category = input("Введите категорию: ").strip()
        if category:
            break
        print("Ошибка, категория не должна быть пустой!")
    while True:
        try:
            amount = int(input("Введите количество участников: "))
            if amount >= 0:
                break
            print("Ошибка, число должно быть больше либо равно нуля!")
        except ValueError:
            print("Ошибка: введите целое число!")
    new_record = logic.add_record(records, title, category, amount)
    print(f"Запись добавлена! ID: {new_record['id']}")

def find_records_ui(records):
    while True:
        request = input("Введите строку: ").strip()
        if request:
            break
        print("Строка не должна быть пустой!")
    found = logic.find_records(records, request)
    if not found:
        print("Ничего не найдено")
        return
    for record in found:
        status = 'Выполнено' if record["completed"] else 'Не выполнено'
        print(
            f"ID: {record['id']} | {record['title']} | Категория: {record['category']} | Участников: {record['amount']} | Статус: {status}")

def set_completed_ui(records):
    while True:
        chosen_id = input("Введите ID: ")
        try:
            chosen_id=int(chosen_id)
            if chosen_id > 0:
                break
            print("Ошибка, введено не положительное число!")
        except ValueError:
            print("Ошибка, введите целое число!")
    while True:
        chosen_status = input("Отметить как выполненную? (да/нет): ").lower()
        if chosen_status == 'да':
            completed = True
            break
        elif chosen_status == 'нет':
            completed = False
            break
        else:
            print("Ошибка, неизвестная команда!")
    success = logic.set_completed(records, chosen_id, completed)
    if success:
        print(f"Статус записи {chosen_id} успешно изменён!")
    else:
        print(f"Ошибка, записи с ID {chosen_id} не существует!")

def delete_record_ui(records):
    while True:
        chosen_id = input("Введите ID: ")
        try:
            chosen_id = int(chosen_id)
            if chosen_id > 0:
                break
            print("Ошибка, введено не положительное число!")
        except ValueError:
            print("Ошибка, введите целое число!")
    confirmation = input(f"Вы уверены, что хотите удалить запись с ID {chosen_id}? (да/нет): ").lower().strip()
    if confirmation == 'да':
        success = logic.delete_record(records, chosen_id)
        if success:
            print(f"Запись с ID {chosen_id} успешно удалена!")
        else:
            print(f"Ошибка, записи с ID {chosen_id} не существует!")
    else:
        print("Удаление отменено!")
        return

def show_statistics_ui(records):
    stats = logic.statistics(records)
    print('\n---Статистика---')
    print(f"Всего записей: {stats['total']}")
    print(f"Выполнено: {stats['completed']}")
    print(f"Не выполнено: {stats['not_completed']}")
    print(f"Общее количество участников: {stats['total_amount']}")
    if stats['by_category']:
        print('Суммы по категориям:')
        for category, amount in stats['by_category'].items():
            print(f' {category}: {amount}')

def save_records_ui(records):
    try:
        storage.save_records(data_path, records)
        print("Данные успешно сохранены!")
        return True
    except OSError:
        print("Ошибка, не удалось сохранить данные!")
        return False

def main():
    try:
        records = storage.load_records(data_path)
    except FileNotFoundError:
        print("Файл data.json не найден. Начинаем с пустого списка!")
        records = []
    except json.JSONDecodeError:
        print("Ошибка в формате JSON-файла!")
        return
    except UnicodeError:
        print("Ошибка Unicode декодирования!")
        return
    except ValueError as e:
        print(f"Ошибка формата данных - {e}!")
        return
    except OSError:
        print("Ошибка в чтении файла!")
        return
    else:
        print(f"Данные успешно загружены. Записей: {len(records)}")

    while True:
        show_menu()
        choice = input("Введите номер команды (1-8): ")
        try:
            choice = int(choice)
        except ValueError:
            print("Ошибка, не целое число!")
            continue
        else:
            if choice not in range(1,9):
                print("Ошибка, число вне указанного диапазона!")
                continue
            elif choice == 1:
                show_records(records)
            elif choice == 2:
                add_record_ui(records)
            elif choice == 3:
                find_records_ui(records)
            elif choice == 4:
                set_completed_ui(records)
            elif choice == 5:
                delete_record_ui(records)
            elif choice == 6:
                show_statistics_ui(records)
            elif choice == 7:
                save_records_ui(records)
            else:
                ask = input("Сохранить данные перед выходом? (да/нет): ").lower().strip()
                if ask == 'да':
                    saved = save_records_ui(records)
                    if saved:
                        print("Выход из программы...")
                        break
                    else:
                        print("Сохранение не выполнено. Вы остаётесь в меню.")
                elif ask == 'нет':
                    print("Выход без сохранения...")
                    break
                else:
                    print("Ошибка, введите 'да' или 'нет'!")
                    continue




if __name__ == "__main__":
    main()