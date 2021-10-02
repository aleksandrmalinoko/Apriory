import csv
import random


tehno_list = ["Номер транзакции", "холодильник", "микроволновка", "пылесос", "гриль",
              "посудомойка", "плита", "телевизор", "миксер", "утюг"]
my_data = []
for _ in range(30):
    zero_one_list = [1, 1, 1, 1, 1, 0, 0, 0, 0]
    random.seed(_)
    random.shuffle(zero_one_list)
    zero_one_list.insert(0, _)
    my_data.append(zero_one_list)
print(my_data)
with open("dataset.csv", 'w') as dataset:
    writer = csv.writer(dataset)
    writer.writerow(tehno_list)
    writer.writerows(my_data)
