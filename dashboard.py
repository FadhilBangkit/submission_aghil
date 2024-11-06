import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Load your data
df_all = pd.read_csv("C:/Users/user/submission/Dashboard/main_data.csv")

# Sidebar selection for variable
with st.sidebar:
    genre = st.selectbox(
        label="Pilih Variabel",
        options=('PM2.5 dan PM10', 'Suhu')
    )

# Title and description

# Conditional content based on selected variable
if genre == 'PM2.5 dan PM10':
    # PM2.5 dan PM10 dalam Tahun
    st.title('Kualitas Udara')
    st.markdown(
    """
    PM2.5 dan PM10 adalah dua jenis partikel polutan udara yang berbeda dalam hal ukuran dan efek terhadap kesehatan. 
    Keduanya merupakan bagian dari Particulate Matter (PM) atau Materi Partikulat, yaitu campuran partikel padat dan cair yang ada di udara.
    """
    )
    with st.container():
        st.subheader("Nilai PM2.5 dan PM10 dalam tahun")
        pm25_yearly_avg = df_all.groupby('year')['PM2.5'].mean()
        pm10_yearly_avg = df_all.groupby('year')['PM10'].mean()
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        ax1.bar(pm25_yearly_avg.index, pm25_yearly_avg.values, color='skyblue', label='PM2.5')
        ax1.set_title("Average Yearly Concentrations of PM2.5")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Concentration (µg/m³)")
        ax1.set_xticks(pm25_yearly_avg.index)
        ax1.set_xticklabels(pm25_yearly_avg.index.astype(str)) 
        ax1.legend(title="Pollutant")
        ax2.bar(pm10_yearly_avg.index, pm10_yearly_avg.values, color='salmon', label='PM10')
        ax2.set_title("Average Yearly Concentrations of PM10")
        ax2.set_xlabel("Year")
        ax2.set_ylabel("Concentration (µg/m³)")
        ax2.set_xticks(pm10_yearly_avg.index)
        ax2.set_xticklabels(pm10_yearly_avg.index.astype(str))
        ax2.legend(title="Pollutant")
        plt.tight_layout()
        st.pyplot(fig)

    with st.expander("Penjelasan"):
        st.write(
        """
        Nilai PM2.5 dan PM10 berdasarkan tahun, dapat dilihat bahwa PM2.5 tertinggi terjadi pada tahun 2014 dan 2017. Sedangkan
        untuk PM10 tertinggi pada tahun 2014.
        """
        )

    # PM2.5 dan PM10 dalam bulan
    with st.container():
        st.subheader("Nilai PM2.5 dan PM10 dalam 12 bulan")
        pm25_by_month = df_all.groupby('month')['PM2.5'].mean()
        pm10_by_month = df_all.groupby('month')['PM10'].mean()
        plt.figure(figsize=(20, 5))
        sns.lineplot(x=pm25_by_month.index, y=pm25_by_month.values, marker='o', label='PM2.5', color='blue')
        sns.lineplot(x=pm10_by_month.index, y=pm10_by_month.values, marker='o', label='PM10', color='red')
        plt.title("Average PM2.5 and PM10 by Month")
        plt.xlabel("Month")
        plt.ylabel("Concentration")
        plt.legend(title="Pollutant")
        plt.ylim(0, max(pm25_by_month.max(), pm10_by_month.max()) * 1.1)
        st.pyplot(plt.gcf())

    with st.expander("Penjelasan"):
        st.write(
        """
        Nilai PM2.5 dan PM10 melonjak dari bulan 10 hingga 3. Pada bulan-bulan tersebut, disarankan untuk menyiapkan pelindung mulut agar
        terhindar dari partikel yang berbahaya.
        """
        )

    # PM2.5 dan PM10 dalam jam        
    with st.container():
        st.subheader("Nilai PM2.5 dan PM10 dalam 24 jam")
        pm25_by_hour = df_all.groupby('hour')['PM2.5'].mean()
        pm10_by_hour = df_all.groupby('hour')['PM10'].mean()
        plt.figure(figsize=(20, 5))
        sns.lineplot(x=pm25_by_hour.index, y=pm25_by_hour.values, marker='o', label='PM2.5', color='blue')
        sns.lineplot(x=pm10_by_hour.index, y=pm10_by_hour.values, marker='o', label='PM10', color='red')
        plt.title("Average PM2.5 and PM10 by Hour")
        plt.xlabel("Hour")
        plt.ylabel("Concentration (µg/m³)")
        plt.legend(title="Pollutant")
        plt.ylim(0, max(pm25_by_hour.max(), pm10_by_hour.max()) * 1.1)
        plt.xlim(-1, 24)
        plt.xticks(ticks=range(0, 24), labels=[str(i + 1) for i in range(24)])
        st.pyplot(plt.gcf())

    with st.expander("Penjelasan"):
        st.write(
        """
        Nilai PM2.5 dan PM10 berdasarkan jam. Dapat dilihat bahwa terjadi lonjakan tingkat partikel
        pada jam 18 hingga jam 1. Disarankan agar memakai pelindung mulut ketika di luar agar melindungi diri
        dari partikel yang berbahaya.
        """
        )


