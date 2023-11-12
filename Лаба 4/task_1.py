import json


# TODO решите задачу
def task() -> float:
    summ = 0
    with open('input.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        for i in range(len(text)):
            summ += (text[i]['score'] * text[i]['weight'])
    return round(summ, 4)


print(task())
