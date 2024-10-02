import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
# Set the style for seaborn
sns.set(style='dark')

# Load the combined dataset from CSV
all_df = pd.read_csv("C:/Users/HP/OneDrive/Documents/BANGKIT/dicoding/DASHBOARD_PROYEK/all_data.csv")
print(all_df.head())

# Set up the Streamlit app
st.title("Dashboard Penjualan")

# Tampilkan DataFrame
st.subheader("Data Pesanan")
st.dataframe(all_df.head())

### **Di kota mana sebagian besar pelanggan berasal?**
customer_city_counts = all_df['customer_city'].value_counts()

# Plot bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=customer_city_counts.index[:10], y=customer_city_counts.values[:10], palette='viridis')
plt.title('10 Kota Asal Pelanggan Teratas')
plt.xlabel('Kota Pelanggan')
plt.ylabel('Jumlah Pelanggan')
plt.xticks(rotation=45)

# Tampilkan plot di Streamlit
st.subheader("10 Kota Asal Pelanggan Teratas")
st.pyplot(plt)  # Menampilkan plot

# Reset plot untuk plot selanjutnya
plt.clf()

### Bagaimana performa penjualan dalam beberapa bulan terakhir?
# Pastikan kolom ini dalam format datetime
all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
monthly_sales = all_df.resample('M', on='order_purchase_timestamp').size()

# Plot line chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='b')
plt.title('Performa Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.grid()

# Tampilkan plot di Streamlit
st.subheader("Performa Penjualan Bulanan")
st.pyplot(plt)  # Menampilkan plot

# Reset plot untuk plot selanjutnya
plt.clf()

### Produk apa yang paling banyak dan paling sedikit terjual?
# Hitung jumlah penjualan berdasarkan kategori produk
product_sales = all_df['product_category_name'].value_counts()

# Ambil 10 kategori produk teratas dan terendah
top_categories = product_sales.head(10)
bottom_categories = product_sales.tail(10)

# Plot bar chart untuk kategori produk terlaris
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.barplot(x=top_categories.index, y=top_categories.values, palette='viridis')
plt.title('10 Kategori Produk Terlaris')
plt.xlabel('Nama Kategori Produk')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)

# Plot bar chart untuk kategori produk terendah
plt.subplot(1, 2, 2)
sns.barplot(x=bottom_categories.index, y=bottom_categories.values, palette='rocket')
plt.title('10 Kategori Produk Penjualan Rendah')
plt.xlabel('Nama Kategori Produk')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)

plt.tight_layout()

# Tampilkan plot di Streamlit
st.subheader("Kategori Produk Terlaris dan Terendah")
st.pyplot(plt)  # Menampilkan plot

# Reset plot untuk plot selanjutnya
plt.clf()

### Kapan terakhir kali pelanggan melakukan transaksi?
# Hitung tanggal terakhir untuk setiap pelanggan
last_transaction = all_df.groupby('customer_unique_id')['order_purchase_timestamp'].max().reset_index()
last_transaction.columns = ['customer_unique_id', 'last_transaction_date']

# Plot
plt.figure(figsize=(12, 6))
sns.histplot(last_transaction['last_transaction_date'], bins=30, kde=True, color='purple')
plt.title('Distribusi Tanggal Transaksi Terakhir')
plt.xlabel('Tanggal Transaksi Terakhir')
plt.ylabel('Jumlah Pelanggan')
plt.xticks(rotation=45)
plt.grid()

# Tampilkan plot di Streamlit
st.subheader("Distribusi Tanggal Transaksi Terakhir")
st.pyplot(plt)  # Menampilkan plot

# Mulai aplikasi Streamlit
if __name__ == "__main__":
    st.write("Aplikasi Dashboard Penjualan Selesai. Jalankan aplikasi dengan `streamlit run dashboard.py`.")