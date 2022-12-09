class Polynomial:
    def __init__(self, coeffi):
        self.coeffi = coeffi


    def __repr__(self):
        s = ''
        s += str(self.coeffi[len(self.coeffi)-1])
        s += "x^"
        s += str(len(self.coeffi)-1)
        for i in range(len(self.coeffi)-2, -1, -1):
                if self.coeffi[i] == 0:
                    continue
                else:
                    if self.coeffi[i] > 0:
                        s += "+"
                        s += str(self.coeffi[i])

                    else:
                        s += str(self.coeffi[i])
                    if i == 1:
                        s += "x"
                    elif i != 0:
                        s += "x^"
                        s += str(i)
        return s


    def eval(self, x):
        total = 0
        for i in range(len(self.coeffi)):
            total += self.coeffi[i] * x ** i
        return total

    def __add__(self, other):
        if len(self.coeffi) > len(other.coeffi):
            result_coeffi = self.coeffi[:]
            for i in range(len(other.coeffi)):
                result_coeffi[i] += other.coeffi[i]
        else:
            result_coeffi = other.coeffi[:]
            for i in range(len(self.coeffi)):
                result_coeffi[i] += self.coeffi[i]
        return Polynomial(result_coeffi)

    def __mul__(self, other):
        a = len(self.coeffi)
        b = len(other.coeffi)
        result_coeffi = [0] * (a + b - 1)
        for i in range(0, a):
            for j in range(0, b):
                result_coeffi[i + j] += self.coeffi[i] * other.coeffi[j]
        return Polynomial(result_coeffi)

    def polySequence(self, start, end, step = 1):
        for i in range(start,end,step):
            yield self.eval(i)


    def derivative(self):
        deriv = [self.coeffi[i] * i for i in range(1, len(self.coeffi))]
        return deriv
    
def main(): 

    p1 = Polynomial([0, 2, 0, 3])
    p2 = Polynomial([0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 2])

    p3 = Polynomial.add(p1, p2)
    p4 = Polynomial.mul(p1, p2)

    print(p3.coeffi)
    print(p4.coeffi)

    print(p2)

    p5 = Polynomial([1, 2])

    for val in p5.polySequence(0,5):
        print(val)

    p6 = p1.derivative()
    p7 = p2.derivative()
    print(p6)
    print(p7)
main()



