import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import requests
import re
import socket

# Configuration du bot Telegram
TOKEN = "TOKEN"
CHAT_ID = "chatid"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Chemin vers le driver
service = Service("C:/Users/Khali/Downloads/edgedriver_win64/msedgedriver.exe")

try:
    # Créer une instance du WebDriver pour Edge
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)

    # Accès à LinkedIn
    driver.get("https://www.linkedin.com/login")
    
    # Authentification
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("EMail@gmail.com")  # Remplacez par votre email LinkedIn
    password_input.send_keys("Password")  # Remplacez par votre mot de passe LinkedIn
    
    time.sleep(5)

    # Accéder à la page d'accueil
    driver.get("https://www.linkedin.com/feed/")# Remplacez par in lien LinkedIn

    # Fonction pour faire défiler la page
    def scroll_page(times):
        for _ in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)  # Attendre que la page charge plus de posts

    # Nombre de fois que vous souhaitez défiler
    scroll_times = 15
    scroll_page(scroll_times)

    # Mots-clés spécifiques pour la détection
    keywords = [
        "java", "JEE", "Salesforce Developer", "front end", 
        "angular", "react", "vuejs", "javascript", 
        "typescript", "omnichannel", "omnistudio", "Hiring", 
        "Nous sommes à la recherche"
    ]

    # Parcourir les posts
    posts = driver.find_elements(By.CLASS_NAME, "occludable-update")
    for post in posts:
        try:
            # Extraction du texte du post
            post_text = post.find_element(By.CSS_SELECTOR, ".update-components-text.relative.update-components-update-v2__commentary").text

            # Vérifier si le post contient "India"
            if "india" in post_text.lower():
                continue  # Passer au prochain post

            # Détection des mots-clés
            if any(keyword.lower() in post_text.lower() for keyword in keywords):
                # Extraction des informations du post
                try:
                    # Extraction du nom de l'auteur
                    author_name = post.find_element(By.CSS_SELECTOR, ".update-components-actor__name").text
                except:
                    author_name = "Inconnu"

                try:
                    # Extraction du type de poste
                    job_type_element = post.find_element(By.CSS_SELECTOR, ".update-components-text.relative.update-components-update-v2__commentary")
                    job_type = re.search(r"(java|JEE|Salesforce Developer|front end|angular|react|vuejs|javascript|typescript|omnichannel|omnistudio)", job_type_element.text, re.IGNORECASE)
                    job_type = job_type.group(0) if job_type else "Inconnu"
                except:
                    job_type = "Inconnu"

                try:
                    # Extraction de la localisation
                    location = re.search(r"(Casablanca|Maroc|Europe)", post_text, re.IGNORECASE)
                    location = location.group(0) if location else "Non spécifiée"
                except:
                    location = "Non spécifiée"

                try:
                    # Extraction de l'email
                    email = re.search(r"[\w\.-]+@[\w\.-]+", post_text)
                    email = email.group(0) if email else "Non spécifié"
                except:
                    email = "Non spécifié"

                try:
                    # Extraction de la date de publication
                    post_date = post.find_element(By.CSS_SELECTOR, ".update-components-actor__sub-description").text
                except:
                    post_date = "Non spécifiée"

                # Création du message pour Telegram
                message = (
                    f"👤 Auteur : {author_name}\n"
                    f"💼 Poste : {job_type}\n"
                    f"📍 Localisation : {location}\n"
                    f"📧 Email : {email}\n"
                    f"📅 Date de publication : {post_date}\n\n"
                    f"Contenu du poste :\n{post_text}"
                )

                # Envoi du message au bot Telegram
                data = {
                    "chat_id": CHAT_ID,
                    "text": message
                }
                response = requests.post(TELEGRAM_API_URL, data=data)

        except Exception as e:
            print(f"Erreur lors du traitement d'un post : {e}")

except socket.timeout:
    print("La connexion au serveur a expiré.")

except Exception as e:
    print(f"Une erreur est survenue : {e}")

finally:
    # Ne pas fermer le navigateur automatiquement
    input("Appuyez sur Entrée pour terminer et fermer le navigateur...")
    driver.quit()
