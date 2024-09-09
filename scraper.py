import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None, "Erreur lors de la récupération de l'URL."

        soup = BeautifulSoup(response.content, 'html.parser')

        # Tentative d'extraction du titre
        title = soup.find('title').get_text()

        # Tentative d'extraction du corps de l'article
        # Cela dépend de la structure du site, donc c'est une simplification
        paragraphs = soup.find_all('p')
        content = ' '.join([para.get_text() for para in paragraphs])

        return {'title': title, 'content': content}, None
    except Exception as e:
        return None, str(e)
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Iran"
    article, error = extract_article_content(url)
    if error:
        print(f"Erreur : {error}")
    else:
        print(f"Titre : {article['title']}")
        print(f"Contenu : {article['content'][:500]}...")  # Affiche les 500 premiers caractères
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Valeur entre -1 (négatif) et 1 (positif)
    return sentiment
SENSATIONALIST_WORDS = [
    'incroyable', 'choc', 'exclusif', 'urgent', 'alerte', 'révélé', 'secret', 
    'dangereux', 'terrible', 'surprenant', 'démenti'
]

def detect_sensationalist_language(text):
    text_lower = text.lower()
    count = 0
    for word in SENSATIONALIST_WORDS:
        if word in text_lower:
            count += 1
    return count  # Nombre de mots sensationnalistes trouvés
FIABLE_SITES = [
    'reuters.com',
    'bbc.com',
    'lemonde.fr',
    'theguardian.com',
    # Ajoute d'autres sites fiables
]

NON_FIABLE_SITES = [
    'fakenewssite.com',
    'dubioussource.net',
    # Ajoute d'autres sites non fiables
]

def check_site_credibility(url):
    domain = url.split("//")[-1].split("/")[0]
    if domain in FIABLE_SITES:
        return 'Fiable'
    elif domain in NON_FIABLE_SITES:
        return 'Non Fiable'
    else:
        return 'Inconnu'
def calculate_reliability_score(sentiment, sensationalist_count, site_credibility):
    score = 100  # Score initial

    # Ajustement basé sur le sentiment
    if sentiment < -0.5 or sentiment > 0.5:
        score -= 10  # Langage trop émotionnel

    # Ajustement basé sur les mots sensationnalistes
    score -= sensationalist_count * 5  # Chaque mot réduit le score

    # Ajustement basé sur la crédibilité du site (si connue)
    if site_credibility == 'Non Fiable':
        score -= 30
    elif site_credibility == 'Fiable':
        score += 10  # Bonus pour un site réputé fiable
    # Ne fais rien si la crédibilité est inconnue

    # Assure que le score est entre 0 et 100
    score = max(0, min(score, 100))
    return score
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Iran"
    article, error = extract_article_content(url)
    if error:
        print(f"Erreur : {error}")
    else:
        print(f"Titre : {article['title']}")
        print(f"Contenu : {article['content'][:500]}...")  # Affiche les 500 premiers caractères

        # Analyse de sentiment
        sentiment = analyze_sentiment(article['content'])
        print(f"Sentiment : {sentiment}")

        # Détection de langage sensationnaliste
        sensationalist_count = detect_sensationalist_language(article['content'])
        print(f"Mots sensationnalistes détectés : {sensationalist_count}")

        # Vérification de la crédibilité du site
        site_credibility = check_site_credibility(url)
        print(f"Crédibilité du site : {site_credibility}")

        # Calcul du score de fiabilité
        score = calculate_reliability_score(sentiment, sensationalist_count, site_credibility)
        print(f"Score de fiabilité : {score}/100")
import sqlite3

def init_db():
    conn = sqlite3.connect('fake_news.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            title TEXT,
            content TEXT,
            sentiment REAL,
            sensationalist_count INTEGER,
            site_credibility TEXT,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_analysis(url, title, content, sentiment, sensationalist_count, site_credibility, score):
    conn = sqlite3.connect('fake_news.db')
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO analyses (url, title, content, sentiment, sensationalist_count, site_credibility, score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (url, title, content, sentiment, sensationalist_count, site_credibility, score))
    conn.commit()
    conn.close()
