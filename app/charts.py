import matplotlib.pyplot as plt

def generateBarChart(code, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./img/{code}.png')
  plt.close()

def generatePiChart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generateBarChart(labels, values)
  generatePiChart(labels, values)
