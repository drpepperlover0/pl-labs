from collections_lab import *

if __name__ == "__main__":
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}

    counts = word_counts("Python, python! SQL, git, git")
    alphabet_sorted(counts)
    print()

    assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
    assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
    assert common_topics([], ["sql", "git"]) == []
    assert all_topics([], ["sql", "git"]) == ["git", "sql"]

    table = {'title': 'Python', 'hours': 66}
    table['hours'] = 67
    table['completed'] = False
    data = (table['title'], table['hours'])
    title, hours = data
    print(f"title = {title}")
    print(f"hours = {hours}")
    print()

    records = [
        {"title": "Монополия", "category": "стратегия", "amount": 4},
        {"title": "Шахматы", "category": "логика", "amount": 2},
        {"title": "Мафия", "category": "командная", "amount": 8},
        {"title": "Уно", "category": "стратегия", "amount": 6},
        {"title": "Дженга", "category": "логика", "amount": 4},
    ]

    orig = [r.copy() for r in records]

    assert totals_by_category(records) == {"стратегия": 10, "логика": 6, "командная": 8}
    assert totals_by_category([]) == {}
    assert titles_in_category(records, "стратегия") == ["Монополия", "Уно"]
    assert titles_in_category(records, "нет") == []
    assert titles_in_category([], "стратегия") == []
    assert records == orig
    
    expected_sorted = [("стратегия", 10), ("командная", 8), ("логика", 6)]
    assert get_sorted(records) == expected_sorted
    
    totals = totals_by_category(records)
    print("Сводка по категориям (по алфавиту):")
    for category in sorted(totals):
        print(f"  {category}: {totals[category]}")

    user_category = input("\nВведите категорию: ").strip().lower()
    found_titles = titles_in_category(records, user_category)

    if found_titles:
        print(f"Найдены задания в '{user_category}': {found_titles}")
    else:
        print(f"В '{user_category}' ничего не найдено ([]).")

    print("\nВсе проверки пройдены!!!")