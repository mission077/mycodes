
#*******************************************************************************
#
# Programmer: Mission Kadariya
#
# Assignment: cpSelectionHW.py
#
# Description: This program contains different function to calculate the equation
#              of a line and distance betwwen the line. It has displayed output
#              for different condition and also checked the points lies inside  
#              the circle or not
#*******************************************************************************

import math

# Prompting user for Value for Variable
x1 =float(input("x1 :"))
y1 =float(input("y1 :"))
x2 =float(input("x2 :"))
y2 =float(input("y2 :"))

#**********************************************************************************
# function_name : calculateSlope
#
# description: This function is coded to find the slope of a line.
# 
# parameters:  x1, y1, x2, y2
# 
# returns: Slope is returned. 
#          It is returned to calculate slope from given points.
#**********************************************************************************
def calculateSlope(x1, y1, x2, y2):
    if x1 != x2 and y1 != y2 :
        slope = (y2-y1)/(x2-x1)
    else:
        slope = 0
    return slope 
#**********************************************************************************
# function_name : findYIntercept
#
# description: This function is coded to find the Y-intercept of a line.
# 
# parameters:  x1, y1, x2, y2
# 
# returns: B is returned in the function.
#          It is returned to calculate Y-intercept from given points and slope
#**********************************************************************************
def findYIntercept(x1, y1, x2, y2):
    slope = calculateSlope(x1, y1, x2, y2)
    b = y1 - slope * x1
    return b
#**********************************************************************************
# function_name : findLineEquation
#
# description: This function is coded to find the slope of a line.
# 
# parameters:  x1, y1, x2, y2
# 
# returns: No
#**********************************************************************************
def findLineEquation(x1, y1, x2, y2):
    slope = calculateSlope(x1, y1, x2, y2)
    b = findYIntercept(x1, y1, x2, y2)
    
# Calling the variable outside the function:
b = findYIntercept(x1, y1, x2, y2)
slope = calculateSlope(x1, y1, x2, y2)

#These following points are checked in the driver code
# (1,-1) and (1,-10)
# (6, 1) and (2, 5)
#(-5,-3) and (8,10)
# (1, 3) and (2, 3)
# (1,-1) and (2,-2)
# (1, 1) and (2, 2)
# (2, 4) and (3, 6)
# (1,-4) and (2,-6)

#Driver code to check the points and print line equations.
if x1 == x2:
    print (f"x = {x2:.1f}")
elif slope == -1 and b == 0 :
    print(f"y = -x")
elif slope == 1 and b == 0:
    print("y = x")
elif slope == -1:
    print(f"y = -x + {b:.1f}")
elif slope == 1:
    print(f"y= x + {b:.1f} ")
elif slope == 0:
    print(f"y= {b:.1f}")
elif b == 0:
    print(f"y = {slope:.1f}x")
elif b < 0 :
    print(f"y = {slope:.1f}x {b:.1f}")

else:
    print((f"y = {slope:.1f}x + {b:.1f}"))


#Prompting User for the values to find Distance Formula
centerX =float(input("centerX :")) 
centerY =float(input("centerY :")) 
pointx  =float(input("pointx  :"))
pointy  =float(input("pointy  :"))
radius  =float(input("Radius  :"))

#*******************************************************************************
# function_name : calcDistance
#
# description: To find the distance formula by prompting user for values
# 
# parameters:  centerX, centerY, pointx, pointy
# 
# returns:  d is returned which is the Distance formula. It is
#          returned to calculate Distance Formula.
#*******************************************************************************
def calcDistance(centerX, centerY, pointx, pointy):
    d = math.sqrt((centerX - pointx)**2 +(centerY - pointy)**2)
    return d 
d = calcDistance(centerX, centerY, pointx, pointy)

#*******************************************************************************
# function_name : isInsideCircle
#
# description: This function checks wheather the given points lies inside the
#               circle or outside.
# 
# parameters:  centerX, centerY, radius, pointx, pointy

# returns: d is returned to check the given points lies inside or outside the
#           function.
#*******************************************************************************
def isInsideCircle(centerX, centerY, radius, pintX, pointY):
    d = calcDistance(centerX, centerY, pointx, pointy)

#Driver code to check and display where the point lies .
if d <= radius**2:
    print("Inside Circle")
elif d >= radius**2:
    print("Outside Circle")

    




