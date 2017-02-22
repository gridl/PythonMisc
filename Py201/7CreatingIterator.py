class MyIterator:
    def __init__(self, letters):
        # constructor
        self.letters = letters
        self.position = 0

    def __iter__(self):
        # returns itself as an iterator
        return self

    def __next__(self):
        # returns the next letter in the sequence or raises stopiteration
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter


if __name__ == "__main__":
    i = MyIterator('abcd')
    for item in i:
        print(item)