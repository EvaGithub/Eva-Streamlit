import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

# Define custom CSS for light business blue tone and white tone
st.markdown("""
    <style>
        .main {
            background-color: #ffffff; /* White tone for main page */
        }
        .sidebar .sidebar-content {
            background-color: #ADD8E6; /* Light blue tone for sidebar */
        }
        .reportview-container .main .block-container {
            background-color: #ffffff; /* White tone for main content area */
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #ADD8E6; /* Light blue tone for upper menu */
        }
        .stMarkdown p {
            color: #495057;
        }
        .stButton>button {
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
    </style>
""", unsafe_allow_html=True)

# Sidebar header and menu
st.sidebar.title("Data Science Bootcamp March 2024")
st.sidebar.title("Menu")
menu_items = ["Team", "Problem", "Data", "Models", "Results", "Future work"]
selected_menu = st.sidebar.radio("", menu_items, index=0, key="menu")

# Load the datasets
@st.cache_data
def load_data():
    try:
        X_train = pd.read_csv('X_train_update.csv')
        Y_train = pd.read_csv('Y_train.csv')
        X_test = pd.read_csv('X_test_update.csv')
    except FileNotFoundError as e:
        st.error(f"Error loading CSV files: {e}")
        return None, None, None

    return X_train, Y_train, X_test

@st.cache_data
def load_images(image_folder, num_images=5):
    images = []
    for folder in ['image_train', 'image_test']:
        folder_path = os.path.join(image_folder, folder)
        images.extend([os.path.join(folder_path, img) for img in os.listdir(folder_path)[:num_images]])
    return images

X_train, Y_train, X_test = load_data()

if X_train is not None and Y_train is not None and X_test is not None:
    # Define a function to display sample images
    def display_images(image_paths):
        fig, axes = plt.subplots(1, len(image_paths), figsize=(15, 5))
        for img_path, ax in zip(image_paths, axes):
            image = Image.open(img_path)
            ax.imshow(image)
            ax.axis('off')
        st.pyplot(fig)

    # Main Page - Team Presentation
    if selected_menu == "Team":
        st.title("Rakuten Classification Project")

        st.header("Team")
        # Display the image
        team_image = Image.open("Rakuten_team.png")  
        st.image(team_image, caption="Rakuten Project Team")

    # Problem context
    if selected_menu == "Problem":

        st.header("Rakuten Classification Challenge")
        st.markdown("""
        ### Challenge Overview:
        - Classify products in Rakuten's e-commerce catalog using text and images.
        - Multimodal classification problem; improves product categorization.

        ### Difficulty:
        - Non-standardized, diverse data (text and images).
        - Requires contextual analysis and advanced models.

        ### Data Source:
        - Rakuten France Multimodal Product Data Classification Challenge.
        - [Download Link](https://challengedata.ens.fr/challenges/35)

        ### Validation:
        - Competition site for validation and ranking.
        - [Validation Link](https://challengedata.ens.fr/participants/challenges/35/ranking/public)
        """)

# Placeholder for other sections
if selected_menu == "Data":
    st.title("Data")
    st.markdown("Details about the data analysis go here.")

if selected_menu == "Models":
    st.title("Models")
    st.markdown("Details about the models go here.")

if selected_menu == "Results":
    st.title("Results")
    st.markdown("Details about the results go here.")

if selected_menu == "Future work":
    st.title("Future work")
    st.markdown("Details about the future work go here.")
