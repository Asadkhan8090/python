import streamlit as st

st.title("Basic Calculator Application")
st.subheader("Perform basic arithmetic operations")
# st. markdown("asad khan")

c1,c2 = st.columns(2)
fnum = c1.number_input("Enter the first number", value=0)
snum = c2.number_input("Enter the second number", value=0)

options = ["Add","Sub","Del","Mul"]
operation = st.radio("Select an operation", options)

button = st.button("calculate")

result= 0
if button:
    if operation == "Add":
        result = fnum + snum
    if operation == "Sub":
        result =  fnum - snum
    if operation == "Mul":
        result = fnum * snum
    if operation == "Del":
        result = fnum / snum
                
st.success(f"Result: {result}")
st.balloons()
st.snow()