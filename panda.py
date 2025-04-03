import pandas as pd
data={
    'Name':['Tom','Jerry','Mickey','Donald'],
    'edad':[20,21,19,18],
    'ciudad':['Madrid','Barcelona','Valencia','Sevilla'],
}

tablet=pd.DataFrame(data)
print(tablet)