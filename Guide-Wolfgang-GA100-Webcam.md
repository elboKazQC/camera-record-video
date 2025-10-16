# Guide de Configuration Wolfgang GA100 comme Webcam

## Étapes de Configuration Webcam Wolfgang GA100

### 1. Mode Webcam / USB Streaming

**Procédure typique pour Wolfgang GA100 :**

1. **Allumer la caméra** - Appuyez sur le bouton Power
2. **Accéder au menu** - Généralement bouton Menu ou paramètres
3. **Chercher les options :**
   - "USB Mode" 
   - "PC Camera"
   - "Webcam Mode"
   - "Live Streaming"
   - "USB Streaming"

### 2. Configuration USB

**Types de modes USB possibles :**
- **Mass Storage** (Stockage) - ❌ Ne fonctionne pas comme webcam
- **PC Camera** - ✅ Mode webcam correct
- **USB Video** - ✅ Mode streaming
- **UVC** (USB Video Class) - ✅ Compatible avec Windows

### 3. Vérifications Physiques

**Connexion USB :**
- Utilisez le câble USB fourni avec la caméra
- Connectez directement à l'ordinateur (évitez les hubs USB)
- Préférez les ports USB 3.0 (bleus)

**État de la caméra :**
- Caméra allumée et en mode webcam
- Écran affichant le mode USB/PC Camera actif
- LED d'activité USB (si présente)

### 4. Navigation Menu Wolfgang GA100

**Navigation typique :**
```
Menu Principal
├── Paramètres / Settings
│   ├── Connexion / Connection
│   │   ├── WiFi
│   │   └── USB Mode ← SÉLECTIONNER ICI
│   │       ├── Mass Storage (Stockage)
│   │       └── PC Camera ← CHOISIR CETTE OPTION
│   └── ...
└── ...
```

### 5. Diagnostic Windows

**Si Wolfgang n'est toujours pas détecté :**

1. **Gestionnaire de périphériques** (`devmgmt.msc`)
   - Chercher dans "Caméras"
   - Chercher dans "Périphériques d'imagerie" 
   - Chercher dans "Autres périphériques" (avec point d'exclamation)

2. **Sons Windows**
   - Écoutez le son de connexion USB lors du branchement
   - Pas de son = problème de connexion physique

3. **Pilotes UVC**
   - Windows devrait reconnaître automatiquement
   - Si point d'exclamation : pilotes manquants

### 6. Solutions de Dépannage

**Problème : Pas de détection**
- Vérifier le mode USB dans les paramètres Wolfgang
- Tester un autre câble USB
- Redémarrer Wolfgang en mode PC Camera
- Tester sur un autre port USB

**Problème : Détecté mais ne fonctionne pas**
- Fermer toutes applications utilisant la caméra
- Redémarrer le service Windows Camera
- Mettre à jour les pilotes USB

**Problème : Image noire ou figée**
- Vérifier l'objectif (pas de cache)
- Réinitialiser Wolfgang
- Vérifier la résolution dans les applications

## Commandes de Test Rapide

### Test 1: Vérification USB
```cmd
# Dans le terminal Windows
wmic path Win32_PnPEntity where "DeviceID like 'USB%'" get Name,DeviceID
```

### Test 2: Services Camera
```cmd
# Redémarrer service camera
sc stop FrameServer && sc start FrameServer
```

### Test 3: Test Navigateur
Ouvrir le fichier `test-wolfgang-simple.html` créé précédemment

## Résolutions Supportées (Typiques GA100)

- **4K** : 3840x2160 (peut ne pas fonctionner en webcam)
- **1080p** : 1920x1080 ✅ Recommandé pour webcam
- **720p** : 1280x720 ✅ Bonne performance
- **VGA** : 640x480 ✅ Compatible universelle

## Applications de Test

1. **Camera Windows** (app native)
2. **Navigateur web** (test-wolfgang-simple.html)
3. **OBS Studio**
4. **VLC Media Player** > Ouvrir un périphérique de capture
5. **Zoom/Teams** (pour tester en visioconférence)

---

**Note :** Les menus exacts peuvent varier selon la version firmware de votre Wolfgang GA100. Cherchez des termes comme "USB", "PC", "Camera", "Streaming" dans les paramètres.