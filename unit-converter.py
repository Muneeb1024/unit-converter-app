import streamlit as st

# st.set_page_config(page_title="Unit Converter")
st.title("⚖️Unit Converter App")
st.markdown("### Convert between different units")


st.write("Welcome! Select a category, enter a value and get the converted result in real-time")
category = st.selectbox("Select a category", ["Length", "Weight", "Temperature", "Area", "Time"])



def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value / 2.54
        elif unit == "Inches to Centimeters":
            return value * 2.54
        

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value / 0.035274
        


    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Minutes":
            return value * 1440
        elif unit == "Minutes to Days":
            return value / 1440
        elif unit == "Seconds to Hours":
            return value / 3600
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Seconds to Days":
            return value / 86400
        elif unit == "Days to Seconds":
            return value * 86400
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60


    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return value * 9/5 + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        
    elif category == "Area":
        if unit == "Square Meters to Square Feet":
            return value * 10.7639
        elif unit == "Square Feet to Square Meters":
            return value / 10.7639
        elif unit == "Square Meters to Square Miles":
            return value / 2589988.1103
        elif unit == "Square Miles to Square Meters":
            return value * 2589988.1103
        elif unit == "Square Feet to Square Miles":
            return value / 27878400
        elif unit == "Square Miles to Square Feet":
            return value * 27878400
        elif unit == "Square Meters to Hectares":
            return value / 10000
        elif unit == "Hectares to Square Meters":
            return value * 10000
        elif unit == "Square Meters to Acres":
            return value / 4046.86
        elif unit == "Acres to Square Meters":
            return value * 4046.86
        elif unit == "Square Feet to Acres":
            return value / 43560
        elif unit == "Acres to Square Feet":
            return value * 43560
        elif unit == "Square Meters to Square Kilometers":
            return value / 1000000
        elif unit == "Square Kilometers to Square Meters":
            return value * 1000000
        elif unit == "Square Meters to Square Yards":
            return value * 1.19599
        elif unit == "Square Yards to Square Meters":
            return value / 1.19599
        elif unit == "Square Meters to Square Miles":
            return value / 2589988.1103
        elif unit == "Square Miles to Square Meters":
            return value * 2589988.1103
        elif unit == "Square Meters to Square Inches":
            return value * 1550.0031
        elif unit == "Square Inches to Square Meters":
            return value / 1550.0031
        elif unit == "Square Meters to Square Centimeters":
            return value * 10000    
        elif unit == "Square Centimeters to Square Meters":
            return value / 10000
        elif unit == "Square Meters to Square Millimeters":
            return value * 1000000
        elif unit == "Square Millimeters to Square Meters":
            return value / 1000000

            
            
if category == "Length":
    unit = st.selectbox("Select a unit", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters"])
    # value = st.number_input("Enter a value")
    # if st.button("Convert"):
        # st.write(convert_units(category, value, unit))



elif category == "Time":
    unit = st.selectbox("Select a unit", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Days to Hours", "Hours to Days", "Days to Minutes", "Minutes to Days", "Seconds to Hours", "Hours to Seconds", "Seconds to Days", "Days to Seconds", "Minutes to Hours", "Hours to Minutes"])


elif category == "Temperature":
    unit = st.selectbox("Select a unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])


elif category == "Area":
    unit = st.selectbox("Select a unit", ["Square Meters to Square Feet", "Square Feet to Square Meters", "Square Meters to Square Miles", "Square Miles to Square Meters", "Square Feet to Square Miles", "Square Miles to Square Feet", "Square Meters to Hectares", "Hectares to Square Meters", "Square Meters to Acres", "Acres to Square Meters", "Square Feet to Acres", "Acres to Square Feet", "Square Meters to Square Kilometers", "Square Kilometers to Square Meters", "Square Meters to Square Yards", "Square Yards to Square Meters", "Square Meters to Square Inches", "Square Inches to Square Meters", "Square Meters to Square Centimeters", "Square Centimeters to Square Meters", "Square Meters to Square Millimeters", "Square Millimeters to Square Meters"])


elif category == "Weight":
    unit = st.selectbox("Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams"])


value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Original Value", value=f"{value:.2f}")
    with col2:
        st.metric(label="Converted Value", value=f"{result:.2f}")
    st.markdown("---")
    st.info(f"💡 The converted value is {result:.2f}")

        
            



















# st.write("This app is a unit converter that allows you to convert between different units of measurement.")

# st.write("### How to use the app")
# st.write("1. Select the unit you want to convert from.")
# st.write("2. Select the unit you want to convert to.")
# st.write("3. Enter the value you want to convert.")
# st.write("4. Click the convert button.")



