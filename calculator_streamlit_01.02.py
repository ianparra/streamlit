import streamlit as st

# Title
st.title("Simple Calculator")

# Inputs
num1 = st.number_input("Enter value 1:", format="%.2f")
num2 = st.number_input("Enter value 2:", format="%.2f")
operation = st.selectbox("Choose an operation", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

# Calculation
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"
    st.write(f"The result is: {result}")
