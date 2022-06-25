import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table ['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['LAKI-LAKI WNI'], rotation=30)
plt.title('Persebaran Penduduk Laki-Laki di Jakarta Pusat')
plt.xlabel('Kelurahan Di Jakarta')
plt.ylabel('Jumlah Penduduk Laki-Laki')
plt.show()