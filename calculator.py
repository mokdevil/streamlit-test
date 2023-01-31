import streamlit as st

st.title("Simple calculator")

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# take input from the user
choice = st.radio("Select an operation", ("Add", "Subtract", "Multiply", "Divide"), horizontal=True)

# check if choice is one of the four options
num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")
if choice == 'Add':
    st.write(num1, "+", num2, "=", add(num1, num2))

elif choice == 'Subtract':
    st.write(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'Multiply':
    st.write(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'Divide':
    st.write(num1, "/", num2, "=", divide(num1, num2))
elif choice == 'Divide':
    st.write("divide", num1, "/", num2, "=", divide(num1, num2))
