import webbrowser
import os
import html
from datetime import datetime
import platform

# Liste pour stocker les réponses
reponses_utilisateur = []

continu = True

while continu:
    prenom = input("Quel est votre prénom ? ").strip()
    nom = input("Quel est votre nom ? ").strip()

    # Vérification d'identité
    if prenom.lower() == "ali" and nom.lower() == "camara":
        print(f"Te revoilà, {prenom} {nom} !")
    else:
        print(f"Bonjour, {prenom} {nom} !")

    # --- Simulation d'une "analyse USB" ---
    print("\nAnalyse du système en cours...\n")

    # Informations système de base
    systeme = platform.system()
    version = platform.version()
    processeur = platform.processor()

    # Simuler le nombre de ports USB (ici juste pour l'exemple)
    nb_usb = 4  # tu peux changer ce chiffre ou le détecter réellement plus tard

    print(f"Système détecté : {systeme}")
    print(f"Version : {version}")
    print(f"Processeur : {processeur}")
    print(f"Nombre de ports USB détectés : {nb_usb}")

    # Enregistrer la date et l'heure exactes
    date_heure = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Sauvegarde dans la liste
    reponses_utilisateur.append({
        "prenom": prenom,
        "nom": nom,
        "systeme": systeme,
        "processeur": processeur,
        "ports_usb": nb_usb,
        "date_heure": date_heure
    })

    # Demander si on continue
    reponse = input("\nSouhaitez-vous refaire une analyse ? (oui/non) ").strip().lower()
    while reponse not in ["oui", "non"]:
        reponse = input("Réponds par 'oui' ou 'non' : ").strip().lower()

    if reponse != "oui":
        continu = False
        print("Fin de l'analyse. Au revoir !")

# --- Génération du HTML ---
def generer_html(reponses):
    contenu = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Rapport d'analyse système</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            table { border-collapse: collapse; width: 90%; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
        </style>
    </head>
    <body>
        <h1>Historique des analyses USB</h1>
        <table>
            <tr>
                <th>Prénom</th>
                <th>Nom</th>
                <th>Système</th>
                <th>Processeur</th>
                <th>Ports USB</th>
                <th>Date et Heure</th>
            </tr>
    """
    for r in reponses:
        contenu += f"""
            <tr>
                <td>{html.escape(r['prenom'])}</td>
                <td>{html.escape(r['nom'])}</td>
                <td>{html.escape(r['systeme'])}</td>
                <td>{html.escape(r['processeur'])}</td>
                <td>{html.escape(str(r['ports_usb']))}</td>
                <td>{html.escape(r['date_heure'])}</td>
            </tr>
        """
    contenu += """
        </table>
    </body>
    </html>
    """
    return contenu

# Créer le fichier HTML et l'ouvrir
fichier_html = "rapport_usb.html"
with open(fichier_html, "w", encoding="utf-8") as f:
    f.write(generer_html(reponses_utilisateur))

webbrowser.open("file://" + os.path.abspath(fichier_html))
