import pandas as pd

data1 = {
    'A': [4, 6, 2],
    'B': [1, 3, 5]
}

data2 = {
    'A': [4, 1, 7],
    'B': [11, 9, 8]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

hasil_penjumlahan = df1 + df2
print("\nHasil Penjumlahan:")
print(hasil_penjumlahan)

hasil_pengurangan = df1 - df2
print("\nHasil Pengurangan:")
print(hasil_pengurangan)

hasil_perkalian = df1 * df2
print("\nHasil Perkalian:")
print(hasil_perkalian)

hasil_pembagian = df1 / df2
print("\nHasil Pembagian:")
print(hasil_pembagian)