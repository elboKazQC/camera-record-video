import sys
import os

def analyze_pdf_info():
    """Analyse les informations du fichier PDF Wolfgang GA100"""
    
    pdf_path = r"c:\Users\SWARM\OneDrive - Noovelia\Documents\GitHub\camera-record-video\WOLFANG_GA100.pdf"
    
    if not os.path.exists(pdf_path):
        print("❌ Fichier PDF non trouvé")
        return
    
    # Informations basiques du fichier
    file_size = os.path.getsize(pdf_path)
    print(f"📄 Fichier trouvé: WOLFANG_GA100.pdf")
    print(f"📊 Taille: {file_size:,} bytes ({file_size/1024/1024:.1f} MB)")
    
    # Tentative de lecture des premières données pour identifier le type
    try:
        with open(pdf_path, 'rb') as f:
            header = f.read(100)
            print(f"📝 En-tête: {header[:50]}...")
            
            # Vérifier si c'est vraiment un PDF
            if header.startswith(b'%PDF'):
                print("✅ Fichier PDF valide détecté")
                
                # Lire plus de contenu pour chercher des mots-clés
                f.seek(0)
                content = f.read(min(file_size, 50000))  # Lire max 50KB
                
                # Chercher des mots-clés liés à webcam/USB
                keywords = [
                    b'webcam', b'USB', b'PC Camera', b'streaming', 
                    b'computer', b'connection', b'mode', b'UVC',
                    b'live', b'camera', b'video', b'capture'
                ]
                
                found_keywords = []
                for keyword in keywords:
                    if keyword.lower() in content.lower():
                        found_keywords.append(keyword.decode())
                
                if found_keywords:
                    print(f"🔍 Mots-clés trouvés: {', '.join(found_keywords)}")
                else:
                    print("⚠️ Aucun mot-clé webcam/USB trouvé dans l'aperçu")
                    
            else:
                print("❌ Le fichier ne semble pas être un PDF valide")
                
    except Exception as e:
        print(f"❌ Erreur lors de la lecture: {e}")

    print("\n" + "="*50)
    print("INSTRUCTIONS BASÉES SUR LE MODÈLE WOLFGANG GA100:")
    print("="*50)
    print("""
🎯 CONFIGURATION WEBCAM WOLFGANG GA100

1. ACTIVATION MODE WEBCAM:
   • Allumer la caméra Wolfgang GA100
   • Appuyer sur le bouton MENU
   • Naviguer vers: Paramètres > USB Mode
   • Sélectionner: "PC Camera" ou "UVC Mode"
   
2. CONNEXION USB:
   • Utiliser le câble USB-C fourni
   • Connecter à un port USB 3.0 (bleu) de préférence
   • Wolfgang devrait afficher "PC Camera" ou icône USB
   
3. VÉRIFICATION WINDOWS:
   • Ouvrir Gestionnaire de périphériques
   • Chercher sous "Caméras" ou "Périphériques d'imagerie"
   • Nom possible: "USB Camera", "UVC Camera", ou "Wolfgang"
   
4. TEST:
   • Ouvrir l'application Caméra Windows
   • Ou utiliser le fichier test-wolfgang-simple.html
   
5. RÉSOLUTION DE PROBLÈMES:
   • Si pas détecté: changer mode USB dans Wolfgang
   • Redémarrer Wolfgang en mode PC Camera
   • Tester autre port/câble USB
   • Redémarrer service Windows Camera Frame Server
   
💡 ASTUCE: Wolfgang GA100 supporte généralement UVC 
   (USB Video Class) qui est compatible Windows sans pilotes
""")

if __name__ == "__main__":
    analyze_pdf_info()