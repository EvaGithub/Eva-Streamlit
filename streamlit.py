import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

# Function to convert image to base64 for HTML embedding
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

# Custom CSS to style the app
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #ADD8E6;
        }
        .reportview-container .main .block-container {
            background-color: #ffffff;
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #ADD8E6;
        }
        .stMarkdown p {
            color: #495057;
        }
        .stButton > button {
            background-color: #007bff;
            color: #fff;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #343a40;
        }
    </style>
""", unsafe_allow_html=True)

# Load the datasets
@st.cache
def load_data():
    try:
        X_train = pd.read_csv('X_train_update.csv')
        Y_train = pd.read_csv('Y_train.csv')
        X_test = pd.read_csv('X_test_update.csv')
        return X_train, Y_train, X_test
    except FileNotFoundError as e:
        st.error(f"Error loading CSV files: {e}")
        return None, None, None

X_train, Y_train, X_test = load_data()

# App logic based on sidebar selection
if selected_menu == "Data":
    st.title("Data Visualizations")
    view_option = st.sidebar.selectbox(
        "Choose Visualization",
        ["Target Variable", "Duplicates", "Image Issues", "Word Cloud"]
    )

    if view_option == "Target Variable":
        st.subheader("y_train_balanced")
        st.image("path/to/y_train_balanced.jpg")
    elif view_option == "Duplicates":
        st.subheader("Text and Image Duplicates")
        col1, col2 = st.columns(2)
        with col1:
            st.image("path/to/Text_duplicates.jpg", caption="Text Duplicates")
        with col2:
            st.image("path/to/Image_duplicates.jpg", caption="Image Duplicates")
    elif view_option == "Image Issues":
        st.subheader("Images Issues")
        col1, col2 = st.columns(2)
        with col1:
            st.image("path/to/Images_issues1.jpg", caption="Images Issues 1")
        with col2:
            st.image("path/to/Images_issues2.jpg", caption="Images Issues 2")
    elif view_option == "Word Cloud":
        st.subheader("Word Cloud")
        st.image("path/to/wordcloud.png", caption="Word Cloud")

# Placeholder for other sections
if selected_menu == "Team":
    st.title("Rakuten Classification Project")
    st.header("Team")
    team_image = Image.open("path/to/Rakuten_team.png")
    st.image(team_image, caption="Rakuten Project Team")
elif selected_menu == "Problem":
    st.title("Challenge Overview")
    st.markdown("""
        - Classify products in Rakuten's e-commerce catalog using text and images.
        - Multimodal classification problem; improves product categorization.
    """)
elif selected_menu == "Models":
    st.title("Models")
    st.markdown("Details about the models go here.")
elif selected_menu == "Results":
    st.title("Results")
    st.markdown("Details about the results go here.")
elif selected_menu == "Future work":
    st.title("Future work")
    st.markdown("Details about the future work go here.")
