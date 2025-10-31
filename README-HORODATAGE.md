# Overlay d'horodatage pour OBS Studio

Ce fichier HTML permet d'afficher la date et l'heure en temps réel dans vos enregistrements OBS.

## 📋 Installation dans OBS

### Étape 1 : Ajouter la source dans OBS
1. Ouvrez **OBS Studio**
2. Dans la section **Sources**, cliquez sur le bouton **+** (Ajouter)
3. Sélectionnez **Navigateur** (Browser)
4. Donnez-lui un nom (ex: "Horodatage")
5. Cliquez sur **OK**

### Étape 2 : Configurer la source
1. Dans **Local file**, cochez la case
2. Cliquez sur **Parcourir** et sélectionnez le fichier `obs-timestamp-overlay.html`
3. Réglez la **Largeur** : 600
4. Réglez la **Hauteur** : 200
5. Cochez **Rafraîchir le navigateur lorsque la scène devient active**
6. Cliquez sur **OK**

### Étape 3 : Positionner l'overlay
1. Déplacez et redimensionnez l'overlay dans votre scène
2. Positionnez-le où vous le souhaitez (coin supérieur gauche recommandé)

## 🎨 Personnalisation

### Changer les couleurs
Ouvrez le fichier HTML et modifiez la section `<style>` :

```css
#timestamp {
    color: #ffffff;  /* Changez cette couleur */
}
```

### Changer la taille du texte
```css
.date {
    font-size: 24px;  /* Taille de la date */
}

.time {
    font-size: 48px;  /* Taille de l'heure */
}
```

### Activer un style prédéfini
Dans le fichier HTML, à la fin du script JavaScript, décommentez une ligne :

```javascript
// Pour un fond semi-transparent :
document.getElementById('timestamp').classList.add('with-background');

// Pour un style néon :
// document.getElementById('timestamp').classList.add('neon');
```

### Modifier le format de date/heure
Dans la section JavaScript, modifiez `config` :

```javascript
const config = {
    locale: 'fr-FR',  // Changez la langue ici
    dateFormat: {
        weekday: 'long',    // 'long', 'short', ou omettez cette ligne
        year: 'numeric',
        month: 'long',      // 'long', 'short', 'numeric'
        day: 'numeric'
    },
    timeFormat: {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false       // true pour format 12h (AM/PM)
    }
};
```

## 🎯 Formats d'affichage disponibles

### Format actuel (par défaut)
```
lundi 28 octobre 2024
14:35:27
```

### Format court
Modifiez `dateFormat` :
```javascript
dateFormat: {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
}
// Résultat : 28/10/2024
```

### Format avec millisecondes
Ajoutez dans `timeFormat` :
```javascript
timeFormat: {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    fractionalSecondDigits: 3
}
```

### Format compact (une seule ligne)
Dans le HTML, modifiez :
```html
<div id="timestamp" class="compact">
    <span id="date"></span> - <span id="time"></span>
</div>
```

## 💡 Conseils

- **Transparence** : L'arrière-plan est transparent par défaut, parfait pour les overlays
- **Performances** : Le script est optimisé et ne consomme presque pas de ressources
- **Positionnement** : Vous pouvez créer plusieurs sources avec des styles différents
- **Chrome clé** : Si besoin, utilisez le filtre "Chrome Key" pour la transparence avancée

## 🔧 Dépannage

### L'horodatage ne s'affiche pas
- Vérifiez que le chemin du fichier est correct
- Assurez-vous que "Local file" est coché dans les paramètres de la source

### L'heure ne se met pas à jour
- Cochez "Rafraîchir le navigateur lorsque la scène devient active"
- Redémarrez OBS

### Le texte est trop petit/grand
- Ajustez les valeurs `font-size` dans le CSS
- Ou redimensionnez la source directement dans OBS

## 📁 Fichiers inclus

- `obs-timestamp-overlay.html` - Overlay principal
- `README-HORODATAGE.md` - Ce fichier d'instructions

## 🌐 Compatibilité

- ✅ OBS Studio 27.0+
- ✅ Windows / macOS / Linux
- ✅ Tous les formats d'enregistrement

---

**Bon enregistrement ! 🎥**
