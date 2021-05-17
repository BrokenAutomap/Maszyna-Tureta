import numpy


class Graf:
    def __init__(self, A, B, C):

        if B.shape == C.shape and B.shape[0] == len(A) and B.shape[1] == len(A):
            self.top = A[:]
            self.connect = numpy.array(B)
            self.weight = numpy.array(C)
            print("Udało się stworzyć graf!")

        else:
            raise Exception("Macierz nie spelnia warunku")

    def skierowany(self):
        T = numpy.transpose(self.weight) == self.weight

        if T.sum() == T.shape[0] * T.shape[0]:
            return 0
        else:
            return 1

    def sort_kruskal(self):
        listakrawedzi = list([])
        for i in range(0, len(self.top)):
            if self.skierowany == 1:
                alfa = 0
            else:
                alfa = i
            for j in range(alfa, len(self.top)):
                if self.connect[i][j] == 1:
                    h = tuple([self.weight[i][j], self.top[i], self.top[j]])
                    listakrawedzi.append(h)
        return listakrawedzi

    def show(self):
        print(self.top, "\n")
        print(self.connect, "\n")
        print(self.weight, "\n")


if __name__ == "__main__":
    A = ['A', 'B', 'C']
    B = numpy.array([(1, 1, 1), (1, 1, 1), (1, 1, 1)])
    C = numpy.array([(4, 7, 3), (4, 2, 4), (2, 9, 5)])