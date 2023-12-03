'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import random

# Пример данных
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

# Создание множества уникальных меток
unique_labels = set(lst)

# Создание словаря для хранения one-hot кодировки
one_hot_encoding = {label: [(1 if value == label else 0) for value in lst] for label in unique_labels}

# Вывод one-hot кодировки
for label, encoding in one_hot_encoding.items():
    print(f'{label}: {encoding}')