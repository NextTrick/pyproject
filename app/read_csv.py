import csv

def read_csv(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter = ',')
    header = next(reader)  # Getting the header
    data = []
    for row in reader:
      iterable = zip(header, row)   # Combining the header with the row
      countryDict = {key: value for key, value in iterable} # Creating a dictionary
      data.append(countryDict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)