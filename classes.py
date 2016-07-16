class Graph:
    def __init__(self, matrix):
        self.lists = [[] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    self.lists[i].append(j, matrix[i][j])


class Vector:
    def __init__(self, coordinats):
        self.coordinats = coordinats
        self.measurement = len(coordinats)

    def __add__(self, other):
        result = [0 for i in range(self.measurement)]
        for i in range(self.measurement):
            result[i] = self.coordinats[i] + other.coordinats[i]
        return Vector(result)

    def __sub__(self, other):
        result = [0 for i in range(self.measurement)]
        for i in range(self.measurement):
            result[i] = self.coordinats[i] - other.coordinats[i]
        return Vector(result)

    def __mul__(self, other):                                             #other = list of adjacents, other2 = list of adjacents with mass
        if type(other) == Vector:                                         #scalar mul
            result = 0
            for i in range(self.measurement):
                result += self.coordinats[i] * other.coordinats[i]
            return result
        elif type(other) == Graph:                                        #return Vector
            result = [0 for i in range(self.measurement)]
            for i in range(len(other.lists)):
                for j in range(len(other.lists[i])):
                    result[other.lists[i][j][0]] += self.coordinats[other.lists[i][j][0]] * other.lists[i][j][1]
        else:
            result = Vector([0 for i in range(self.measurement)])
            for i in range(self.measurement):
                result[i] = self.coordinats[i] * other
            return Vector(result)

    def __abs__(self):
        result = 0
        for i in range(self.measurement):
            result += self.coordinats[i] ** 2
        return result

    def norma(self):
        return abs(self) ** 2
