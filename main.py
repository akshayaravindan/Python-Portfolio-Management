import controller.controller as controller
import plotter.line as linePlot
import plotter.bar as barPlot
import matplotlib.pyplot as plt

import pandas as pd

'''
GLOBAL DECLARATION SECTION
'''
pd.options.display.float_format = '{:.2f}'.format

if __name__ == '__main__':
    filename = "dao/AAPL.csv"
    startingBalance = 10000
    aggregationPeriod = "Annual"
    startDate = ""
    endDate = ""

    rawData = controller.getData(filename)
    data = controller.removeNullRows(rawData)

    data = controller.addDailyTotalReturnColumn(data)

    data = controller.addPortfolioAmountColumn(data, startingBalance)
    print(data)

    # fig, axs = plt.subplots(2)
    # linePlot.plotter(portfolioGrowthDataFrame['Date'], portfolioGrowthDataFrame['Portfolio Growth'], axs[0])
    # plt.yscale("log")
    # barPlot.plotter([1, 2, 3], [1, 2, 3], axs[1])

    # plt.show()