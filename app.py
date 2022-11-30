import streamlit as st
st.write("
         # Odd Even Tracker")
num = st.number_input("Enter number",min_value = 1,step = 1)
if (num % 2 == 0):
         st.write("The number is even")
else:
         st.write("The number is odd")
st.write("Assignment by Rajkishore Nandi,Rollno- 22f1006016")
         
