# WOLFGANG GA100 - SOLUTION GRATUITE WEBCAM VIA WIFI

## 🎯 OBJECTIF
Utiliser Wolfgang GA100 comme webcam GRATUITEMENT via WiFi + OBS

---

## 📋 ÉTAPE 1 : ACTIVER LE WIFI SUR WOLFGANG

### Sur votre Wolfgang GA100 :

1. **Allumez Wolfgang**
2. **Appuyez sur MENU**
3. **Naviguez vers WiFi** (ou Wireless/Sans-fil)
4. **Activez le WiFi**
5. **Notez les informations affichées :**
   - Nom du réseau (SSID) : `Wolfgang_XXXXX`
   - Mot de passe : `12345678` (ou celui affiché)

---

## 📋 ÉTAPE 2 : CONNECTER LE PC AU WIFI WOLFGANG

### Sur Windows :

1. **Cliquez sur l'icône WiFi** (barre des tâches)
2. **Cherchez le réseau Wolfgang** (ex: `Wolfgang_GA100` ou `SSID_XXXXX`)
3. **Cliquez sur Connexion**
4. **Entrez le mot de passe** affiché sur Wolfgang
5. **Confirmez la connexion**

⚠️ **Note** : Votre PC sera déconnecté d'Internet pendant ce temps

---

## 📋 ÉTAPE 3 : INSTALLER L'APPLICATION WOLFGANG

### Option A : Application Mobile sur PC (via émulateur)

Si l'app Wolfgang n'existe pas pour PC, utilisez votre téléphone :

1. **Sur smartphone** : Téléchargez "iSmart DV" ou "Wolfgang Action Cam"
2. **Connectez smartphone au WiFi Wolfgang**
3. **Ouvrez l'app** → Live View
4. **Affichez l'image sur grand écran** ou utilisez option B

### Option B : Via Navigateur Web (Préféré pour PC)

1. **Ouvrez votre navigateur** (Chrome, Edge, Firefox)
2. **Essayez ces adresses :**
   - `http://192.168.1.1`
   - `http://192.168.0.1`
   - `http://192.168.42.1`
   - `http://10.0.0.1`

3. **Interface web Wolfgang devrait s'ouvrir**
4. **Cherchez "Live View" ou "Aperçu en direct"**

---

## 📋 ÉTAPE 4 : INSTALLER OBS STUDIO

### Téléchargement :

1. **Allez sur** : https://obsproject.com/
2. **Téléchargez OBS Studio** (gratuit)
3. **Installez** avec les paramètres par défaut
4. **Lancez OBS Studio**

---

## 📋 ÉTAPE 5 : CONFIGURER OBS POUR CAPTURER WOLFGANG

### Dans OBS Studio :

1. **Section "Sources"** (en bas)
2. **Cliquez sur "+"** (Ajouter)
3. **Choisissez selon votre méthode :**

#### Si vous utilisez le navigateur web :
   - Sélectionnez **"Capture de fenêtre"**
   - Nommez : "Wolfgang Live"
   - Fenêtre : Sélectionnez votre navigateur avec Wolfgang
   - OK

#### Si vous utilisez l'app smartphone mirrorée :
   - Sélectionnez **"Capture d'écran"**
   - Ou utilisez logiciel de mirroring (ex: scrcpy pour Android)

4. **Ajustez la zone de capture** pour montrer uniquement la vidéo Wolfgang

---

## 📋 ÉTAPE 6 : ACTIVER LA CAMÉRA VIRTUELLE OBS

### Dans OBS Studio :

1. **Menu Outils** (en haut)
2. **Cliquez sur "Démarrer la caméra virtuelle"**
3. **OBS est maintenant une webcam !**

### Utilisation dans Zoom/Teams/Discord :

1. **Ouvrez votre application** (Zoom, Teams, etc.)
2. **Paramètres Vidéo**
3. **Caméra** : Sélectionnez **"OBS Virtual Camera"**
4. **Vous voyez maintenant Wolfgang !**

---

## 🔧 CONFIGURATION AVANCÉE OBS

### Améliorer la qualité :

1. **Dans OBS, clic droit sur source Wolfgang**
2. **Filtres**
3. **Ajouter :**
   - Correction des couleurs
   - Netteté
   - Suppression du bruit

### Désactiver les overlays Wolfgang :

Sur Wolfgang : Menu → Display → OSD → Off

---

## ⚠️ LIMITATIONS DE CETTE MÉTHODE

**Inconvénients :**
- ❌ Latence de 1-3 secondes (retard)
- ❌ Qualité réduite vs HDMI
- ❌ Pas d'internet sur PC pendant l'utilisation
- ❌ Connexion peut être instable
- ❌ Batterie Wolfgang se décharge

**Avantages :**
- ✅ Complètement gratuit
- ✅ Pas de matériel supplémentaire
- ✅ Fonctionne immédiatement
- ✅ Portable (pas de câbles)

---

## 🎬 ALTERNATIVE : OBS + DROIDCAM (Si vous avez un smartphone)

Si Wolfgang WiFi ne fonctionne pas bien, utilisez votre smartphone :

1. **Installez DroidCam** sur smartphone + PC
2. **Utilisez smartphone comme webcam** (gratuit, meilleure qualité)
3. **Wolfgang reste pour enregistrements** sur carte SD

---

## 💡 SOLUTION RECOMMANDÉE FINALE

### Pour usage occasionnel :
**WiFi + OBS** (méthode ci-dessus)

### Pour usage régulier/professionnel :
**Carte capture HDMI** (20-40€ pour modèle basique)

```
Wolfgang HDMI → Carte capture USB → PC
```

**Cartes recommandées :**
- Générique USB 3.0 HDMI (Amazon, ~25€)
- Détectée automatiquement comme webcam
- Aucun logiciel requis
- Qualité 1080p 60fps
- Pas de latence

---

## 📞 COMMANDES POUR TESTER

### Ouvrir OBS après installation :
```powershell
Start-Process "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
```

### Vérifier si OBS Virtual Camera est détectée :
```powershell
Get-WmiObject Win32_PnPEntity | Where-Object {$_.Name -like "*OBS*"}
```

---

## ✅ CHECKLIST DE CONFIGURATION

- [ ] Wolfgang WiFi activé
- [ ] PC connecté au WiFi Wolfgang  
- [ ] Interface web Wolfgang accessible (192.168.x.x)
- [ ] OBS Studio installé
- [ ] Source capture ajoutée dans OBS
- [ ] Caméra virtuelle OBS démarrée
- [ ] Testée dans application (Zoom/Teams/etc.)

---

## 🚀 PROCHAINES ÉTAPES

Testez cette méthode maintenant, puis décidez si vous voulez investir dans une carte capture HDMI pour meilleure qualité.

**Budget carte capture : 20-40€** pour qualité professionnelle sans latence.
