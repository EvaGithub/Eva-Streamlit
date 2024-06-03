import pandas as pd
import numpy as np
# from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
import seaborn as sns
import streamlit as st

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix

sns.palplot("pastel")
sns.set_style("darkgrid")


# Relevant Streamlit functions
#     st.title(): displays a title
#     st.header(): displays a second title
#     st.subheader(): displays a third title
#     st.markdown(): displays text in markdown format
#     st.code(): displays code
#     st.image(): display an image (this function takes a 3-dimensional np.array as argument)
#     st.write(): display text or code (equivalent to print on a notebook)
#     st.dataframe() : displays a dataframe. Note: Classic dataframe code should be enclosed in this command. For example, if the base code is df.head(), we write st.dataframe(df.head()) to get the display on Streamlit.*
#     st.button: creates a button
#     st.checkbox(): creates a checkbox to get the display
#     st.selectbox(): creates a box with different options to get the selected display
#     st.slider(): creates a slider to select a numeric value from a given range
#     select_slider(): creates a slider to select a non-numeric value from a given range
#
# All existing functions are listed in the following CheatSheet and in the official Streamlit documentation.

def prediction(classifier):
    if classifier == 'Random Forest':
        clf = RandomForestClassifier()
    elif classifier == 'SVC':
        clf = SVC()
    elif classifier == 'Logistic Regression':
        clf = LogisticRegression()
    clf.fit(X_train, y_train)
    return clf


def scores(clf, choice):
    if choice == 'Accuracy':
        return clf.score(X_test, y_test)
    elif choice == 'Confusion matrix':
        return confusion_matrix(y_test, clf.predict(X_test))



# streamlit_data_folder = "../git/mar24_bds_int_rakuten/reports/Streamlit/"
streamlit_data_folder = ""

# st.title("Data Science Bootcamp March 2024")
df_repeated_images = pd.read_csv(image_samples_folder + "03 - Data/Repeated Images Report.csv", index_col="category")


df_repeated_images.drop(["unique_repeated"], axis=1, inplace=True)
df_repeated_images.drop(["test"], axis=0, inplace=True)

df_classes = pd.read_csv("../DataBase/Rakuten/categories.csv")
df_classes = df_classes.astype({"Prdtypecode": object})

df_repeated_text = df_repeated_images

df_word_frequency = df_repeated_images


image_samples_folder = streamlit_data_folder + "03 - Data/Image Samples/"
image_samples = [image_samples_folder + "image_1186985707_product_3040901566.jpg",
                 image_samples_folder + "image_1205931587_product_3314026358.jpg",
                 image_samples_folder + "image_1269778871_product_3962605902.jpg",
                 image_samples_folder + "image_1283853406_product_4061619978.jpg",
                 image_samples_folder + "image_1320402674_product_4224453497.jpg"]

image_placeholder_samples_folder = streamlit_data_folder + "03 - Data/Image Placeholder Samples/"
image_placeholder_samples = [image_placeholder_samples_folder + "image_1190252015_product_2647272662.jpg",
                             image_placeholder_samples_folder + "image_1269708872_product_3962007000.jpg",
                             image_placeholder_samples_folder + "image_1261386002_product_3898718415.jpg",
                             image_placeholder_samples_folder + "image_1271791205_product_2994592691.jpg",
                             image_placeholder_samples_folder + "image_1271791205_product_3894592691.jpg"]

image_word_cloud = streamlit_data_folder + "03 - Data/square_wordcloud.jpg"

team_image = streamlit_data_folder + "01 - Team/Rakuten_team.png"

st.sidebar.title("Data Science Bootcamp March 2024")
pages = ["Problem", "Data", "Data Analysis", "Models", "Models live demo", "Results", "Future work", "Team"]
page = st.sidebar.radio("Table of contents", pages, index=0)

if page == "Team":
    st.title("Rakuten Classification Project")
    st.header("Team")
    st.image(team_image, caption="Rakuten Project Team")

if page == "Problem":
    st.title("Contest")
    st.subheader("[Rakuten France Multimodal Product Data Classification](https://challengedata.ens.fr/challenges/35)")
    st.header('Provider')
    st.subheader("[Challenge Data website](https://challengedata.ens.fr/)")
    st.header("Goal")
    st.subheader("_Classify_ an _item_ into a _store category_ given its _image_ and _textual description_.")
    st.header("Metric")
    st.subheader("[Weighted-F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)")

