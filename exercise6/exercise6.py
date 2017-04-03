"""
    Exercise 6: CSV and histograms
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

non_countries = [
    'ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 'EMU',
    'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA', 'IDB', 'IDX',
    'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC',
    'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST', 'SAS', 'SSA',
    'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA', 'TSS', 'UMC',
    'WLD',
]

def read_worldbank(filename, year, mean=5):
    """
    Read CSV data as provided by worldbank.org

    Arguments
    ---------
    filename: string
    year: int
    mean: float, Calculate the mean value over a range of years

    Return
    ------
    Dict
    """
    file = open(filename, encoding='utf-8')
    table = csv.reader(file)
    data = {}
    i = 0
    col_range = (0,0)
    for row in table:
        if i == 4:
            col_index = row.index(str(year))
            start = max(col_index-3, 4)
            end = min(start+5, len(row))
            col_range = (start, end)
        if i > 4 and not row[1] in non_countries:
            values = [0 if row[i] == '' else float(row[i]) for i in range(col_range[0], col_range[1])]
            data[row[1]] = np.mean(values)
        i += 1
    return data


if __name__ == '__main__':

    # Define the year
    year = 2010

    # Read the data
    pop_data = read_worldbank('population.csv', year)
    hom_data = read_worldbank('intentional-homicide.csv', year)

    # Process the data
    pop = []
    yrs = []
    for key in hom_data.keys():
        if hom_data[key] > 0 and key in pop_data:
            pop.append(pop_data[key])
            yrs.append(hom_data[key])

    pop = np.array(pop)
    yrs = np.array(yrs)

    pop = 1e-6*pop
    yrs = 1e5/yrs

    # Plot the data
    lgyrs = np.log10(yrs)
    bins = np.linspace(np.min(lgyrs), np.max(lgyrs), 21)
    bins = 10**bins

    plt.hist(yrs, bins, weights=pop)
    plt.gca().set_xscale('log')
    plt.ylabel("Population (millions)")
    plt.xlabel("Life expectancy (years)")
    plt.show()
