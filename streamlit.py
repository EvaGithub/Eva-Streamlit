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

# Custom CSS to style the app
# Custom CSS to style the app
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
    image_path = "Rakuten_challenge3.jpg"
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(f"""<div class="header-container" style="background-image: url('data:image/jpeg;base64,{base64_image}');"></div>""", unsafe_allow_html=True)
    
    st.markdown("""
        
        ### Challenge Overview:
        - Classify products in Rakuten's e-commerce catalog using text and images.
        - Multimodal classification problem; improves product categorization.
        ### Data Source:
        - Rakuten France Multimodal Product Data Classification Challenge.  [Download Link](https://challengedata.ens.fr/challenges/35)
        ### Validation:
        - Competition site for validation and ranking. [Validation Link](https://challengedata.ens.fr/participants/challenges/35/ranking/public)
    """)


# Placeholder for other sections
if selected_menu == "Data":

# Directly declare the mapping of product type codes to category names
category_mapping = {
    10: "Used Books",
    2280: "Magazines & Comics",
    50: "Console games accessories",
    1280: "Children´s toys",
    2705: "New books",
    2522: "Office supplies",
    2582: "Gardening furniture",
    1560: "Furniture",
    1281: "Board games",
    2910: "Household linens",
    2403: "Books, magazines & collections",
    1140: "Action figurines",
    2583: "Pool & accessories",
    1180: "Role playing games",
    1300: "Miniature car toys",
    2462: "Used videogames & accessories",
    1160: "Trading card games",
    2060: "Crafts & souvenirs",
    40: "Used video games",
    60: "New console games",
    1320: "Baby care",
    1302: "Outdoor play",
    2220: "Pet accessories",
    2905: "Computer games",
    2585: "Gardening tools",
    1940: "Food",
    1301: "Indoor games"
}

# Example data
data = pd.DataFrame({
    'prdtypecode': [10,2280,50,1280,2705,2522,2582,1560,1281,2910,2403,1140,2583,1180,1300,2462,1160,2060,40,60,1320,2220,2905,2585,1940,1301]
})

# Function to ensure all categories are represented
def ensure_all_categories(data, category_mapping):
    # Convert mapping to DataFrame
    categories_df = pd.DataFrame(list(category_mapping.items()), columns=['prdtypecode', 'category_name'])
    # Merge with existing data
    data['category_name'] = data['prdtypecode'].map(category_mapping)
    full_data = pd.merge(categories_df, data['category_name'].value_counts().reset_index(), how='left', left_on='category_name', right_on='index')
    full_data.drop('index', axis=1, inplace=True)
    full_data.fillna(0, inplace=True)
    full_data.rename(columns={'category_name_y': 'count'}, inplace=True)
    return full_data[['category_name_x', 'count']]

# Function to create and display the frequency plot
def create_frequency_plot(data, category_mapping):
    category_data = ensure_all_categories(data, category_mapping)
    plt.figure(figsize=(12, 10))
    sns.barplot(y='category_name_x', x='count', data=category_data, color="lightblue")
    plt.title('Frequency Distribution of Product Categories')
    plt.xlabel('Count')
    plt.ylabel('Product Categories')
    plt.tight_layout()
    st.pyplot(plt)

# Streamlit application layout
st.title('Product Category Visualization')
st.sidebar.title('Data Visualizations')

if st.sidebar.button('Generate Frequency Plot'):
    create_frequency_plot(data, category_mapping)


   

if selected_menu == "Models":
    st.title("Models")
    st.markdown("Details about the models go here.")

if selected_menu == "Results":
    st.title("Results")
    st.markdown("Details about the results go here.")

if selected_menu == "Future work":
    st.title("Future work")
    st.markdown("Details about the future work go here.")
