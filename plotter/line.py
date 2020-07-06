import matplotlib.pyplot as plt
import math

def plotter(xData, yData, givenPlot, logScale=False):
    x = xData
    if (logScale):
        y = [math.log10(yValue) for yValue in yData]
    else:
        y = yData
    
    return givenPlot.plot(x, y)