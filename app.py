import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EcoTrack AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 EcoTrack AI")
st.subheader("Personal Carbon Footprint Assistant")

st.sidebar.header("Daily Activities")

transport = st.sidebar.selectbox(
    "Mode of Transport",
    ["Car", "Bike", "Bus", "Train", "Walking"]
)

distance = st.sidebar.number_input(
    "Distance Travelled (km)",
    min_value=0,
    value=10
)

electricity = st.sidebar.number_input(
    "Electricity Usage (kWh)",
    min_value=0,
    value=5
)

meat_meals = st.sidebar.number_input(
    "Meat Meals Per Week",
    min_value=0,
    value=3
)

shopping = st.sidebar.number_input(
    "Online Purchases Per Month",
    min_value=0,
    value=2
)

transport_factor = {
    "Car": 0.21,
    "Bike": 0.10,
    "Bus": 0.08,
    "Train": 0.04,
    "Walking": 0
}

transport_emission = distance * transport_factor[transport]
electricity_emission = electricity * 0.82
food_emission = meat_meals * 2
shopping_emission = shopping * 1.5

total = (
    transport_emission +
    electricity_emission +
    food_emission +
    shopping_emission
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Transport CO₂",
        f"{transport_emission:.2f} kg"
    )

with col2:
    st.metric(
        "Electricity CO₂",
        f"{electricity_emission:.2f} kg"
    )

with col3:
    st.metric(
        "Total CO₂",
        f"{total:.2f} kg"
    )

st.subheader("Carbon Breakdown")

df = pd.DataFrame({
    "Category": [
        "Transport",
        "Electricity",
        "Food",
        "Shopping"
    ],
    "CO2": [
        transport_emission,
        electricity_emission,
        food_emission,
        shopping_emission
    ]
})

st.bar_chart(
    df.set_index("Category")
)

st.subheader("AI Recommendations")

if transport == "Car":
    st.warning(
        "Use public transport or carpooling to reduce emissions."
    )

if electricity > 10:
    st.warning(
        "High electricity usage detected. Consider energy-efficient appliances."
    )

if meat_meals > 5:
    st.warning(
        "Reducing meat consumption can significantly lower your carbon footprint."
    )

if total < 10:
    st.success(
        "Excellent! Your carbon footprint is relatively low."
    )

elif total < 20:
    st.info(
        "Good progress. Small improvements can make a big difference."
    )

else:
    st.error(
        "Your carbon footprint is high. Follow the recommendations above."
    )

st.subheader("Sustainability Score")

score = max(0, 100 - total * 2)

st.progress(
    int(score)
)

st.write(
    f"🌿 Your Eco Score: {score:.0f}/100"
)

st.subheader("Future Features")

st.markdown("""
- AI Carbon Forecasting
- Green Rewards System
- Community Challenges
- Carbon Credit Marketplace
- Smart Meter Integration
""")