if page == "Data":
    st.title("Data")
    st.header("Nonstandard textual description cluttered with _links_, _hashtags_ and _markup_.")
    if st.checkbox("Show sample description"):
        st.text_area("Item description",
					 "Manette Contrôleur Classic Pro Pour Nintendo Wii Wii U - 120 M - Blanc	\"Jouez avec une manette classique à votre Nintendo Wii ou Wii U.<br>Se branche sur la Wiimote.<br>Manette avec prise en main idéale. Facilite la jouabilité.<br>Compatible 50 1160 2724395348  Nezahal Marée Primordiale - Mtg - Les Combattants D&#39;Ixalan - R - 45/196 Cartes de jeux Jeux-Video-et-Consoles Jeux-Video-et-Consoles_Cartes-de-jeux   https://fr.shopping.rakuten.com/offer/buy/2724395348/nezahal-maree-primordiale-mtg.html https://images.fr.shopping.rakuten.com/photo/1161100757_S.jpg 1  Titre=Nezahal Marée primordiale - Mtg - Les Combattants d&#39;Ixalan - r - 45/196;Tranche de poids=0 à 100 g;cartesdejeux/conditionnement=Cartes seules;Cartesdejeux/Catégorie1=Magic Dvdcave 24950 1502606277  Unité Motion Plus Contrôle Manette Wiimote Console Jeu Nintendo Wii + Housse Silicone Accessoires jeux vidéo Jeux-Video-et-Consoles Jeux-Video-et-Consoles_Accessoires-Jeux-Video   https://fr.shopping.rakuten.com/offer/buy/1502606277/unite-motion-plus-controle-manette-wiimote-console-jeu-nintendo-wii-housse-silicone.html https://images.fr.shopping.rakuten.com/photo/1104740623_S.jpg  L'unité de la Wii Remote Plus est une commande nouvelle norme pour la Wii.<br>Cette nouvelle unité utilise un accéléromètre à trois axes avec un <br>capteur optique qui fonctionne en conjonction avec la sensor bar Wii.<br>Reconnaissance des mouvements du joueur et agit comme un dispositif de pointage.<br>L'unité Wii Remote Plus intègre la technologie gyroscope supplémentaire.<br>Détecte la torsion du poignet ou les mouvements du corps avec plus de précision.<br><br>Wii MotionPlus doit être utilisé avec une manette contrôleur"" de la Remote Wii (vendu séparément).<br><br>Spécifications:<br>Wii MotionPlus intégré.<br>3-axes détection de mouvement.<br>Pour les jeux Wii MotionPlus.<br><br>Exemples de titres Wii MotionPlus compatibles:<br>Virtua Tennis 2009 - SEGA.<br>Tiger Woods PGA TOUR 10 - EA Sports.<br>Grand Slam Tennis - EA Sports.<br>Wii Sports Resort - Nintendo.<br><br>Inclus:<br>1x Unité Nintendo Wii MotionPlus + housse silicone.<br>Livraison 15 à 20 jours.\" 2118164518  Ttx Tech Manette Pad Joystick Analogique Filaire Usb Pour Playstation 3/Pc Blanc Accessoires jeux vidéo Jeux-Video-et-Consoles Jeux-Video-et-Consoles_Accessoires-Jeux-Video   https://fr.shopping.rakuten.com/offer/buy/2118164518/ttx-tech-manette-pad-joystick-analogique-filaire-usb-pour-playstation-3-pc-blanc.html https://images.fr.shopping.rakuten.com/photo/1127180220_S.jpg  <b>Descriptions du produit:</b><ul><li>TTX Tech Manette Pad Joystick Analogique filaire USB Pour PlayStation 3/PC Blanc</li></ul> En-tête / Fabricant=TTX TECH;Type de Produit=Manette;Product_scoring_GG=K;Titre=Ttx Tech Manette Pad Joystick Analogique Filaire Usb Pour Playstation 3/Pc Blanc;Divers / Consoles de jeux compatibles=PC;Divers / Couleur=Blanc;Product scoring=E;Divers / Catégorie de couleur=Blanc MAISONCYBER 249 avec la plupart des jeux Wii et Wii U Wiiware et jeux virtuels.<br> 8 boutons: X Y A B L R ZL ZR.<br>Croix directionnelle 2 sticks analogiques. Boutons : select start et home.<br>Longueur : environ 120 mètre.<br>Poids : environ 140 grammes.<br>Compatible avec les consoles Nintendo Wii et Wii U.<br>Couleur blanc. En-tête / Fabricant=Strasse Game;Type de Produit=Manette;Product_scoring_GG=I;Titre=Manette contrôleur Classic Pro pour Nintendo Wii Wii U - 120 m - Blanc;Divers / Consoles de jeux compatibles=Nintendo Wii;Marché spécifique=Rétrogaming;Product scoring=E;Divers / Catégorie de couleur=Blanc les3fritz", disabled=True, height=400)

    st.header("Nonstandard 500x500 RGB images.")
    if st.checkbox("Show sample images"):
        st.image(image_samples, width=200)

    st.header("27 diverse categories spanning a wide variety of items: from _books_ to _Gardening tools_.")
    if st.checkbox("Show Classes"):
        st.dataframe(df_classes)

