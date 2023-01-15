from math import sqrt
print('This is a triangle solver')
print('Make sure to enter a 0 for the values you want to solve for')
triList = []
while True:
    angleA = (input('What is the measure of Angle A: '))
    if angleA.isnumeric():
        angleA = float(angleA)
        triList.append(angleA)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    angleB = input('What is the measure of Angle B: ')
    if angleB.isnumeric():
        angleB = float(angleB)
        triList.append(angleB)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    angleC = input('What is the measure of Angle C: ')
    if angleC.isnumeric():
        angleC = float(angleC)
        triList.append(angleC)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    a = input('What is the measure of Side A: ')
    if a.isnumeric():
        a = float(a)
        triList.append(a)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    b = input('What is the measure of Side B: ')
    if b.isnumeric():
        b = float(b)
        triList.append(b)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    c = input('What is the measure of Side C: ')
    if c.isnumeric():
        c = float(c)
        triList.append(c)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    perim = input('What is the perimeter: ')
    if perim.isnumeric():
        perim = float(perim)
        triList.append(perim)
        break
    else:
        print('Please enter a numerical value that is not negative')

while True:
    area = input('What is the area: ')
    if area.isnumeric():
        area = float(area)
        triList.append(area)
        break
    else:
        print('Please enter a numerical value that is not negative')

def triangleSum():
    global angleA, angleB, angleC
    if angleA ==0 and angleB ==0:
        print('Not enough info to find all angles')
        return
    if angleA ==0 and angleC ==0:
        print('Not enough info to find all angles')
        return
    if angleB ==0 and angleC ==0:
        print('Not enough info to find all angles')
        return
    if angleA ==0:
        angleA = 180 - angleB - angleC
    if angleB == 0:
        angleB = 180 - angleC - angleA
    if angleC == 0:
        angleC = 180 - angleA - angleB
    print('Angle A  is: ' + str(angleA))
    print('Angle B is: ' + str(angleB))
    print('Angle C is: ' + str(angleC))

def pythag():
    global angleA, angleB, angleC, a, b, c

    if angleA != 90 and angleB != 90 and angleC != 90:
        print('Cant use pythagorean theorem. This is not a right triangle')
        return
    if angleA == 90:
        if a == 0:
            a = sqrt(b**2 + c**2)
        if b == 0:
            b = sqrt(a**2 - c**2)
        if c == 0:
            c = sqrt(a**2 - b**2)

    if angleB == 90:
        if b == 0:
            b = sqrt(a**2 + c**2)
        if c == 0:
            c = sqrt(b**2 - a**2)
        if a ==0:
            a = sqrt(b**2 - c**2)

    if angleC == 90:
        if c == 0:
            c = sqrt(a**2 + b**2)
        if b == 0:
            b = sqrt(c**2 - a**2)
        if a == 0:
            a = sqrt(c**2 - b**2)

    print('a is: ' + str(a))
    print('b is: ' + str(b))
    print('c is: ' + str(c))

def perimeter():
      global perim, angleA, angleB, angleC, a, b, c

      if perim != 0:
          print('Cant find the perimeter. Perimeter is already given')
          return
      if angleA != 90 and angleB != 90 and angleC != 90:
          print('Cant find Perimeter. There must be at least one angle that is 90 degrees')
          return
      else:
          solvePerim = (a + b + c)
          print('perimeter is ' + str(solvePerim))
def Area():
    global area, angleA, angleB, angleC, a, b, c

    if area != 0:
        print('Cant find area. Area is already given')
        return

    if angleA != 90 and angleB != 90 and angleC != 90:
        print('Cant find area. There must be at least one angle that is 90 degrees')
        return
    else:
        if angleA == 90:
            print('area is ' + str((b*c)/2))
        if angleB == 90:
            print('area is ' + str((a*c)/2))
        if angleC == 90:
            print('area is ' + str((b*a)/2))

triangleSum()
pythag()
perimeter()
Area()