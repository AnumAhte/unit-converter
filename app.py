import streamlit as st
from pint import UnitRegistry

# Streamlit default header/footer hide karna
st.markdown("""
    <style>
        /* Streamlit header, footer, menu hide karna */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Background styling */
        body { background-color: #f5f5f5; }
        
        /* Main content box */
        .main { 
            background: linear-gradient(135deg, #6a11cb, #2575fc); 
            padding: 20px; 
            border-radius: 12px; 
            color: white; 
            text-align: center;
        }
        
        /* Selectbox and input fields styling */
        .stSelectbox, .stNumberInput, .stButton>button {
            font-size: 18px !important;
            border-radius: 8px !important;
        }

        /* Convert button styling */
        .stButton>button {
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #2575fc, #6a11cb);
        }
    </style>
""", unsafe_allow_html=True)

# Unit registry initialize
ureg = UnitRegistry()

# Unit categories
unit_categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Mass": ["kilogram", "gram", "milligram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
    "Volume": ["liter", "milliliter", "gallon", "cubic_meter"],
    "Area": ["square_meter", "square_kilometer", "square_foot", "acre", "hectare"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "Energy": ["joule", "calorie", "kilowatt_hour", "btu"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["kilometer/liter", "mile/gallon"],
    "Digital Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "megabit/second", "gigabit/second"]
}

# Custom title
st.markdown('<div class="main"><h1>⚡ Unit Converter</h1></div>', unsafe_allow_html=True)

# Select category
category = st.selectbox(" Select Unit Category", list(unit_categories.keys()))

# Select units
units = unit_categories[category]
col1, col2 = st.columns(2)
from_unit = col1.selectbox("🔄 Convert from", units)
to_unit = col2.selectbox("➡ Convert to", units)

# Input value
value = st.number_input(" Enter value", min_value=0.0, format="%.4f")

# Convert button
if st.button(" Convert Now"):
    try:
        result = (value * ureg(from_unit)).to(to_unit).magnitude
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    except:
        st.error("❌ Invalid conversion! Try another unit.")
