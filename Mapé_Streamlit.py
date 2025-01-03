
import streamlit as st

# Titre de l'application
st.title("Mon application Streamlit")

# Affichage d'un message
st.write("Bonjour, Ntugulo Lebon ")

# Ajout d'un curseur pour sélectionner une valeur
valeur = st.slider("Sélectionnez une valeur", 0, 100, 50)

# Affichage de la valeur sélectionnée et de son carré
st.write(f"La valeur sélectionnée est {valeur} et son carré est {valeur**2}")
from datetime import datetime
import datetime
# Demander à l'utilisateur de saisir sa date de naissance
date_naissance =st.date_input("Entrez votre date de naissance", datetime.date(2000, 4, 29))
# Obtenir la date actuelle
aujourd_hui = datetime.date.today()
# Vérifier si c'est l'anniversaire de 
if aujourd_hui.month == date_naissance.month and aujourd_hui.day == date_naissance.day:
    st.success("Joyeux anniversaire ! ")
else:
    st.info(f"Ce n'est pas votre anniversaire aujourd'hui. Votre anniversaire est le {date_naissance.strftime('%d %B')}.")
# Afficher la date de naissance saisie
st.write("Votre date de naissance est :", date_naissance)


