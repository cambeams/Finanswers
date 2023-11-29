from urllib.parse import uses_query
import streamlit as st
import markdown as md
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from hugchat import hugchat


# Create a title and sub-title
st.title("MyFinanswers.ai")
st.subheader("Manage your personal finances with integrated AI")
st.markdown("<h1 style='text-align: center; color:dark blue;'>Analysis</h1>", unsafe_allow_html=True)

# Create a sidebar for user input
st.sidebar.header("User Input")


uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"], key="file_uploader_1")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    if 'TransactionType' in df.columns and 'Amount' in df.columns and 'Date' in df.columns and 'NetWorth' in df.columns and 'CashFlow' in df.columns and 'CreditScore' in df.columns:
        # Convert 'Date' to datetime and set as index
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Transaction breakdown pie chart
        transaction_types = df.groupby('TransactionType')['Amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(transaction_types, labels=transaction_types.index, autopct='%1.1f%%')
        ax1.set_title('Transactions Breakdown')
        st.pyplot(fig1)

        # Monthly analysis
        monthly_data = df.resample('M')['Amount'].sum()
        monthly_withdrawals = df[df['TransactionType'] == 'Withdrawal'].resample('M')['Amount'].sum()
        monthly_expenses = df[df['TransactionType'] == 'Deposit'].resample('M')['Amount'].sum()

        # Plotting monthly trends
        fig2, ax2 = plt.subplots(3, 1, figsize=(10, 15))
        
        # Total Monthly Transactions
        ax2[0].plot(monthly_data, marker='o', color='blue')
        ax2[0].set_title('Total Monthly Transactions')
        ax2[0].set_ylabel('Amount')

        # Monthly Withdrawals
        ax2[1].plot(monthly_withdrawals, marker='o', color='red')
        ax2[1].set_title('Monthly Withdrawals')
        ax2[1].set_ylabel('Amount')

        # Monthly Deposits
        ax2[2].plot(monthly_expenses, marker='o', color='green')
        ax2[2].set_title('Monthly Deposits')
        ax2[2].set_ylabel('Amount')

        st.pyplot(fig2)

        # Net Worth Over Time
        st.header('Net Worth Over Time')
        net_worth = df['NetWorth'].resample('M').last()
        st.line_chart(net_worth)

        # Cash Flow Over Time
        st.header('Cash Flow Over Time')
        cash_flow = df['CashFlow'].resample

# Create a sidebar for user input
st.sidebar.header("Account 2")

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"], key="file_uploader_2")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    if 'TransactionType' in df.columns and 'Amount' in df.columns and 'Date' in df.columns and 'NetWorth' in df.columns and 'CashFlow' in df.columns and 'CreditScore' in df.columns:
        # Convert 'Date' to datetime and set as index
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Transaction breakdown pie chart
        transaction_types = df.groupby('TransactionType')['Amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(transaction_types, labels=transaction_types.index, autopct='%1.1f%%')
        ax1.set_title('Transactions Breakdown')
        st.pyplot(fig1)

        # Monthly analysis
        monthly_data = df.resample('M')['Amount'].sum()
        monthly_withdrawals = df[df['TransactionType'] == 'Withdrawal'].resample('M')['Amount'].sum()
        monthly_expenses = df[df['TransactionType'] == 'Deposit'].resample('M')['Amount'].sum()

        # Plotting monthly trends
        fig2, ax2 = plt.subplots(3, 1, figsize=(10, 15))
        
        # Total Monthly Transactions
        ax2[0].plot(monthly_data, marker='o', color='blue')
        ax2[0].set_title('Total Monthly Transactions')
        ax2[0].set_ylabel('Amount')

        # Monthly Withdrawals
        ax2[1].plot(monthly_withdrawals, marker='o', color='red')
        ax2[1].set_title('Monthly Withdrawals')
        ax2[1].set_ylabel('Amount')

        # Monthly Deposits
        ax2[2].plot(monthly_expenses, marker='o', color='green')
        ax2[2].set_title('Monthly Deposits')
        ax2[2].set_ylabel('Amount')

        st.pyplot(fig2)

        # Net Worth Over Time
        st.header('Net Worth Over Time')
        net_worth = df['NetWorth'].resample('M').last()
        st.line_chart(net_worth)

        # Cash Flow Over Time
        st.header('Cash Flow Over Time')
        cash_flow = df['CashFlow'].resample('M').last()
        st.line_chart(cash_flow)

        # Credit Score Over Time
        st.header('Credit Score Over Time')
        credit_score = df['CreditScore'].resample('M').last()
        st.line_chart(credit_score)

    else:
        st.write("The uploaded file does not have required columns ('TransactionType', 'Amount', 'Date', 'NetWorth', 'CashFlow', 'CreditScore').")    

# Create a sidebar for user input
st.sidebar.header("Account 3")

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"], key="file_uploader_3")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())
    
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    if 'TransactionType' in df.columns and 'Amount' in df.columns and 'Date' in df.columns and 'NetWorth' in df.columns and 'CashFlow' in df.columns and 'CreditScore' in df.columns:
        # Convert 'Date' to datetime and set as index
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Transaction breakdown pie chart
        transaction_types = df.groupby('TransactionType')['Amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(transaction_types, labels=transaction_types.index, autopct='%1.1f%%')
        ax1.set_title('Transactions Breakdown')
        st.pyplot(fig1)

        # Monthly analysis
        monthly_data = df.resample('M')['Amount'].sum()
        monthly_withdrawals = df[df['TransactionType'] == 'Withdrawal'].resample('M')['Amount'].sum()
        monthly_expenses = df[df['TransactionType'] == 'Deposit'].resample('M')['Amount'].sum()

        # Plotting monthly trends
        fig2, ax2 = plt.subplots(3, 1, figsize=(10, 15))
        
        # Total Monthly Transactions
        ax2[0].plot(monthly_data, marker='o', color='blue')
        ax2[0].set_title('Total Monthly Transactions')
        ax2[0].set_ylabel('Amount')

        # Monthly Withdrawals
        ax2[1].plot(monthly_withdrawals, marker='o', color='red')
        ax2[1].set_title('Monthly Withdrawals')
        ax2[1].set_ylabel('Amount')

        # Monthly Deposits
        ax2[2].plot(monthly_expenses, marker='o', color='green')
        ax2[2].set_title('Monthly Deposits')
        ax2[2].set_ylabel('Amount')

        st.pyplot(fig2)

        # Net Worth Over Time
        st.header('Net Worth Over Time')
        net_worth = df['NetWorth'].resample('M').last()
        st.line_chart(net_worth)

        # Cash Flow Over Time
        st.header('Cash Flow Over Time')
        cash_flow = df['CashFlow'].resample('M').last()
        st.line_chart(cash_flow)

        # Credit Score Over Time
        st.header('Credit Score Over Time')
        credit_score = df['CreditScore'].resample('M').last()
        st.line_chart(credit_score)

    else:
        st.write("The uploaded file does not have required columns ('TransactionType', 'Amount', 'Date', 'NetWorth', 'CashFlow', 'CreditScore').")
    
    


# User input functions for income, expenses, savings
def get_user_input(field_name):
    return st.sidebar.text_input(f"Monthly {field_name}", "0")
    
st.sidebar.header("Monthly Analysis") 

# Function to get user input for income
def get_income():
    income = st.sidebar.text_input("Monthly Income", "0")
    return income

# Function to get detailed user input for various expenses
def get_expenses():
    expenses_details = {
        "Rent or Mortgage": 0,
        "Car Payments": 0,
        "Other Loan Payments": 0,
        "Insurance Premiums": 0,
        "Property Taxes": 0,
        "Phone and Utility Bills": 0,
        "Child Care Costs": 0,
        "Tuition Fees": 0,
        "Gym Memberships": 0
    }

    total_expenses = 0
    for expense_item, default_value in expenses_details.items():
        expense_value = st.sidebar.text_input(f"{expense_item}", default_value)
        total_expenses += float(expense_value)

    return total_expenses

# Function to get user input for savings
def get_savings():
    savings = st.sidebar.text_input("Monthly Savings", "0")
    return savings

# Display the user's financial summary
st.header("Financial Summary")
income = get_income()
expenses = get_expenses()
savings = get_savings()

st.write(f"Your monthly income is: ${income}")
st.write(f"Your monthly expenses are: ${expenses}")
st.write(f"Your monthly savings are: ${savings}")

# Calculate and display the user's net income
net_income = float(income) - float(expenses)
st.write(f"Your net income is: ${net_income}")

# Calculate and display the user's savings rate
if float(income) > 0:
    savings_rate = (float(savings) / float(income)) * 100
    st.write(f"Your savings rate is: {savings_rate}%")
    
# Emergency Fund Adequacy
def calculate_emergency_fund(expenses, savings):
    emergency_fund_months = float(savings) / float(expenses) if float(expenses) > 0 else 0
    return emergency_fund_months

# Disposable Income
def calculate_disposable_income(income, expenses):
    disposable_income = float(income) - float(expenses)
    return disposable_income

# Simple function to respond to user queries
def get_chatbot_response(query):
    query = query.lower()
    if "How should I save?" in query:
        return "Set a savings goal and track your progress. Prioritize your spending. Build an emergency fund"
    elif "What are my expenses?" in query or "spend" in query:
        return "Tracking your expenses helps you understand where your money is going. Consider using a budgeting app."
    else:
        return "I'm sorry, I don't have an answer to that question. Please ask another finance-related question."

disposable_income = calculate_disposable_income(income, expenses)
st.write(f"Your disposable income is: ${disposable_income}")

emergency_fund_months = calculate_emergency_fund(expenses, savings)
st.write(f"Your emergency fund covers {emergency_fund_months:.1f} months of expenses")


st.sidebar.header("Annual Analysis") 

import streamlit as st

# Function to get annual income, savings, and expenses
def get_annual_financials():
    annual_income = st.sidebar.number_input("Enter your annual income", value=0.0, step=1000.0, format='%f')
    annual_savings = st.sidebar.number_input("Enter your annual savings", value=0.0, step=100.0, format='%f')
    annual_expenses = st.sidebar.number_input("Enter your annual expenses", value=0.0, step=100.0, format='%f')
    return annual_income, annual_savings, annual_expenses

# Function to calculate savings ratio
def calculate_savings_ratio(annual_income, annual_savings):
    if annual_income > 0:
        savings_ratio = (annual_savings / annual_income) * 100
    else:
        savings_ratio = 0
    return savings_ratio

# Getting user input for income, savings, and expenses
annual_income, annual_savings, annual_expenses = get_annual_financials()

# Display annual financials
st.write(f"Your annual income is: ${annual_income}")
st.write(f"Your annual savings are: ${annual_savings}")
st.write(f"Your annual expenses are: ${annual_expenses}")

# Calculating and displaying savings ratio
savings_ratio = calculate_savings_ratio(annual_income, annual_savings)
st.write(f"Your savings ratio is: {savings_ratio:.2f}%")

def get_financial_advice(savings_ratio):
    if savings_ratio < 10:
        return "Your savings ratio is less than 10%. Consider cutting unnecessary expenses and saving more."
    else:
        return "Great job! Your savings ratio is above 10."

# Call get_financial_advice regardless of whether a query is entered
response = get_financial_advice(savings_ratio)
st.sidebar.write(response)

st.sidebar.header("MyFinanswers.ai")
uses_query = st.sidebar.text_input("Ask for financial advice")        
if uses_query:
    # Use the user query to generate a response
    response = get_chatbot_response(uses_query)
    st.sidebar.write(response)
