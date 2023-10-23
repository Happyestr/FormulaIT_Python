# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, sep=','):
    return sorted(set(participants_first_group.split(sep)).intersection(participants_second_group.split(sep)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
