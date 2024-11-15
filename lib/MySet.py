class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, val):
        self.dictionary[val] = True
        return self
    
    def delete(self, val):
        self.dictionary.pop(val, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
    
    def __str__(self):
        set_list = []
        for key, val in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'