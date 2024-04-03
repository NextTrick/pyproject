import charts
import read_csv
import utils

data = read_csv.read_csv('./app/data.csv')
country = utils.getPopulationByCountryCode(data, 'GIN')
formatData = utils.extractPopulationByYear(country[0])
sortedData = {key: formatData[key] for key in sorted(formatData)}
charts.generatePiChart(list(sortedData.keys()), list(sortedData.values()))

