import controller.controller as controller
import plotter.line as linePlot
import plotter.bar as barPlot
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = "dao/MSFT.csv"
    startingBalance = 10000
    aggregationPeriod = "Annual"
    startDate = ""
    endDate = ""

    portfolioReturns = controller.getPortfolioReturns(filename, startingBalance, aggregationPeriod, startDate, endDate)

    portfolioGrowthDataFrame = controller.getPortfolioGrowthDataFrame(filename, startingBalance, startDate, endDate)
    print(portfolioGrowthDataFrame)

    fig, axs = plt.subplots(2)
    linePlot.plotter(portfolioGrowthDataFrame['Date'], portfolioGrowthDataFrame['Portfolio Growth'], axs[0])
    plt.yscale("log")
    barPlot.plotter([1, 2, 3], [1, 2, 3], axs[1])

    plt.show()