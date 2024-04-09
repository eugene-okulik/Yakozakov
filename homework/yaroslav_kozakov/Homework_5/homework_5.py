# Задача1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задача2
str1 = str('результат операции: 42')
str2 = str('результат операции: 514')
str3 = str('результат операции: 9')

number_str1 = str1[19:]
number_str2 = str2[19:]
number_str3 = str3[19:]

number_str1_new = int(number_str1) + 10
number_str2_new = int(number_str2) + 10
number_str3_new = int(number_str3) + 10

number_result = number_str1_new + number_str2_new + number_str3_new

print(number_result)

# Задача3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students', ', ' .join(students), 'study these subjects:', ', ' .join(subjects))
