# Proyek Submission

## Setup Environment - Command Prompt (Requirements)
```
Navigasi ke folder proyek:
cd (nama path folder)

Buat virtual environment:
python -m venv env

Aktifkan virtual environment:
Pada Windows :
env\Scripts\activate
Pada Mac/Linux:
source env/bin/activate

Install dependencies:
pip install pandas matplotlib seaborn streamlit babel

Simpan dependencies ke dalam requirements.txt:
pip freeze > requirements.txt

Buka requirements.txt untuk verifikasi (opsional):
notepad requirements.txt
```

## Run steamlit app
```
Navigasi ke direktori dashboard:
cd dashboard

Jalankan aplikasi Streamlit:
streamlit run dashboard.py
```

## Struktur Proyek
```
dashboard/: Berisi file all_data.csv dan dashboard.py untuk aplikasi Streamlit.
data/: Berisi file dataset dan file notebook notebook.ipynb.
requirements.txt: Daftar dependensi yang diperlukan untuk menjalankan proyek.
```

## Notes
```
Pastikan Anda memiliki Python versi terbaru dan telah menginstal pip.
Jika Anda menghadapi masalah saat menjalankan aplikasi, pastikan semua dependensi telah terinstal dengan benar.
```
