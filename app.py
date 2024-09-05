import streamlit as st

#define BMI function
def calculate_bmi(height_in_inches, weight_in_pounds):
  # convert height from inches to meters
  height_in_meters = height_in_inches * 0.0254

  # convert weight from pounds to kilograms
  weight_in_kg = weight_in_pounds * 0.453592

  #calculate the BMI
  bmi = weight_in_kg / (height_in_meters **2)

  return bmi


#streamlit app title
st.title("BMI Calculator")

#get user input for height and weight
height_in_inches = st.number_input("Enter your height in inches: ", min_value=0.0)
weight_in_pounds = st.number_input("Enter your weight in pounds: ", min_value=0.0)

#call function
if st.button("Calculate BMI"):
    bmi = calculate_bmi(height_in_inches, weight_in_pounds)
    st.write(f"Your BMI is {bmi:.2f}")
