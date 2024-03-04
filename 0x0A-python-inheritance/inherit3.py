class A:
    def __init__(self, n='mikiyas'):
        self.name = n

    def display(self):
        print(self.name)


class B(A):
    def __init__(self, roll):
        super().__init__()
        self.roll = roll


object = B('bezi')
print(object.display())
