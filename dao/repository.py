import pandas as pd

'''
GLOBAL DECLARATION SECTION
'''
pd.options.display.float_format = '{:.2f}'.format

def convertDataFromCsvToPandas(filename):
    convertedData = pd.read_csv(filename)

    return convertedData

def getColumn(data, column):
    return data[column]

def addColumn(data, column, values):
    data[column] = values

    return data

def removeColumn(data, column):
    return data.drop(columns=column)

def splitDataByAggregationPeriod(data, aggregationPeriod):
    dates = getColumn(data, 'Date')

    for i in range(1, len(data)):
        if (aggregationPeriod == "Annual"):
            prevValue = dates[i - 1].split('/')[2]
            currValue = dates[i].split('/')[2]
        elif (aggregationPeriod == "Monthly"):
            prevValue = dates[i - 1].split('/')[0]
            currValue = dates[i].split('/')[0]
        else:
            return data
        
        if (currValue == prevValue):
            data.drop(i - 1, inplace=True)
        else:
            if (aggregationPeriod == "Annual"):
                data = data.replace(dates[i - 1], prevValue)
            else:
                data = data.replace(dates[i - 1], prevValue + '/' + dates[i - 1].split('/')[2])
    
    if (aggregationPeriod == "Annual"):
        data = data.replace(dates.iloc[-1], dates.iloc[-1].split('/')[2])
    else:
        data = data.replace(dates.iloc[-1], dates.iloc[-1].split('/')[0] + '/' + dates.iloc[-1].split('/')[2])
    
    newData = data.reset_index()

    return removeColumn(newData, "index")

def splitDataByDates(data, startDate, endDate):
    dates = getColumn(data, 'Date')

    inTimeFrame = False
    for i in range(len(data)):
        if (dates[i] == startDate):
            inTimeFrame = True
        
        if (dates[i] == endDate):
            inTimeFrame = False
        
        if (not inTimeFrame):
            data.drop(i, inplace=True)

    newData = data.reset_index()

    return removeColumn(newData, "index")