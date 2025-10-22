#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guide Interactif Wolfgang GA100 - Configuration Webcam
Basé sur le manuel officiel Wolfgang GA100
"""

def guide_wolfgang_ga100():
    print("🎥" + "="*60 + "🎥")
    print("       GUIDE WOLFGANG GA100 - CONFIGURATION WEBCAM")
    print("🎥" + "="*60 + "🎥")
    print()
    
    print("📋 ÉTAPES À SUIVRE DANS L'ORDRE:")
    print("-" * 40)
    
    # Étape 1: Vérification physique
    print("\n🔧 ÉTAPE 1: VÉRIFICATION PHYSIQUE")
    print("   ✓ Wolfgang GA100 est allumé")
    print("   ✓ Écran LCD fonctionne") 
    print("   ✓ Câble USB-C connecté fermement")
    print("   ✓ Port USB 3.0 (bleu) utilisé si possible")
    
    # Étape 2: Configuration Wolfgang
    print("\n⚙️  ÉTAPE 2: CONFIGURATION MODE WEBCAM")
    print("   Sur votre Wolfgang GA100:")
    print("   1️⃣ Appuyez sur le bouton MENU")
    print("   2️⃣ Naviguez avec ↑↓ vers 'Paramètres' ou 'Settings'")
    print("   3️⃣ Cherchez 'USB Mode' ou 'Connexion USB'")
    print("   4️⃣ Sélectionnez une de ces options:")
    print("      • 'PC Camera' 📹")
    print("      • 'UVC Mode' 📹") 
    print("      • 'Webcam' 📹")
    print("      • 'USB Video' 📹")
    print("   ❌ NE PAS choisir 'Mass Storage' ou 'Stockage'")
    
    # Étape 3: Vérification Windows
    print("\n🖥️  ÉTAPE 3: VÉRIFICATION WINDOWS")
    print("   Après configuration Wolfgang:")
    print("   1️⃣ Déconnecter et reconnecter le câble USB")
    print("   2️⃣ Écouter le son de connexion Windows")
    print("   3️⃣ Ouvrir Gestionnaire de périphériques:")
    print("      • Appuyer Win+R, taper: devmgmt.msc")
    print("      • Chercher sous 'Caméras'")
    print("      • Ou sous 'Périphériques d'imagerie'")
    print("      • Ou sous 'Autres périphériques' (⚠️ problème)")
    
    # Étape 4: Test fonctionnel
    print("\n🧪 ÉTAPE 4: TEST FONCTIONNEL")
    print("   Tester dans cet ordre:")
    print("   1️⃣ Application Caméra Windows (ms-camera:)")
    print("   2️⃣ Fichier test-wolfgang-simple.html (dans navigateur)")
    print("   3️⃣ OBS Studio ou logiciel streaming")
    
    print("\n" + "="*60)
    print("🚨 RÉSOLUTION DE PROBLÈMES WOLFGANG GA100")
    print("="*60)
    
    print("\n❌ PROBLÈME: Wolfgang pas détecté du tout")
    print("   🔧 SOLUTIONS:")
    print("   • Vérifier mode USB dans Wolfgang (pas Mass Storage)")
    print("   • Tester autre câble USB-C")
    print("   • Essayer port USB différent")
    print("   • Redémarrer Wolfgang complètement")
    print("   • Vérifier que Wolfgang est chargé (>20%)")
    
    print("\n❌ PROBLÈME: Détecté mais image noire")
    print("   🔧 SOLUTIONS:")
    print("   • Vérifier cache objectif retiré")
    print("   • Fermer autres apps utilisant caméra")
    print("   • Redémarrer service Windows Camera")
    print("   • Réinitialiser Wolfgang aux paramètres usine")
    
    print("\n❌ PROBLÈME: Connexion instable")
    print("   🔧 SOLUTIONS:")
    print("   • Utiliser port USB 3.0 directement (pas hub)")
    print("   • Vérifier alimentation USB suffisante")
    print("   • Mettre à jour firmware Wolfgang si disponible")
    print("   • Changer résolution webcam (1080p → 720p)")
    
    print("\n" + "="*60)
    print("📱 SPÉCIFICITÉS WOLFGANG GA100")
    print("="*60)
    print("• Résolutions webcam supportées: 4K, 1080p, 720p")
    print("• Format: UVC (USB Video Class) - pas de pilotes requis")
    print("• Compatible: Windows 10/11, Mac, Linux")
    print("• Connexion: USB-C (câble fourni)")
    print("• Mode webcam: doit être activé dans les paramètres")
    
    print("\n🎯 COMMANDES RAPIDES WINDOWS:")
    print("• Gestionnaire périphériques: Win+R → devmgmt.msc")
    print("• App Caméra: Win+R → ms-camera:")
    print("• Services: Win+R → services.msc → FrameServer")
    
    print("\n✅ Si tout fonctionne, Wolfgang apparaîtra comme 'USB Camera' ou 'Wolfgang GA100'")

if __name__ == "__main__":
    guide_wolfgang_ga100()
    
    print("\n" + "🎬" * 20)
    print("Appuyez sur Entrée pour continuer...")
    input()