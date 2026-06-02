import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Predictive Maintenance System")

st.write(
    "Predict machine failure using Machine Learning"
)

# Inputs

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

machine_type_map = {
    "L": 0,
    "M": 1,
    "H": 2
}

air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)

rpm = st.number_input(
    "Rotational Speed (RPM)",
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    value=100
)

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[
            machine_type_map[machine_type],
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Machine Failure Predicted")
    else:
        st.success("Machine Operating Normally")