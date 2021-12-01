import pandas as pd
import matplotlib.pyplot as plt
import io
data = ['name', 'john', 'mary']
print(data)
print(','.join(data))
print('\n'.join(data))
a = '\n'.join(data)
df = pd.read_csv(io.StringIO(a))
print(df)