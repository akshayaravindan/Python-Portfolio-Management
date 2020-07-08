import controller.controller as controller
import dao.repository as repository
import plotter.line as linePlot
import plotter.bar as barPlot
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filename = "dao/AAPL.csv"
    startingBalance = 10000
    aggregationPeriod = "Monthly"
    startDate = "6/30/2020"
    endDate = "7/2/2020"

    rawData = controller.getData(filename)
    data = controller.removeNullRows(rawData)

    data = controller.addDailyTotalReturnColumn(data)

    data = controller.addPortfolioAmountColumn(data, startingBalance)

    # data = repository.splitDataByAggregationPeriod(data, aggregationPeriod)
    data = repository.splitDataByDates(data, startDate, endDate)
    print(data)

    # fig, axs = plt.subplots(2)
    # linePlot.plotter(data['Date'], data['Portfolio Amount'], axs[0])
    # barPlot.plotter([1, 2, 3], [1, 2, 3], axs[1])

    # plt.show()