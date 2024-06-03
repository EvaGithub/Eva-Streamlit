# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import base64
import os

# Function to convert image to base64 for HTML embedding
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

# Custom CSS to style the 
st.markdown("""
    <style>
        .main {
            background-color: #ffffff; /* White background for the main page */
        }
        .sidebar .sidebar-content {
            background-color: #ADD8E6; /* Light blue for the sidebar */
        }
        .reportview-container .main .block-container {
            background-color: #ffffff; /* White background for main content */
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #ADD8E6; /* Light blue for the top menu bar */
        }
        .stMarkdown p {
            color: #495057; /* Dark grey for text */
        }
        .stButton > button {
            background-color: #007bff; /* Blue for buttons */
            color: #fff; /* White text on buttons */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #343a40; /* Dark grey for headings */
        }
        .participants-title {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px; /* Space above the participants title */
        }
        .header-container {
            position: relative;
            width: 100%;
            height: 250px;
            background-size: cover; /* Adjusted to cover */
            background-position: center center; /* Centered horizontally and vertically */
            background-repeat: no-repeat; /* Ensures the image doesn't repeat */
            border-bottom: 2px solid white; /* Adds a white border line at the bottom */
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
    # Displaying the banner image
    image_path = "Rakuten_challenge3.jpg"
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(f"""<div class="header-container" style="background-image: url('data:image/jpeg;base64,{base64_image}'); height: 250px;"></div>""", unsafe_allow_html=True)

    # Problem Section Introduction
    st.markdown("""
    <h1 style='color: #4a90e2; text-align: center; margin-bottom: 30px;'>Rakuten France Product Classification Challenge</h1>
    """, unsafe_allow_html=True)

    # Context
    st.markdown("""
    <h2 style='color: #343a40;'>Context</h2>
    <p>The Rakuten Institute of Technology (RIT), Paris, is focusing on the large-scale, multimodal classification of products 
    into predefined type codes using both text and images. This classification aids in improving search and recommendation systems 
    on Rakuten's e-commerce platforms, where the vast range of products poses significant challenges for standard categorization techniques.</p>
    """, unsafe_allow_html=True)

    # Problem Description
    st.markdown("""
    <h2 style='color: #343a40;'>Problematic</h2>
    <p>The challenge involves predicting each product's type code based on multimodal data (text and images) from the Rakuten France catalog. 
    The use of advanced machine learning techniques to handle noisy, large-scale data sets from e-commerce platforms is central to this challenge.</p>
    """, unsafe_allow_html=True)

    # Aim
    st.markdown("""
    <h2 style='color: #343a40;'>Aim</h2>
    <p>The main objective is to develop a classifier that can automatically categorize each product into the correct product type code, 
    significantly reducing the reliance on manual categorization and improving the efficiency of the e-commerce platform's backend processes.</p>
    """, unsafe_allow_html=True)

    # Metric
    st.markdown("""
    <h2 style='color: #343a40;'>The Metric</h2>
    <p>Submissions will be evaluated based on the <strong>weighted-F1 score</strong>, which considers both precision and recall, 
    particularly important in unbalanced datasets typically found in commercial product catalogs.</p>
    """, unsafe_allow_html=True)

    # Data Source
    st.markdown("""
    <h2 style='color: #343a40;'>Data</h2>
    <p>Data is provided for registered participants and includes images and text descriptions of products listed on Rakuten France's e-commerce site. 
    This challenge presents a unique set of data, rich in diversity but also complexity due to the noisy and often incomplete information provided by sellers.</p>
    """, unsafe_allow_html=True)



# Placeholder for other sections
if selected_menu == "Data":
    options = ["Target Variable", "Duplicates", "Image Issues", "Word Cloud"]
    choice = st.selectbox("Choose Visualization", options)

    if choice == "Target Variable":
        st.subheader("Target Variable ")
        try:
            image = Image.open("y_train_balanced.jpg")
            st.image(image, caption="Frequency Distribution of target variable")
        except FileNotFoundError:
            st.error("File not found: y_train_balanced.jpg")

    elif choice == "Duplicates":
        st.subheader("Text and Image Duplicates")
        try:
            image1 = Image.open("Text_duplicates.jpg")
            st.image(image1, caption="Text Duplicates")
        except FileNotFoundError as e:
            st.error(f"File not found: {e}")

    elif choice == "Image Issues":
        st.subheader("Image Issues")
        try:
            image2 = Image.open("Image_issues2.png")
            st.image(image2)
        except FileNotFoundError as e:
            st.error(f"File not found: {e}")

    elif choice == "Word Cloud":
        st.subheader("Word Cloud")
        try:
            image = Image.open("wordcloud.png")
            st.image(image, caption="Word Cloud")
        except FileNotFoundError:
            st.error("File not found: wordcloud.png")


if selected_menu == "Models":
    st.title("Models")
    st.markdown("Details about the models go here.")

if selected_menu == "Results":
    st.title("Results")
    st.markdown("Details about the results go here.")

if selected_menu == "Future work":
    st.title("Future work")
    st.markdown("Details about the future work go here.")
