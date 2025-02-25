import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data_dict = {}        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        self.data_dict[val] = len(self.data)-1
        self.data.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data_dict:
            return False
        index = self.data_dict[val]
        last_element = self.data[-1]
        self.data[index] = last_element
        self.data_dict[last_element] = index
        self.data.pop()
        del self.data_dict[val]
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)