from math import sqrt


class Vector:
    vector = []

    def __init__(self, vector):
        self.vector = vector

    def add(self, b):
        if len(self.vector) != len(b.vector):
            raise Exception
        else:
            tmp = [0 for i in range(len(self.vector))]
            for i in range(len(self.vector)):
                tmp[i] = self.vector[i] + b.vector[i]
            return Vector(tmp)

    def subtract(self, b):
        if len(self.vector) != len(b.vector):
            raise Exception
        else:
            tmp = [0 for i in range(len(self.vector))]
            for i in range(len(self.vector)):
                tmp[i] = self.vector[i] - b.vector[i]
            return Vector(tmp)

    def dot(self, b):
        if len(self.vector) != len(b.vector):
            raise Exception
        else:
            tmp = 0
            for i in range(len(self.vector)):
                tmp += self.vector[i] * b.vector[i]
            return tmp

    def norm(self):
        tmp = 0
        for el in self.vector:
            tmp += el ** 2
        return sqrt(tmp)

    def __str__(self):
        return "(" + ",".join([str(el) for el in self.vector]) + ")"

    def __eq__(self, other):
        return self.vector == other.vector
