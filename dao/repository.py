import pandas as pd

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