import pandas as pd
import plotly.express as px
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Cohort Retention Dashboard", layout="wide")
st.title("Customer Retention Cohort Analysis")
st.write("This dashboard tracks monthly cohort retention rates.")

# Use Streamlit's caching so the Excel file doesn't reload on every interaction
@st.cache_data
def load_and_clean_data():
    # 1. Load the dataset (Make sure this filename exactly matches your .xlsx file)
    df = pd.read_excel('online-retail.xlsx')
    
    # 2. Clean the data (Mirroring your Tableau README assumptions)
    # Drop rows without a CustomerID (cannot track retention without it)
    df = df.dropna(subset=['CustomerID'])
    
    # Filter out returns/cancellations (negative quantities) and zero/negative prices
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    # Ensure InvoiceDate is a datetime object
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    return df

# Load the data
df = load_and_clean_data()

# -----------------------------------------
# Cohort Analysis Logic
# -----------------------------------------

# 1. Create a period column for the Order Month
df['OrderMonth'] = df['InvoiceDate'].dt.to_period('M')

# 2. Find the very first month each customer made a purchase (Their Cohort)
df['CohortMonth'] = df.groupby('CustomerID')['OrderMonth'].transform('min')

# 3. Calculate Cohort Index (How many months it has been since their first purchase)
df['CohortIndex'] = (df['OrderMonth'].dt.year - df['CohortMonth'].dt.year) * 12 + \
                    (df['OrderMonth'].dt.month - df['CohortMonth'].dt.month)

# 4. Group by CohortMonth and CohortIndex to count unique active customers
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].nunique().reset_index()

# 5. Pivot the data to create a matrix (Rows = Cohort, Columns = Months since first purchase)
cohort_counts = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerID')

# 6. Convert absolute counts to retention percentages
cohort_sizes = cohort_counts.iloc[:, 0]
retention = cohort_counts.divide(cohort_sizes, axis=0) * 100

# Convert the Period index to strings so Plotly renders the Y-axis cleanly
retention.index = retention.index.astype(str)

# -----------------------------------------
# Plotly Visualization
# -----------------------------------------

# Build the Heatmap
fig = px.imshow(retention, 
                labels=dict(x="Months Since First Purchase", y="Cohort Month", color="Retention Rate (%)"),
                x=retention.columns, 
                y=retention.index,
                color_continuous_scale='Reds', # Matches your Tableau dark red aesthetic
                text_auto='.1f', # Show 1 decimal place
                aspect="auto") 

# Clean up layout
fig.update_layout(
    title="Monthly Cohort Retention Rate", 
    xaxis_nticks=len(retention.columns),
    plot_bgcolor='white',
    height=600
)

# Render the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)