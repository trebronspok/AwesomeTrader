import streamlit as st

# Define the point values for each symbol
point_values = {
    "Step Index 100": 0.01,
    "Volatility Index 10": 0.01,
    "Volatility Index 25": 0.01,
    "Volatility Index 50": 0.01,
    "Volatility Index 75": 0.01,
    "Volatility Index 100": 0.01,
    "Volatility Index 10 1s": 0.01,
    "Volatility Index 25 1s ": 0.01,
    "Volatility Index 50 1s": 0.01,
    "Volatility Index 75 1s": 0.01,
    "Volatility Index 100 1s": 0.01,
    "Volatility Index 150 1s": 0.01,
    "Volatility Index 200 1s": 0.01,
    "Volatility Index 300 1s": 0.01,
    "Jump Index 10": 0.01,
    "Jump Index 25": 0.01,
    "Jump Index 50": 0.01,
    "Jump Index 100": 0.01,
    # Add more symbols and their point values here
}

# Streamlit app
st.title("Deriv Lot Size Calculator")

# Pick List of Symbol
symbol = st.selectbox("Select Symbol", list(point_values.keys()))

# Pick List Position Type
position_type = st.selectbox("Select Position Type", ["Buy", "Sell"])

# Risk Amount
risk_amount = st.number_input("Risk Amount", min_value=0.0, step=0.01)

# Entry Price
entry_price = st.number_input("Entry Price", min_value=0.0, step=0.01)

# Stop Loss Price
stop_loss_price = st.number_input("Stop Loss Price", min_value=0.0, step=0.01)

# Calculate Stop Loss Points
stop_loss_points = abs(entry_price - stop_loss_price)
st.subheader(f"Stop Loss Points: {stop_loss_points}")

# Calculate Lot Size
point_value = point_values[symbol]
lot_size = (risk_amount/100) / (stop_loss_points * point_value)
lot_size_formatted = "{:.5f}".format(lot_size)
st.header(f"Lot Size: {lot_size_formatted}")


# Convert Lot Size to scientific notation
#lot_size_scientific = "{:.2e}".format(lot_size)
#st.header(f"Lot Size: {lot_size_scientific}")

# Add footer with sample copyright
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>&copy; 2024 Awesome Trader. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)