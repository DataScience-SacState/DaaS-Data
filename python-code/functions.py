#bin/bash/python!
import random 
import json
import math

def brandonSummer(x, num, power):
  zipped = zip(num, power)
  y = 0
  for i in zipped:
    y = y + i[0] * math.pow(x,i[1])
  return y

def jsonReturner(keyString, valString):
  lst = zip(keyString,valString)
  rs = json.dumps(dict(lst))
  return rs

def uniformStep(minN, maxN, step=None):
  if (step == None or step == 0):
    number = random.uniform(minN,maxN)
  else:
    numberList = range(minN,maxN,step)
    number = random.choice(numberList)
  return number

def normalStep(meanN, stdev, roundN=False):
  number = random.normalvariate(meanN, stdev)
  if (roundN == True):
    return round(number)
  return number

def findJitter(maxJitter):
  minJitter = -1 * maxJitter
  number = random.uniform(minJitter,maxJitter)
  return number

def linear(slope, intercept, maxJitter, minN, maxN):
  jitter = findJitter(maxJitter)
  x = random.uniform(minN, maxN)
  y = (slope * x) + intercept + jitter
  jsonReturn = jsonReturner(['x','y'],[x,y])
  return jsonReturn

def polynomial(degree, maxJitter, minN, maxN):
  coefficients = []
  degreeList = []
  for i in range(0,degree):
    coefficients.append(random.uniform(-5,5))
    degreeList.append(i)
  x = random.uniform(minN,maxN)
  y = brandonSummer(x, coefficients, degreeList)
  jsonReturn = jsonReturner(['x','y'],[x,y])
  return jsonReturn

def sinusodial(period, xOffset, yOffset, maxJitter, minN, maxN):
  jitter = findJitter(maxJitter)
  x = random.uniform(minN,maxN)
  y = math.sin((2*math.pi/period)*x - xOffset) + yOffset + jitter
  jsonReturn = jsonReturner(['x','y'],[x,y])
  return jsonReturn

