import pandas as pd

pokemon_dataset = pd.read_csv('../src/data/pokedex_420.csv')

pkmn_global = pokemon_dataset.drop(['Unnamed: 0','name', 'japanese_name', 'catch_rate', 'base_experience',
                                    'base_friendship', 'growth_rate', 'egg_cycles', 'egg_type_1', 'egg_type_2',
                                    'egg_type_number', 'percentage_male'],axis=1)

pkmn = pkmn_global[pkmn_global['generation'] <= 3]