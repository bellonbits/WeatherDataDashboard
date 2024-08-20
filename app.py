import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('WeatherData.csv')

# Convert 'Date/Time' to datetime format and set as index
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df.set_index('Date/Time', inplace=True)

# Create sidebar for navigation
st.sidebar.title("Weather Data Analysis")
option = st.sidebar.selectbox("Select Section", 
                              ["Data Overview", "Statistical Summary", "Time Series Analysis", 
                               "Correlation Analysis", "Seasonal Trends", "Anomalies", "Insights & Recommendations"])

# Data Overview
if option == "Data Overview":
    st.title("Data Overview")
    st.write(df.head())
    st.write(f"Number of records: {df.shape[0]}")
    st.write(f"Number of features: {df.shape[1]}")
    st.write(f"Data types:\n{df.dtypes}")

# Statistical Summary
elif option == "Statistical Summary":
    st.title("Statistical Summary")
    st.write(df.describe())

# Time Series Analysis
elif option == "Time Series Analysis":
    st.title("Time Series Analysis")
    
    # Temperature over time
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Temp_C'], marker='o', linestyle='-', color='b')
    plt.title('Temperature Over Time')
    plt.xlabel('Date/Time')
    plt.ylabel('Temperature (°C)')
    st.pyplot(plt)
    
    # Humidity over time
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Rel_Hum_%'], marker='o', linestyle='-', color='g')
    plt.title('Humidity Over Time')
    plt.xlabel('Date/Time')
    plt.ylabel('Relative Humidity (%)')
    st.pyplot(plt)
    
    # Wind Speed over time
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Wind_Speed_km/h'], marker='o', linestyle='-', color='r')
    plt.title('Wind Speed Over Time')
    plt.xlabel('Date/Time')
    plt.ylabel('Wind Speed (km/h)')
    st.pyplot(plt)

# Correlation Analysis
elif option == "Correlation Analysis":
    st.title("Correlation Analysis")
    
    # Correlation Matrix
    plt.figure(figsize=(10, 8))
    corr = df[['Temp_C', 'Dew_Point_Temp_C', 'Rel_Hum_%', 'Wind_Speed_km/h', 'Visibility_km', 'Press_kPa']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    st.pyplot(plt)

# Seasonal Trends
elif option == "Seasonal Trends":
    st.title("Seasonal Trends")
    
    # Plot seasonal temperature
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Season', y='Temp_C', data=df)
    plt.title('Temperature by Season')
    plt.xlabel('Season')
    plt.ylabel('Temperature (°C)')
    st.pyplot(plt)
    
    # Plot seasonal humidity
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Season', y='Rel_Hum_%', data=df)
    plt.title('Humidity by Season')
    plt.xlabel('Season')
    plt.ylabel('Relative Humidity (%)')
    st.pyplot(plt)

# Investigate Anomalies
elif option == "Anomalies":
    st.title("Investigate Anomalies")
    
    # Temperature Outliers
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Temp_Outliers', y='Temp_C', data=df)
    plt.title('Temperature Outliers')
    plt.xlabel('Outliers')
    plt.ylabel('Temperature (°C)')
    st.pyplot(plt)

# Insights & Recommendations
elif option == "Insights & Recommendations":
    st.title("Insights & Recommendations")
    
    st.write("### 5.1 Summarizing Key Insights")
    st.write("""
    The plots show seasonal variations in temperature and humidity for a location. The temperature plot exhibits a clear pattern, with higher temperatures typically observed from May through August during the summer months. Temperatures peak in July. A similar seasonal pattern is seen for humidity, as humidity levels are higher in the summer and lower in the winter. Humidity is highest between August and September.

    The bar charts provide summaries of average temperature and humidity by season. The summer season from June through August has the highest average temperature compared to other seasons. Both summer and fall seasons see the highest average humidity levels, while winter has the lowest humidity on average.

    Overall, the analyses reveal significant seasonal fluctuations in temperature and humidity for this location. Temperature and humidity generally increase during the summer months and decrease during the winter months. The insights offer a high-level view of typical seasonal patterns and trends in the climate. This information could prove useful for applications like agriculture, energy management, and outdoor planning by providing context about expected seasonal weather conditions.
    """)
    
    st.write("### 6.1 Suggest Areas for Further Study")
    st.write("""
    To enhance the weather dataset analysis, I would consider expanding the scope to include longitudinal studies that track seasonal and annual trends over multiple years, enabling the identification of long-term patterns and the effects of climate change. Advanced techniques such as time series forecasting can predict future weather conditions, while examining the impact of weather on other factors like agricultural productivity and energy consumption can provide valuable insights. Incorporating geographical and regional analyses will reveal variations across different areas and potential microclimates. Investigating extreme weather events and anomalies will offer a deeper understanding of unusual patterns. Additionally, integrating external data sources like historical weather records, satellite imagery, air quality measurements, and socio-economic indicators will enrich the analysis, providing a more comprehensive view of weather impacts and interactions.
    """)
