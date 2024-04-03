import utils
import charts
import read_csv

def run():
  #print(utils.a) #importing variable from module
  countryCode= input('Type country code => ')
  data = read_csv.read_csv('./data.csv')
  country = utils.getPopulationByCountryCode(data, countryCode)
  if len(country) > 0:    
    labels, values = utils.extractPopulationByYear(country)    
    charts.generateBarChart(countryCode, labels, values)
  else:
    print('Country not found')

def piChartProcess(): # My solution
  data = read_csv.read_csv('./data.csv')
  labels, values = utils.getPopulationPercentage(data)    
  charts.generatePiChart(labels, values)

def piChartProcess2(): # Another solution  
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percetages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generatePiChart(countries, percetages)
  
if __name__ == '__main__': # It' called: entry point
  run()
  piChartProcess()
  #piChartProcess2()