#page Suhu
elif genre == 'Suhu':
    # New page for temperature data
    st.title('Data Suhu')
    st.markdown(
        """
        Suhu udara adalah ukuran derajat panas atau dingin yang terdapat di atmosfer. Suhu ini diukur dengan 
        menggunakan alat yang disebut termometer dan biasanya dinyatakan dalam derajat Celsius (°C) atau Fahrenheit (°F). 
        Suhu udara sangat penting karena mempengaruhi berbagai aspek kehidupan, termasuk cuaca, iklim, dan ekosistem, 
        serta berperan dalam kegiatan manusia sehari-hari seperti pertanian, perikanan, dan kegiatan industri. Dalam data ini ditampilkan dalam celcius
        """
    )
    
    #Suhu dalam tahun
    with st.container():
        st.subheader("Suhu Tahunan")
        df_year_TEMP = df_all.groupby(by=['year']).agg({'TEMP': 'mean'})

        # Menyiapkan figure untuk bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(df_year_TEMP.index.astype(str), df_year_TEMP['TEMP'], color='skyblue')  
        plt.xlabel('Year')
        plt.ylabel('Average Temperature (°C)')
        plt.title('Average Temperature by Year')
        plt.xticks(rotation=45)

        # Menampilkan plot di Streamlit
        st.pyplot(plt.gcf())
    with st.expander("Penjelasan"):
        st.write(
        """
        Suhu mengalami penurunan dari tahun ke tahun kecuali pada tahun 2016 namun tidak terlalu banyak perubahannya.
        """
        )
        
    #Suhu Bulanan
    with st.container():
        st.subheader("Suhu Bulanan")
        df_month_TEMP = df_all.groupby(by=['month']).agg({'TEMP': 'mean'})

        # Menyiapkan figure untuk bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(df_month_TEMP.index.astype(str), df_month_TEMP['TEMP'], color='skyblue')  
        plt.xlabel('month')
        plt.ylabel('Average Temperature (°C)')
        plt.title('Average Temperature by month')
        plt.xticks(rotation=45)

        # Menampilkan plot di Streamlit
        st.pyplot(plt.gcf())
    with st.expander("Penjelasan"):
        st.write(
        """
        Suhu terdingin terjadi pada bulan 1, 2, dan 12. Diharapkan agar menyiapkan perlengkapan musim dingin
        """
        )
    
    #Suhu perjam
    with st.container():
        st.subheader("Suhu Perjam")
        df_jam_TEMP = df_all.groupby(by=['hour']).agg({'TEMP': 'mean'})

        # Menyiapkan figure untuk bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(df_jam_TEMP.index.astype(str), df_jam_TEMP['TEMP'], color='skyblue')  
        plt.xlabel('jam')
        plt.ylabel('Average Temperature (°C)')
        plt.title('Average Temperature by jam')
        plt.xticks(rotation=45)

        # Menampilkan plot di Streamlit
        st.pyplot(plt.gcf())
    with st.expander("Penjelasan"):
        st.write(
        """
        Variasi suhu naik turun, dari pukul 1 hingga pukul 5 mengalami penurunan. Pada pukul 6 hingga 15 mengalami kenaikkan.
        Pada pukul 16 hingga pukul 23 mengalami penurunan.
        """
        )
