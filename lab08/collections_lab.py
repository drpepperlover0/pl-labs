def word_counts(text):
    words = text.lower().split()
    result = {}
    for word in words:
        word = word.strip(".,!?;:")
        if not word:
            continue
        result[word] = result.get(word, 0) + 1
    return result


def alphabet_sorted(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    result = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        result[category] = result.get(category, 0) + amount
    return result


def titles_in_category(records, category):
    result = []
    for record in records:
        if record['category'] == category:
            result.append(record['title'])
    return result


def get_sorted(records):
    totals = totals_by_category(records)
    result = list(totals.items())
    return sorted(result, key=lambda x: (-x[1], x[0]))
