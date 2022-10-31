from numpy import linspace
from matplotlib import pyplot as plt
from pandas import ExcelWriter, DataFrame

class FieldLine():

    def __init__(
        self,
        x,
        y
        ):

        self.x = x
        self.y = y

    def slope(self):
        return int(self.y - self.x)

    def b(self):
        return self.y - self.slope()*self.x

    def new_y(self, x):
        return self.slope() * x + self.b()

    def line_points(self):
        offset = .1
        xs = [self.x - offset, self.x + offset]
        ys = [self.new_y(i) for i in xs]
        return xs, ys

xs = linspace(-10, 10, 21, dtype=int)
ys = linspace(-10, 10, 21, dtype=int)

flds = []
for i in range(len(xs)):
    for j in range(len(ys)):
        flds.append(FieldLine(xs[i], ys[j]))

for i in flds:
    xss, yss = i.line_points()
    plt.plot(xss, yss)
plt.xticks(xs)
plt.yticks(ys)

plt.scatter(4,0, color='black')
plt.show()

##df = DataFrame({'x': [i.x for i in flds],
##                'y': [i.y for i in flds],
##                'slope': [i.slope() for i in flds]})
##
##with ExcelWriter(r'C:\Users\mattk\OneDrive\Desktop\dataset.xlsx') as writer:
##    df.to_excel(writer)

