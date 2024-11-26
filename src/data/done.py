#alle generation sortiert als balkendiagramm

gen_sort = pkmn_global.value_counts('generation')

gen_sort.plot(kind= 'bar',
              x = 'count',
              y = 'generation');