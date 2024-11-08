#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:52:50 2024

@author: neelanjanmazumder
"""

!pip install streamlit
!pip install google-generativeai
!pip install getpass

import getpass
import os
import pandas as pd
import google.generativeai as genai

import streamlit as st


#!wget https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv -O titanic.csv

st.title("Create your data scraping query:")

df = pd.read_csv("Titanic-Dataset.csv")
print(df.shape)
print(df.columns.tolist())

os.environ["GOOGLE_API_KEY"] = "AIzaSyCukAAwH_C5WvuTvasTp8qsx5E1woWnCqE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Prepare your question
question1 = "How many people Survived?"
question2 = "How many Pclass were available?"

question=st.text_input('Enter your query here:')

# Convert the DataFrame to a string format
table = pd.DataFrame.from_dict(df)
table_str = table.to_string(index=False)
#print(table_str)
context = df.to_string(index=False)

#Generate content with Gemini
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = f"Based on the following large table, answer the question: {question}\n\nTable:\n{table_str} without * "
response = model.generate_content(prompt)

# Step 6: Print the response
print(f"Question: {question2}")
print(f"Answer: {response.text}")
st.write(response.text)

