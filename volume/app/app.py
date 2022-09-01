import sqlite3
import streamlit as st 
import pandas as pd

conn = sqlite3.connect('data.db')
c = conn.cursor()



c.execute(''' create table IF NOT EXISTS spmkp(
    npwp text not null primary key,
    nama text not null ,
    tanggalcair text,
    nominal int
)
''')
conn.commit()

def input_db(npwp,nama,tanggal,nominal):
    kueri = f'insert into spmkp(npwp,nama,tanggalcair,nominal) values({npwp},"{nama}",{tanggal},{nominal})'
    c.execute(kueri)
    conn.commit()

def show_db(kueri):
    c.execute(kueri)
    data = c.fetchall()
    return data

st.header('COBA APLIKASI DENGAN SQLITE UNTUK DOCKER VOLUME')
col1,col2 = st.columns(2)


with col1 :
    st.title('Masukkan Data')
    npwp = st.text_input('Masukkan NPWP')
    nama = st.text_input('Masukkan Nama WP')
    tanggal = st.date_input('Masukkan tanggalcair')
    nominal = st.number_input('Masukkan Nominal')
    if st.button('Simpan'):
        input_db(npwp,nama,tanggal,nominal)
        logs = open('logs/logs.txt','a')
        logs.writelines(f'{npwp},"{nama}",{tanggal},{nominal}')

with col2:
    st.title('isi database')
    kueri = 'select * from spmkp'
    data = pd.DataFrame(show_db(kueri))
    st.dataframe(data)
