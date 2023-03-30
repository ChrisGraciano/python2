import utils
import read_csv
import chart

def run():
  data = read_csv.read_csv("./app/data.csv")
  data = list(filter(lambda item: item["Continent"] == "South America", data))

  countries = list(map(lambda x: x["Country/Territory"], data))
  percentages = list(map(lambda x: x["World Population Percentage"], data))
  chart.generate_pie_chart(countries, percentages)
  
  '''country = input("Escribe el país que quieres consultar: ")

  result = utils.pupulation_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    chart.generate_bar_chart(labels, values)'''

if __name__ == "__main__":
  run()
    

