class Son:
    def __init__(self, qiymat):
        self.qiymat = qiymat

    def __add__(self, b):
        return Son(self.qiymat + b.qiymat)

    def __str__(self):
        return str(self.qiymat)

son1 = Son(5)
son2 = Son(7)

son3 = son1 + son2
print(son3)  # Chiqaradi: 12
