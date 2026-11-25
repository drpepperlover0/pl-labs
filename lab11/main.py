import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, select_tasks


def main():
    folder = Path(__file__).resolve().parent
    todos_json = folder / "todos.json"
    try:
        with open(todos_json, 'r', encoding='utf-8') as file:
            todos = json.load(file)
        validate_todos(todos)
    except FileNotFoundError:
        print("Файл не найден")
    except UnicodeError:
        print("Ошибка в кодировке")
    except json.JSONDecodeError:
        print("Ошибка в формате JSON файла")
    except ValueError as err:
        print(f"Ошибка структуры данных: {err}")
    except OSError:
        print("Ошибка доступа")
    else:
        counts = completion_counts(todos)
        leaders = top_users(counts)
        leaders_tasks = []
        print("Количество выполненных задач по пользователям:", counts)
        print("Лидеры:", leaders)
        for record in todos:
            if record["userId"] in leaders and record["completed"] is True:
                leaders_tasks.append(record)
        leaders_path = folder / "leaders.json"
        with open(leaders_path, 'w', encoding='utf-8') as file:
            json.dump(leaders_tasks, file, ensure_ascii=False, indent=2)
        while True:
            try:
                user_id = int(input("Введите user_id (целое, положительное): "))
                if user_id > 0:
                    break
            except ValueError:
                print("Ошибка ввода данных!")
            else:
                print("Введено не положительное число!")
        select_json = folder / "selected.json"

        with open(select_json, "w", encoding="utf-8") as file:
            json.dump(select_tasks(todos, user_id), file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
