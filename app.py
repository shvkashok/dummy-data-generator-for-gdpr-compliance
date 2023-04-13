# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:12:23 2023

@author: samue
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import faker
import pandas as pd

# Initialize Faker library
fake = faker.Faker()

# Streamlit app
def generate_dummy_data():
    st.title("Dummy Data Generator for GDPR Compliance")

    # Select data types
    data_types = ["First Name", "Last Name", "Date of Birth", "Gender", "Location", "ID Card", "Mobile Number",
                  "Zip Code", "Card Number", "Transaction Date", "Amount"]
    selected_data_types = st.multiselect("Select data types:", data_types, default=data_types)

    # Set number of rows to generate
    num_rows = st.number_input("Number of rows to generate:", min_value=1, value=10)

    # Generate dummy data based on selected data types
    generated_data = {}
    for data_type in selected_data_types:
        if data_type == "First Name":
            generated_data["First Name"] = [fake.first_name() for _ in range(num_rows)]
        elif data_type == "Last Name":
            generated_data["Last Name"] = [fake.last_name() for _ in range(num_rows)]
        elif data_type == "Date of Birth":
            generated_data["Date of Birth"] = [fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100) for _ in range(num_rows)]
        elif data_type == "Gender":
            generated_data["Gender"] = [fake.random_element(elements=("M", "F")) for _ in range(num_rows)]
        elif data_type == "Location":
            generated_data["Location"] = [fake.city() for _ in range(num_rows)]
        elif data_type == "ID Card":
            generated_data["ID Card"] = [fake.ssn() for _ in range(num_rows)]
        elif data_type == "Mobile Number":
            generated_data["Mobile Number"] = [fake.phone_number() for _ in range(num_rows)]
        elif data_type == "Zip Code":
            generated_data["Zip Code"] = [fake.zipcode() for _ in range(num_rows)]
        elif data_type == "Card Number":
            generated_data["Card Number"] = [fake.credit_card_number(card_type="mastercard") for _ in range(num_rows)]
        elif data_type == "Transaction Date":
            generated_data["Transaction Date"] = [fake.date_between(start_date='-30d', end_date='today') for _ in range(num_rows)]
        elif data_type == "Amount":
            generated_data["Amount"] = [fake.random_number(digits=5, fix_len=True) for _ in range(num_rows)]

    # Convert generated data to dataframe
    df = pd.DataFrame(generated_data)

    # Display generated data
    st.write("Generated Data:")
    st.write(df)

# Run the Streamlit app
if __name__ == "__main__":
    generate_dummy_data()
