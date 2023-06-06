from random import randint
class Colorsearch():
    def __init__(self):
        self.week = [["GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","BLUE","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN"],
                    ["ARSH","BROWN","GREEN","BROWN","BLUE","BLUE","BLEW","PINK","PINK","ORANGE","ORANGE","RED","WHITE","BLUE","WHITE","WHITE","BLUE","BLUE","BLUE"],
                    ["GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","RED","YELLOW","ORANGE","RED","ORANGE","RED","BLUE","BLUE","WHITE","BLUE","BLUE","WHITE","WHITE"],
                    ["BLUE","BLUE","GREEN","WHITE","BLUE","BROWN","PINK","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN"],
                    ["GREEN","WHITE","GREEN","BROWN","BLUE","BLUE","BLACK","WHITE","ORANGE","RED","RED","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","WHITE"]]
    
        self.colorfre = {}
        for i in self.week:
            for j in i:
                if j in self.colorfre:
                    self.colorfre[j] += 1
                else:
                    self.colorfre[j] = 1
    
    def mostcolor(self):
        n = 0
        color = ''
        for j in self.colorfre:
            if self.colorfre[j] > n:
                n = self.colorfre[j]
                color = j
        print("Color with most frequency is " + color)
    def meancolor(self):
        sumcolor = 0
        least = 200
        meancl = ""
        for y in self.colorfre:
            sumcolor += self.colorfre[y]
        aver = sumcolor/len(self.colorfre)
        for i in self.colorfre:
            if abs(self.colorfre[i] - aver) < least:
                least = abs(self.colorfre[i] - aver)
                meancl = i
        print("Mean Color is " + meancl)

    def varianceofcolor(self):
        sumcolor = 0
        var = 0
        for y in self.colorfre:
            sumcolor += self.colorfre[y]
        aver = sumcolor/len(self.colorfre)
        
        for y in self.colorfre:
            var += (self.colorfre[y] - aver)**2
        print("Variance of colors is " + str(var/len(self.colorfre)))
    def prob_of_red_color(self):
        sumcolor = 0
        for y in self.colorfre:
            sumcolor += self.colorfre[y]
        res = int(self.colorfre["RED"])/sumcolor
        print("The probability of red color " + str(res))
    def mediancolor(self):
        val = []
        medvalu = 0
        for j in self.colorfre:
            val.append(self.colorfre[j])
        val = sorted(val)
        if len(val)%2 == 0:
            medvalu = val[int(len(val)/2)]
        else:
            medvalu = val[int((len(val) + 1)/2)]
        for i in self.colorfre:
            if self.colorfre[i] == medvalu:
                print("Median color is " + i)
                break

def searchalgorithm(m, g):
    #m is the list of numbers entered by user, and g is the number to seacrh for
    if len(m) > 0:
        if m[0] == g:
            print("A matching number found")
        else:
            m.pop(0)
            searchalgorithm(m, g)
    else:
        print("A match can't be found")
def randomfourdigit():
    rannum = ""
    for i in range(4):
        rannum = rannum + str(randint(0,1))
    rannum = "0b" + rannum
    print(int(rannum, 2))

def fibonacci():
    # The below list is the list of fibonacci sequence with first term = 1, and second term = 1.
    fib = [1,1]
    for i in range(2,50):
        fib.append(fib[i - 1] + fib[i - 2])
    print(sum(fib))

n = Colorsearch()

n.meancolor()
n.mostcolor()
n.mediancolor()
n.varianceofcolor()
n.prob_of_red_color()
searchalgorithm([1,3,4,6], 3)
randomfourdigit()
fibonacci()

