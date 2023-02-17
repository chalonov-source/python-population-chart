import utils
import read_csv
import charts

def run():

    data = read_csv.read_csv('./project/data.csv')
    print('** Este programa le ayuda a filtrar los paises con la población\n mayor a las ingresada y los mostrara en una grafica **')
    population_filter = int(input('Ingrese una cantidad de habitantes (ej: 10000000) => '))
    title_chart = f"Paises con población mayor a {population_filter/1000000}M de habitantes en el 2022"

    data = utils.filter_by_population(data, population_filter)
    countries = list(map(lambda x : x['Country/Territory'], data))
    population = list(map(lambda x : x['2022 Population'], data))    
    charts.generate_pie_chart(countries, population, title_chart)

if __name__ == '__main__':
    run()