if page == "Data Analysis":
    st.title("Data Analysis")

    st.header("Category distribution")
    if st.checkbox("Show balance analysis"):
        fig, ax = plt.subplots()
        plt.title("Category distribution")
        sns.barplot(x=df_repeated_images.index, y=df_repeated_images.total,
                    order=df_repeated_images.sort_values("total", ascending=False).index, label='Total', ax=ax,
                    data=df_repeated_images)
        plt.xlabel('Category', fontsize=13)
        plt.ylabel('Count', fontsize=13)
        ax.tick_params(axis='x', rotation=90)
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        st.pyplot(fig)

    st.header("Repeated data")
    if st.checkbox("Show Repeated text Analysis"):
        fig, ax = plt.subplots()
        plt.title('Repeated description count')
        sns.barplot(x=df_repeated_images.index, y=df_repeated_images.total,
                    order=df_repeated_images.sort_values("total", ascending=False).index, color='y', edgecolor='w',
                    label='Total', ax=ax)
        sns.barplot(x=df_repeated_images.index, y=df_repeated_images.total_repeated,
                    order=df_repeated_images.sort_values("total", ascending=False).index, color='g', edgecolor='w',
                    label='Repeated', ax=ax)
        plt.xlabel('Category', fontsize=13)
        plt.ylabel('Count', fontsize=13)
        ax.tick_params(axis='x', rotation=90)
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        st.pyplot(fig)

    if st.checkbox("Show Repeated image Analysis"):
        fig, ax = plt.subplots()
        plt.title('Repeated image count')
        sns.barplot(x=df_repeated_images.index, y=df_repeated_images.total,
                    order=df_repeated_images.sort_values("total", ascending=False).index, color='purple',
                    edgecolor='w',
                    label='Total', ax=ax)
        sns.barplot(x=df_repeated_images.index, y=df_repeated_images.total_repeated,
                    order=df_repeated_images.sort_values("total", ascending=False).index, color='orange',
                    edgecolor='w',
                    label='Repeated', ax=ax)
        plt.xlabel('Category', fontsize=13)
        plt.ylabel('Count', fontsize=13)
        ax.tick_params(axis='x', rotation=90)
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        st.pyplot(fig)

    if st.checkbox("Show Repeated image samples"):
        st.image(image_placeholder_samples, width=200)

    st.header("Word Cloud")
    if st.checkbox("Show most frequent words"):
        fig, ax = plt.subplots()
        plt.title('Most frequent words')
        sns.set_color_codes("muted")
        sns.barplot(y=df_word_frequency.index, x=df_word_frequency.total,
                    order=df_word_frequency.sort_values("total", ascending=False).index, edgecolor='w',
                    label='Total', ax=ax)
        plt.xlabel('Category', fontsize=13)
        plt.ylabel('Count', fontsize=13)
        ax.tick_params(axis='x', rotation=90)
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
        plt.legend()
        st.pyplot(fig)
    if st.checkbox("Show visual word frequency analysis"):
        st.image(image_word_cloud)

    # 	Missing textual data\
    # 	Placeholder images (repeats across classes)\
    # 	Data Cleaning Actions')

if page == "Models":
    st.title("Models")

if page == "Models live demo":
    st.title("Models live demo")
    st.text_area("Item description", )
    st.text_area("Item image", )
    st.write(f"Detected class:", {42})

    models = ["Word Bagging + Gradient",
              "Word Bagging + Tree",
              "Custom CNN",
              "Voting Classifier(Word Bagging + Gradient, Word Bagging + Tree, Custom CNN",
              "Google 1",
              "Google 2",
              "Google 3",
              "Google 4",
              "Bert",
              "CamemBERT",
              "MultiModel"]

    model = st.selectbox('Chosen model', models)

    st.write('The chosen model is :', model)
    #        clf = prediction(model)

    if st.checkbox("Show Accuracy"):
        st.write(scores(clf, display))
    if st.checkbox("Show Confusion matrix"):
        st.dataframe(scores(clf, display))

if page == "Results":
    st.title("Results")

if page == "Future work":
    st.title("Future work")
