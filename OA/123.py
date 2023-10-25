from typing import Optional, List
from collections import deque


def special_data_table(number_of_slots, values, find_item):
    ####### DO NOT MODIFY BELOW #######
    myTable = MySpecialTable(number_of_slots)
    for val in values:
        myTable.add_item(val)

    return myTable.find_item(find_item)


####### DO NOT MODIFY ABOVE #######

class MySpecialTable():
    def __init__(self, slots):
        self.slots = slots
        self.table = []
        self.create_table()

    def hash_key(self, value):
        key = value % self.slots
        return key

    def create_table(self):
        for i in range(self.slots):
            self.table.append(set())


    def add_item(self, value):
        k = self.hash_key(value)
        self.table[k].append(value)
        return

    def find_item(self, item):
        k = self.hash_key(item)
        if item in self.table[k]:
            return k
        else:
            return -1


if __name__ == '__main__':
    sol = MySpecialTable(3)
