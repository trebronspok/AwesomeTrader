import streamlit as st

# Define the point values for each symbol
point_values = {
    "Step Index 100": 0.1,
    "Volatility Index 10": 0.001,
    "Volatility Index 25": 0.001,
    "Volatility Index 50": 0.0001,
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
risk_amount = st.number_input("Risk Amount", min_value=0.00, step=0.00001, format="%.5f")

# Entry Price
entry_price = st.number_input("Entry Price", min_value=0.00, step=0.00001, format="%.5f")

# Stop Loss Price
stop_loss_price = st.number_input("Stop Loss Price", min_value=0.00, step=0.00001, format="%.5f")

if st.button("Calculate"):
# Calculate Stop Loss Points only if entry_price and stop_loss_price are not zero
    if entry_price != 0 and stop_loss_price != 0:
        stop_loss_points = abs(entry_price - stop_loss_price)
        st.subheader(f"Stop Loss Points: {stop_loss_points}")

        # Calculate Lot Size only if stop_loss_points and risk_amount are not zero
        if stop_loss_points != 0 and risk_amount != 0:
            point_value = point_values[symbol]
            lot_size = (risk_amount/100) / (stop_loss_points * point_value)

            # Format Lot Size to 2 decimal places
            lot_size_formatted = "{:.5f}".format(lot_size)
            st.header(f"Lot Size: {lot_size_formatted}")

            # Convert Lot Size to scientific notation
            #lot_size_scientific = "{:.2e}".format(lot_size)
            #st.write(f"Lot Size (Scientific Notation): {lot_size_scientific}")
        else:
            st.write("Stop Loss Points and Risk Amount cannot be zero. Please enter valid values.")
    else:
        st.write("Entry Price and Stop Loss Price cannot be zero. Please enter valid values.")


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
