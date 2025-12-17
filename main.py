from PIL import Image
import pytesseract, os

# Indiquer à pytesseract où trouver les fichiers de langue
os.environ["TESSDATA_PREFIX"] = "/opt/homebrew/share/tessdata"

# Charger l'image de la facture
image = Image.open("facture.png")

# Extraire le texte avec Tesseract (langue française)
text = pytesseract.image_to_string(image, lang="fra")

# Afficher le texte extrait
print("Texte extrait de la facture :\n")
print(text)