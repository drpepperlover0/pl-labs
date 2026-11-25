

def validate_todos(data):
    if type(data) is not list:
        raise ValueError("Корень не является списком")
    seen_ids = set()
    for record in data:
        if type(record) is not dict:
            raise ValueError("Запись не является словарём")
        if "id" not in record:
            raise ValueError("В записи отсутствует ID")
        if type(record["id"]) is not int:
            raise ValueError("Ошибка ID - не целое число")
        if record["id"] <= 0:
            raise ValueError("Ошибка ID - не положительное")
        if record["id"] in seen_ids:
            raise ValueError("Ошибка ID - такой уже существует в базе")
        else:
            seen_ids.add(record["id"])
        if "userId" not in record:
            raise ValueError("В записи отсутствует userId")
        if type(record["userId"]) is not int:
            raise ValueError("Ошибка userId - не целое число")
        if record["userId"] <= 0:
            raise ValueError("Ошибка userId - не положительное")
        if "title" not in record:
            raise ValueError("В записи отсутствует title")
        if type(record["title"]) is not str:
            raise ValueError("Ошибка title - не строка")
        if record["title"].strip() == "":
            raise ValueError("Ошибка title - пустая строка")
        if "completed" not in record:
            raise ValueError("В записи отсутствует completed")
        if type(record["completed"]) is not bool:
            raise ValueError("Ошибка completed - не булевое")


def completion_counts(todos):
    counts = {}
    for record in todos:
        user_id = record["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        completed = record["completed"]
        if completed:
            counts[user_id] += 1
    return counts


def top_users(counts):
    if not counts:
        return []
    max_count = max(counts.values())
    if max_count == 0:
        return []
    leaders = []
    for userId, count in counts.items():
        if count == max_count:
            leaders.append(userId)
    return sorted(leaders)

def select_tasks(todos, user_id, parameter=None):
    return [task.copy() for task in todos if task['userID'] == user_id and task['userID'] % 2 != 0]
