first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result  = (len(x) - len(y) for x , y in zip(first,second) if len(x) != len(y))
second_result  = (True if len(first[i]) == len(second[i]) else False for i in range(0,max(len(first),len(second))))
# # " Если читать задание дословно ,во 2 пункте "содержит результаты сравнения строк в одинаковых позициях""
# second_result  = (True if first[i] == second[i] else False for i in range(0,max(len(first),len(second))))

print(list(first_result))
print(list(second_result))