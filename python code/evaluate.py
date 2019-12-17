"""try some configurations"""

import csv
import numpy as np
import pandas as pd
from calculate_cost import CostCalculator
from run_sim import Simulink

print('starting simulink')

cost_calculator = CostCalculator(400, 1, 0.2, 6000, 1000000)  # add turbine later
simulink = Simulink('WT_SP_model_vs1total')

print('started simulink')

N_PANELS = 4
N_SOLAR_FEATURES = N_PANELS * 3

rows = []
with open('examples.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        row_array = np.array([float(f) for f in row])
        # run simulink
        energy_production = simulink.run_simulation(row_array[:N_SOLAR_FEATURES], 10)  # add turbine later
        # run cost calculator
        sp_sm = np.sum(row_array[0:N_SOLAR_FEATURES:3])
        stats = cost_calculator.get_stats(energy_production, sp_sm, 0)  # add turbine later
        stats['surface_1'] = row_array[0]
        stats['angle_1'] = row_array[1]
        stats['orientation_1'] = row_array[2]
        stats['surface_2'] = row_array[3]
        stats['angle_2'] = row_array[4]
        stats['orientation_2'] = row_array[5]
        stats['surface_3'] = row_array[6]
        stats['angle_3'] = row_array[7]
        stats['orientation_3'] = row_array[8]
        stats['surface_4'] = row_array[9]
        stats['angle_4'] = row_array[10]
        stats['orientation_4'] = row_array[11]
        rows.append(stats)
        print('ran simulation')

df = pd.DataFrame(rows)
df.to_excel('stats.xlsx')

print('saved result')
