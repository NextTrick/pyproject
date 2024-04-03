def getPopulation():
  keys = ['col', 'bol', 'pe']
  values = [300, 400, 500]
  return keys, values

a = 'this a variable'

def getPopulationByCountry(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

def getPopulationByCountryCode(data, code):
  result = list(filter(lambda item: item['CCA3'] == code, data))
  if len(result) == 0:
    return [] 
  return result[0]

def extractPopulationByYear(item):
  populationByYear = {}
  for key, value in item.items():
      if "Population" in key and key[:4].isdigit():
        year = key.split(" ")[0]
        populationByYear[year] = int(value)

  sortedPopulation = {key: populationByYear[key] for key in sorted(populationByYear)}

  return sortedPopulation.keys(), sortedPopulation.values()

def getPopulationPercentage(data):
  # populationPercentage = {}
  # for item in data:
  #   populationPercentage[item['Country/Territory']] = float(item['World Population Percentage'])
  populationPercentage = {item['Country/Territory']: float(item['World Population Percentage']) 
                          for item in data}  
  return populationPercentage.keys(), populationPercentage.values()
  


      