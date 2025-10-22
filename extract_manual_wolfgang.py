import PyPDF2
import sys
import os

def extract_pdf_text():
    """Extrait le texte du manuel Wolfgang GA100"""
    
    pdf_path = r"c:\Users\SWARM\OneDrive - Noovelia\Documents\GitHub\camera-record-video\WOLFANG_GA100.pdf"
    
    try:
        print("📄 Ouverture du PDF Wolfgang GA100...")
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"📊 Nombre de pages: {num_pages}")
            print("\n🔍 Recherche des mentions de 'USB', 'webcam', 'PC Camera'...\n")
            print("="*70)
            
            found_pages = []
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text().lower()
                
                # Mots-clés à chercher
                keywords = ['usb mode', 'pc camera', 'webcam', 'uvc', 'mass storage', 
                           'usb connection', 'computer connection', 'usb setting']
                
                for keyword in keywords:
                    if keyword in text:
                        if page_num not in found_pages:
                            found_pages.append(page_num)
                            print(f"\n📄 PAGE {page_num + 1} - Contient: '{keyword}'")
                            print("-"*70)
                            
                            # Extraire contexte autour du mot-clé
                            lines = page.extract_text().split('\n')
                            for i, line in enumerate(lines):
                                if keyword.lower() in line.lower():
                                    # Afficher ligne trouvée + contexte
                                    start = max(0, i-2)
                                    end = min(len(lines), i+3)
                                    print('\n'.join(lines[start:end]))
                                    print()
            
            if not found_pages:
                print("\n⚠️ Aucune mention spécifique trouvée.")
                print("Extraction du contenu des premières pages...\n")
                
                for page_num in range(min(5, num_pages)):
                    print(f"\n--- PAGE {page_num + 1} ---")
                    print(pdf_reader.pages[page_num].extract_text())
                    
    except ImportError:
        print("❌ PyPDF2 non installé")
        print("Installation: pip install PyPDF2")
        print("\n📝 Tentative avec méthode alternative...")
        extract_pdf_basic()
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        print("\n📝 Tentative avec méthode basique...")
        extract_pdf_basic()

def extract_pdf_basic():
    """Méthode basique sans PyPDF2"""
    pdf_path = r"c:\Users\SWARM\OneDrive - Noovelia\Documents\GitHub\camera-record-video\WOLFANG_GA100.pdf"
    
    print("\n" + "="*70)
    print("INSTRUCTIONS WOLFGANG GA100 - SANS EXTRACTION PDF")
    print("="*70)
    
    print("""
🎯 NAVIGATION MENU WOLFGANG GA100 (Basé sur modèles similaires)

╔══════════════════════════════════════════════════════════╗
║  MENU WOLFGANG GA100 - CHERCHEZ DANS CET ORDRE :        ║
╚══════════════════════════════════════════════════════════╝

1️⃣ Bouton MENU (sur Wolfgang)
   ↓
2️⃣ Utilisez ↑↓ pour naviguer
   ↓
3️⃣ CHERCHEZ CES SECTIONS :

   📂 "Setup" ou "Paramètres" ou ⚙️
      ↓
      Entrez (bouton OK)
      ↓
      📂 "USB Mode" ou "Connexion USB" ou 🔌
         ↓
         Entrez (bouton OK)
         ↓
         ✅ "PC Camera" ← SÉLECTIONNEZ CECI
         ❌ "Mass Storage" ← NE PAS SÉLECTIONNER

OU ALTERNATIVEMENT :

   📂 "System" ou "Système"
      → "USB Setting" 
      → "Camera Mode"

OU :

   📂 "Connection" ou "Connexion"
      → "USB Mode"
      → "PC Camera"

╔══════════════════════════════════════════════════════════╗
║  MÉTHODE RAPIDE (Si menu complexe) :                    ║
╚══════════════════════════════════════════════════════════╝

1. Wolfgang ÉTEINT
2. Branchez USB au PC
3. ALLUMEZ Wolfgang (pendant qu'il est branché)
4. Il devrait démarrer en mode PC Camera automatiquement

╔══════════════════════════════════════════════════════════╗
║  BOUTONS WOLFGANG GA100 :                               ║
╚══════════════════════════════════════════════════════════╝

🔴 Power - Allumer/Éteindre
📋 Menu - Ouvrir paramètres
⬆️ Up - Naviguer vers le haut
⬇️ Down - Naviguer vers le bas
✅ OK/Select - Valider choix
🔙 Back - Retour

╔══════════════════════════════════════════════════════════╗
║  VÉRIFICATION QUE ÇA FONCTIONNE :                       ║
╚══════════════════════════════════════════════════════════╝

✅ Écran Wolfgang affiche "PC Camera" ou "UVC"
✅ Windows fait "ding" (son connexion USB)
✅ Apparaît dans Gestionnaire de périphériques
✅ Visible dans l'app Caméra Windows

""")

if __name__ == "__main__":
    extract_pdf_text()