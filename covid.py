import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Data Download and Preprocessing Functions
def load_covid_data():
    """
    Load COVID-19 dataset from a reliable source
    This is a placeholder function - in real implementation, 
    you'd use actual data sources like Johns Hopkins CSSE or WHO
    """
    # Simulated data structure
    data = {
        'date': pd.date_range(start='2020-01-01', end='2023-12-31'),
        'confirmed_cases': np.cumsum(np.random.randint(100, 1000, size=len(pd.date_range(start='2020-01-01', end='2023-12-31')))),
        'deaths': np.cumsum(np.random.randint(10, 100, size=len(pd.date_range(start='2020-01-01', end='2023-12-31')))),
        'recovered': np.cumsum(np.random.randint(50, 500, size=len(pd.date_range(start='2020-01-01', end='2023-12-31')))),
        'country': ['USA'] * len(pd.date_range(start='2020-01-01', end='2023-12-31'))
    }
    return pd.DataFrame(data)

def preprocess_data(df):
    """
    Clean and prepare the COVID-19 dataset
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Calculate daily new cases
    df['daily_new_cases'] = df['confirmed_cases'].diff().fillna(0)
    
    # Calculate case fatality rate
    df['case_fatality_rate'] = (df['deaths'] / df['confirmed_cases'] * 100).fillna(0)
    
    return df

# Visualization Functions
def plot_total_cases(df):
    """
    Create a line plot of total confirmed cases over time
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['confirmed_cases'], label='Total Confirmed Cases')
    plt.title('COVID-19 Total Confirmed Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.xticks(rotation=45)
    return plt

def plot_daily_cases(df):
    """
    Create a bar plot of daily new cases
    """
    plt.figure(figsize=(12, 6))
    plt.bar(df['date'], df['daily_new_cases'], label='Daily New Cases')
    plt.title('COVID-19 Daily New Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of New Cases')
    plt.legend()
    plt.xticks(rotation=45)
    return plt

def plot_case_fatality_rate(df):
    """
    Create a line plot of case fatality rate
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['case_fatality_rate'], label='Case Fatality Rate')
    plt.title('COVID-19 Case Fatality Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Case Fatality Rate (%)')
    plt.legend()
    plt.xticks(rotation=45)
    return plt

# Streamlit App
def main():
    st.title('COVID-19 Data Analysis Dashboard')
    
    # Load and preprocess data
    df = load_covid_data()
    df = preprocess_data(df)
    
    # Sidebar for visualization selection
    st.sidebar.header('Visualization Options')
    visualization = st.sidebar.selectbox(
        'Select Visualization',
        ['Total Cases', 'Daily New Cases', 'Case Fatality Rate']
    )
    
    # Display selected visualization
    if visualization == 'Total Cases':
        st.pyplot(plot_total_cases(df))
    elif visualization == 'Daily New Cases':
        st.pyplot(plot_daily_cases(df))
    else:
        st.pyplot(plot_case_fatality_rate(df))
    
    # Key Statistics
    st.header('Key Statistics')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total Confirmed Cases", 
            value=f"{df['confirmed_cases'].max():,}"
        )
    
    with col2:
        st.metric(
            label="Total Deaths", 
            value=f"{df['deaths'].max():,}"
        )
    
    with col3:
        st.metric(
            label="Case Fatality Rate", 
            value=f"{df['case_fatality_rate'].iloc[-1]:.2f}%"
        )

if __name__ == '__main__':
    main()

# Requirements for the project
# requirements.txt content:
# streamlit
# pandas
# numpy
# matplotlib
# seaborn
