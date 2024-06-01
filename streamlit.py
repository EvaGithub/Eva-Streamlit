# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import base64
import os
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

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
        .participants-title {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
        }
        .header-container {
            position: relative;
            width: 100%;
            height: 250px;
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            border-bottom: 2px solid white;
        }
    </style>
""", unsafe_allow_html=True)

# Setup the sidebar and main menu
st.sidebar.title("Data Science Bootcamp March 2024")
menu_items = ["Team", "Problem", "Data", "Models", "Results", "Future work"]
selected_menu = st.sidebar.radio("Menu", menu_items, index=0)

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

# Display images function
def display_images(image_paths):
    fig, axes = plt.subplots(1, len(image_paths), figsize=(15, 5))
    for img_path, ax in zip(image_paths, axes):
        image = Image.open(img_path)
        ax.imshow(image)
        ax.axis('off')
    st.pyplot(fig)

# App logic based on sidebar selection
if selected_menu == "Team":
    st.title("Rakuten Classification Project")
    st.header("Team")
    team_image = Image.open("Rakuten_team.png")
    st.image(team_image, caption="Rakuten Project Team")

elif selected_menu == "Problem":
    image_path = "Rakuten_challenge3.jpg"
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(f"""<div class="header-container" style="background-image: url('data:image/jpeg;base64,{base64_image}');"></div>""", unsafe_allow_html=True)
    st.markdown("""
        ### Challenge Overview:
        - Classify products in Rakuten's e-commerce catalog using text and images.
        - Multimodal classification problem; improves product categorization.
        ### Data Source:
        - Rakuten France Multimodal Product Data Classification Challenge. [Download Link](https://challengedata.ens.fr/challenges/35)
        ### Validation:
        - Competition site for validation and ranking. [Validation Link](https://challengedata.ens.fr/participants/challenges/35/ranking/public)
    """)

if selected_menu == "Data":
    st.title("Data")
    if X_train is not None and Y_train is not None:
        X_train['description'].fillna('No description', inplace=True)
        X_train['designation_length'] = X_train['designation'].apply(lambda x: len(word_tokenize(x)))
        X_train['description_length'] = X_train['description'].apply(lambda x: len(word_tokenize(x)))
        train_data = X_train.join(Y_train)

        st.sidebar.subheader("Visualization Options")
        
        # Visualization 1: Frequency Distribution of Product Type Codes
        st.sidebar.subheader("Product Type Frequency Distribution")
        all_classes = st.sidebar.checkbox("Show All Classes", True)
        selected_classes = st.sidebar.multiselect("Select Classes", options=train_data['prdtypecode'].unique(), default=train_data['prdtypecode'].unique())
        
        if all_classes or not selected_classes:
            filtered_data = train_data
        else:
            filtered_data = train_data[train_data['prdtypecode'].isin(selected_classes)]
        
        fig, ax = plt.subplots()
        sns.countplot(y='prdtypecode', data=filtered_data, color="lightblue")
        plt.title("Frequency Distribution of Product Type Codes")
        st.pyplot(fig)
        
        # Visualization 2: Boxplot of Designation and Description Lengths
        st.sidebar.subheader("Designation and Description Lengths")
        show_designation = st.sidebar.checkbox("Show Designation Lengths", True)
        show_description = st.sidebar.checkbox("Show Description Lengths", True)
        
        fig, ax = plt.subplots()
        if show_designation:
            sns.boxplot(x='prdtypecode', y='designation_length', data=train_data, color="green", ax=ax)
        if show_description:
            sns.boxplot(x='prdtypecode', y='description_length', data=train_data, color="red", ax=ax)
        plt.title("Boxplot of Designation and Description Lengths")
        plt.xticks(rotation=90)
        st.pyplot(fig)
        
        # Visualization 3: Missing Descriptions by Product Type Code
        st.sidebar.subheader("Missing Descriptions Analysis")
        missing_data = train_data.copy()
        missing_data['missing_description'] = missing_data['description'] == 'No description'
        
        fig, ax = plt.subplots()
        sns.countplot(x='prdtypecode', hue='missing_description', data=missing_data)
        plt.title("Missing Descriptions by Product Type Code")
        plt.xticks(rotation=90)
        st.pyplot(fig)

if selected_menu == "Models":
    st.title("Models")
    st.markdown("Details about the models go here.")

if selected_menu == "Results":
    st.title("Results")
    st.markdown("Details about the results go here.")

if selected_menu == "Future work":
    st.title("Future work")
    st.markdown("Details about the future work go here.")

