import streamlit as st
from scraper import extract_article_content, analyze_sentiment, detect_sensationalist_language, check_site_credibility, calculate_reliability_score, init_db, save_analysis
import matplotlib.pyplot as plt

# Initialisation de la base de données
init_db()

# Interface Streamlit
st.title("Système de Détection des Fake News")

url = st.text_input("Entrez l'URL de l'article à analyser:")

if st.button("Analyser"):
    with st.spinner('Extraction du contenu...'):
        article, error = extract_article_content(url)
    if error:
        st.error(f"Erreur : {error}")
    else:
        st.success("Contenu extrait avec succès!")

        title = article['title']
        content = article['content']

        st.subheader("Titre de l'Article")
        st.write(title)

        st.subheader("Contenu de l'Article")
        st.write(content[:1000] + '...')  # Affiche les 1000 premiers caractères

        # Analyse de sentiment
        sentiment = analyze_sentiment(content)
        st.subheader("Analyse de Sentiment")
        st.write(f"Score de sentiment : {sentiment:.2f}")

        # Détection de langage sensationnaliste
        sensationalist_count = detect_sensationalist_language(content)
        st.subheader("Détection de Langage Sensationnaliste")
        st.write(f"Nombre de mots sensationnalistes : {sensationalist_count}")

        # Vérification de la crédibilité du site
        site_credibility = check_site_credibility(url)
        st.subheader("Crédibilité du Site Source")
        st.write(f"Crédibilité : {site_credibility}")

        # Calcul du score de fiabilité
        score = calculate_reliability_score(sentiment, sensationalist_count, site_credibility)

        # Sauvegarde de l'analyse dans la base de données
        save_analysis(url, title, content, sentiment, sensationalist_count, site_credibility, score)

        st.subheader("Score de Fiabilité")
        st.write(f"Score : {score}/100")

        # Visualisation du score
        fig, ax = plt.subplots()
        ax.bar(['Fiabilité'], [score], color='green' if score > 70 else 'orange' if score > 40 else 'red')
        ax.set_ylim(0, 100)
        ax.set_ylabel('Score')
        st.pyplot(fig)

        # Suggestions (optionnel)
        # Tu peux ajouter des suggestions d'articles similaires ici
