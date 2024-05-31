import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

# Define custom CSS for light green tone and styles
st.markdown("""
    <style>
        .main {
            background-color: #ffffff; /* White tone for main page */
        }
        .sidebar .sidebar-content {
            background-color: #d4edda; /* Light green tone for sidebar */
        }
        .reportview-container .main .block-container {
            background-color: #ffffff; /* White tone for main content area */
        }
        .css-18e3th9, .css-1d391kg {
            background-color: #d4edda; /* Light green tone for upper menu */
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
        hr {
            border: 0;
            height: 2px;
            background-color: #d4edda;
        }
        .participants-title {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("Menu")
menu_items = ["Team Presentation", "Problem Context", "Data Analysis", "Models", "Results", "Future Work"]
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





    # Main Page - Team Presentation
    if selected_menu == "Team Presentation":
        st.title("Teampresentation")
        st.image('Rakuten_challenge', use_column_width=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.header("Team Members")
        st.markdown("""
        - **João Pedro Kerr Catunda**
        - **Mani Chandan Naru**
        - **Eva Losada Barreiro**
        """)
    
    # Problem Context
    if selected_menu == "Problem Context":
        st.title("Problem Context")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        En quelques décennies à peine, la question du réchauffement climatique est devenue un sujet majeur,
        inquiétant pour l'avenir de la planète et de sa biodiversité, y compris l'espèce humaine.
        """)
    
    # Data Analysis
    if selected_menu == "Data Analysis":
        st.title("Data Analysis")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.header("Data Input Summary")
        st.markdown("""
        The dataset includes approximately 99,000 product listings, with around 84,916 entries in the training set and 13,812 entries in the test set. The image data is around 2.2 GB, containing images of size 500x500 pixels. in the test set. Each image is 500x500 pixels in size.
        """)
        st.image('input_dataset.png', caption='Dataset Structure 1', use_column_width=True)

        st.header("Dataset Previews")
        st.subheader("X_train.csv")
        st.write(X_train.head())

        st.subheader("Y_train.csv")
        st.write(Y_train.head())

        st.subheader("X_test.csv")
        st.write(X_test.head())

        st.header("Sample Images")
        image_paths = load_images('images', num_images=5)
        display_images(image_paths)

        st.header("Detailed Analysis of Datasets")
        analyze_dataset(X_train, "X_train.csv")
        analyze_dataset(Y_train, "Y_train.csv")
        analyze_dataset(X_test, "X_test.csv")

        st.header("Data Distribution and Visualization")
        st.subheader("Distribution of Product Type Codes in Y_train")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.countplot(y=Y_train.iloc[:, 1], ax=ax1)
        ax1.set_title('Distribution of Product Type Codes')
        ax1.set_xlabel('Count')
        ax1.set_ylabel('Product Type Code')
        st.pyplot(fig1)

        st.subheader("Length of Descriptions in X_train")
        X_train['Description Length'] = X_train['description'].apply(lambda x: len(str(x).split()))
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.histplot(X_train['Description Length'], bins=50, kde=True, ax=ax2)
        ax2.set_title('Distribution of Description Lengths')
        ax2.set_xlabel('Description Length')
        ax2.set_ylabel('Frequency')
        st.pyplot(fig2)

# Placeholder for other sections
if selected_menu == "Models":
    st.title("Models")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Details about the models go here.")

if selected_menu == "Results":
    st.title("Results")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Details about the results go here.")

if selected_menu == "Future Work":
    st.title("Future Work")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Details about the future work go here.")

# Project team in the sidebar
st.sidebar.markdown("**Promotion Continue Data Analyst - Mars 2022**")
st.sidebar.markdown('<p class="participants-title">Participants</p>', unsafe_allow_html=True)

team_members = [
    {"name": "João Pedro Kerr Catunda", "linkedin": None},
    {"name": "Mani Chandan Naru", "linkedin": "https://www.linkedin.com/in/mani-cn/"},
    {"name": "Eva Losada Barreiro", "linkedin": "https://www.linkedin.com/in/evalosadabarreiro/?locale=de_DE"}
]

for member in team_members:
    st.sidebar.markdown(f"**{member['name']}**")
    if member['linkedin']:
        st.sidebar.markdown(f"[LinkedIn]({member['linkedin']})")
