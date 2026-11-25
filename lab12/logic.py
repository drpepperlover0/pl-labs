def validate_records(records):
    if type(records) is not list:
        raise ValueError("Корень записей не является списком!")
    set_id = set()
    for record in records:
        if type(record) is not dict:
            raise ValueError("Ошибка в типе данных, записи не являются словарями!")
        for test in ["id", "title", "category", "amount", "completed"]:
            if test not in record:
                raise ValueError(f"Ошибка, отсутсвует значение {test}!")
        if type(record["id"]) is not int:
            raise ValueError("Ошибка, id не целое число!")
        if record["id"] <= 0:
            raise ValueError("Ошибка, id не положительное число!")
        if record["id"] in set_id:
            raise ValueError("Ошибка, такой id уже существует!")
        else:
            set_id.add(record["id"])
        if type(record["title"]) is not str:
            raise ValueError("Ошибка, title не является строкой!")
        if record["title"].strip() == '':
            raise ValueError("Ошибка, title - пустая строка!")
        if type(record["category"]) is not str:
            raise ValueError("Ошибка, category не является строкой!")
        if record["category"].strip() == '':
            raise ValueError("Ошибка, category - пустая строка!")
        if type(record["completed"]) is not bool:
            raise ValueError("Ошибка, completed не является булевым!")
        if type(record["amount"]) is not int:
            raise ValueError("Ошибка, amount не целое число!")
        if record["amount"] < 0:
            raise ValueError("Ошибка, amount отрицательное!")

def add_record(records, title, category, amount):
    title = title.strip()
    category = category.strip()
    id = max([record["id"] for record in records], default=0) + 1
    record = {"id" : id, "title": title, "category": category, "amount": amount, "completed": False}
    records.append(record)
    return record

def find_records(records, query):
    if query.strip() == '':
        raise ValueError("Ошибка, запрос пустой!")
    result = []
    for record in records:
        if query.lower() in record["title"].lower():
            result.append(record)
    return result

def set_completed(records, record_id, completed):
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False

def delete_record(records, record_id):
    for i, record in enumerate(records,0):
        if record["id"] == record_id:
            del records[i]
            return True
    return False

def statistics(records):
    total = len(records)
    completed = sum([1 for r in records if r["completed"] == True])
    not_completed = total - completed
    total_amount = sum([r["amount"] for r in records])
    by_category = {}
    for record in records:
        new_sum = by_category.get(record["category"], 0) + record["amount"]
        by_category[record["category"]] = new_sum
    return {
        "total": total,
        "completed": completed,
        "not_completed": not_completed,
        "total_amount": total_amount,
        "by_category": dict(sorted(by_category.items()))
    }