def filter_by_population(data, population_filter):
    result = list(filter(lambda item : int(item['2022 Population']) > population_filter, data))
    return result
