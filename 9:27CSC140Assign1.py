#Devon Hobbs
#9/27, CSC 140, Volume of a Circle
'''
I found that the Monte Carlo method is not very good unless you test a very
large number of random points. The % errors when using 10 points for the 2D
circle, 3D sphere, and 4D hyper-sphere, respectively, was 3.23%, 8.83%, and
12.37%. However, the difference in using 100 and 99999 points was miniscule
in most cases, but there was a 7% difference with the hyper-sphere. In
conclusion, increasing the number of points used does help to a certain
extent but both the % error and results of the volume are still wrong and
inconsistent
'''

import random
import math


points2d = int(input("# of 2D test points:"))
points3d = int(input("# of 3D test points:"))
points4d = int(input("# of 4D test points:"))

def d2():
    hits2d = 0
    for i in range(points2d):
        x = random.random()
        y = random.random()
        x = x*2-1
        y = y*2-1
        if x**2 + y**2 <= 1:
            hits2d = hits2d + 1
    volume2d = (hits2d/points2d*4)
    print(str(volume2d))

def d3():
    hits3d = 0
    for i in range(points3d):
        x = random.random()
        y = random.random()
        z = random.random()
        x = x*2-1
        y = y*2-1
        z = z*2-1
        if x**2 + y**2 + z**2 <= 1:
            hits3d = hits3d + 1
    volume3d = (hits3d/points3d*8)
    print(str(volume3d))

def d4():
    hits4d = 0
    for i in range(points4d):
        x = random.random()
        y = random.random()
        z = random.random()
        w = random.random()
        x = x*2-1
        y = y*2-1
        z = z*2-1
        w = w*2-1
        if x**2 + y**2 + z**2 + w**2 <= 1:
            hits4d = hits4d + 1
    volume4d = (hits4d/points4d*16)
    print(str(volume4d))

d2()
d3()
d4()



    




    
        
