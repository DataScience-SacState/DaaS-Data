uniform <- function(min, max, step=NA){
  if(is.na(step) | step==0){
    number <- runif(1,min,max)
  }else{
    number <- sample(seq(min,max,step),1)
  }
  return(number)
}



normal <- function(mean, stdev, round){
  
}

findJitter<- function(maxJitter){
  return(runif(1,-maxJitter,maxJitter))
}

linear = function(slope, intercept, maxJitter, xmin, xmax){
  jitter = findJitter(maxJitter)
  x = runif(1,xmin, xmax)
  y = slope*x+intercept+jitter
  return({"x": x, "y" : y})
}

polynomial = function(degree, maxJitter, xmin, xmax){
  coefficients = NULL
  degreeList = NULL
  i = 0
  for(i in 0:degree){
    coefficients[i] = runif(1,-5,5)
    degreeList[i] = i
  }
  x = runif(1,xmin, xmax)
  y = sum(coefficients*x^degreeList) + findJitter(maxJitter)
  #return("x" : x, "y" : y)
  return(c(x,y))
}

sinusoidal = function(period, xOffset, yOffset, maxJitter, xmin, xmax){
  jitter = findJitter(maxJitter)
  x = runif(1,xmin, xmax)
  y = sin(((2*pi/period)*x-xOffset))+yOffset + jitter
  return(c(x,y))
}







