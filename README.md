# Fake_News
# Système de Détection des Fake News

Ce projet utilise Python pour analyser des articles de presse en ligne et évaluer leur fiabilité. Il s'agit d'un système simple de détection de fake news basé sur le traitement du langage naturel (NLP) et le scraping de contenu en ligne.

## Description

L'objectif du projet est de fournir un outil capable d'analyser un article en ligne en se basant sur plusieurs critères :
- Le contenu de l'article (analyse de sentiment et détection de langage sensationnaliste)
- La crédibilité du site source
- Un score global de fiabilité est ensuite généré pour aider les utilisateurs à évaluer la fiabilité de l'article.

## Fonctionnalités

- **Analyse d'URL** : Soumettez une URL pour extraire le contenu d'un article.
- **Analyse du contenu** : Évaluation du sentiment du texte et détection de mots sensationnalistes.
- **Vérification des sources** : Analyse de la crédibilité de la source.
- **Score de fiabilité** : Génération d'un score global basé sur différents indicateurs.
- **Interface utilisateur** : Une interface web interactive créée avec **Streamlit**.

## Prérequis

Avant d'exécuter ce projet, assurez-vous que vous avez installé les éléments suivants :

- Python 3.8 ou plus
- pip (gestionnaire de paquets Python)
- Virtualenv (optionnel mais recommandé)

## Installation

1. Clonez ce dépôt dans votre machine locale :

   ```bash
   git clone https://github.com/votre_utilisateur/fake_news_detection.git
   cd fake_news_detection
Créez un environnement virtuel (optionnel mais recommandé) :

bash
Copier le code
python -m venv fake_news_env
Activez l'environnement virtuel :

Sous Windows :
bash
Copier le code
fake_news_env\Scripts\activate
Sous macOS/Linux :
bash
Copier le code
source fake_news_env/bin/activate
Installez les dépendances du projet à partir du fichier requirements.txt :

bash
Copier le code
pip install -r requirements.txt
Utilisation
Pour lancer l'application, utilisez la commande suivante :

bash
Copier le code
streamlit run app.py
Une fenêtre de navigateur s'ouvrira avec l'interface Streamlit. Vous pouvez y entrer une URL d'article et cliquer sur Analyser pour obtenir les résultats :

Le titre de l'article
L'analyse du contenu (sentiment, langage sensationnaliste)
La crédibilité du site source
Un score de fiabilité global
Exemples d'utilisation
Vous pouvez tester l'application avec la URL suivante :
https://en.wikipedia.org/wiki/France
Les résultats affichés incluront le titre de l'article, une analyse du contenu textuel, ainsi qu'un score de fiabilité.
