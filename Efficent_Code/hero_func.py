import numpy as np 
from memory_profiler import profile 

heroes = ['Batman','Superman', 'Wonder Woman']
hts = np.array([188.0,191.0,183.0])
wts = np.array([95.0, 101.0, 74.0])

@profile
def convert_units(heroes, height, weight):
  new_hts = [ht * 0.39370 for ht in hts]
  new_wts = [wt * 2.20462 for wt in wts]

  hero_data = {}

  for i, hero in enumerate(heroes):
    hero_data[hero] = (new_hts[i], new_wts[i])
  return hero_data

convert_units(heroes, hts, wts)

