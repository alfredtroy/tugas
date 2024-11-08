import numpy as np
import pandas as pd

data = np.random.randint(1, 11, size=10)  
print("Data yang dihasilkan:", data)

df = pd.DataFrame(data, columns=['Angka'])

df_sorted = df.sort_values(by='Angka')

top_5 = df_sorted.head(5)
bottom_5 = df_sorted.tail(5)

print("\n5 Angka Teratas:")
print(top_5)

print("\n5 Angka Terbawah:")
print(bottom_5)