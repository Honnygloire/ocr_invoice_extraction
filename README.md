# OCR – Extraction de texte (V1)

Mini-projet OCR avec Tesseract.

## Objectif
Mettre en place un script simple permettant d'extraire automatiquement du texte brut depuis une facture scannée.  
Ce projet a pour but de comprendre le fonctionnement de l'OCR (Optical Character Recognition) 

## Technologies
- Python
- PIL (Pillow) : ouverture et manipulation d’images
- pytesseract (wrapper de Tesseract OCR) : wrapper Python de Tesseract OCR
- tesseract OCR : moteur de reconnaissance optique de caractères

---

## Structure du projet

```bash
ocr-invoice/
├── facture.png #Exemple de facture scannée
├── main.py #Script principal OCR
└── README.md #Documentation du projet
```

---

## Installation

1. Installer Python 3 et pip.  
2. Installer les dépendances : pillow pytesseract , Tesseract OCR

## Utilisation

1. Placer une image de facture dans le dossier (facture.png).
2. Lancer le script :
```bash
python3 main.py
```
3. Le texte extrait s’affiche dans la console.
