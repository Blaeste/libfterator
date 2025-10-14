# 🚀 Libfterator 2025

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/Tests-281%2F281-brightgreen)](https://github.com/Blaeste/libfterator)
[![Norminette](https://img.shields.io/badge/Norminette-100%25-blue)](https://github.com/42School/norminette)
[![42 School](https://img.shields.io/badge/42-School-000000)](https://42.fr)

> Testeur complet et professionnel pour la libft de l'École 42 — 281 tests, Valgrind intégré, sur-protection, interface lisible et logs détaillés.

## ⚡ Installation ultra-rapide (copier/coller)

```bash
git clone https://github.com/Blaeste/libfterator.git
cd libfterator
```

```bash
./tester.py /chemin/vers/votre/libft
# Exemple: ./tester.py ../libft
```

**C'est tout ! Aucune dépendance requise.** Fonctionne avec Python 3.6+ (installé par défaut sur les machines 42).

---

## ✨ Points forts

- ✅ Norminette intégrée (vérification automatique)
- 🧪 281 tests exhaustifs avec cas limites et edge cases
- 🔒 Validation de sur-protection (NULL pointers attendus)
- 🚰 Valgrind intégré avec fallback si non installé
- 🎨 Interface claire avec sous-sections par fonction
- 🧾 Logs complets horodatés et métriques détaillées

## 🎯 Couverture des tests (281)

- 📚 Partie 1 — Fonctions de la libc: 149 tests
- 🔧 Partie 2 — Fonctions supplémentaires: 80 tests
- 🎁 Bonus — Listes chaînées: 19 tests
- 🚰 Valgrind — Fuites mémoire: 22 tests
- 🛡️ Validation — Sur-protection: 8 tests

## 💡 Utilisation rapide

```bash
# Lister tous les tests disponibles
./tester.py /chemin/vers/libft --list

# Exécuter tous les tests
./tester.py /chemin/vers/libft

# Exécuter une fonction spécifique
./tester.py /chemin/vers/libft --run strlen
./tester.py /chemin/vers/libft --run memcpy
./tester.py /chemin/vers/libft --run list

# Mode verbeux (progression + logs complets)
./tester.py /chemin/vers/libft --verbose

# Désactiver les couleurs (pratique pour les logs CI)
./tester.py /chemin/vers/libft --no-color

# Mode sécurisé (aucune modif temporaire côté projet)
./tester.py /chemin/vers/libft --safe
```

## 🧰 Options

- --list: affiche tous les tests disponibles et leur nom exécutable
- --run <nom>: exécute une sous-section (ex: strlen, memcpy, list)
- --verbose: affiche la progression détaillée et les logs complets
- --no-color: désactive les couleurs (utile pour la CI/logs)
- --safe: n’écrit rien dans le projet testé (mode lecture seule)

## 🌟 Fonctionnalités avancées

### 🔍 Détection automatique des headers
- Recherche de `libft.h` dans `inc/`, `include/`, `includes/`, `headers/` et sous-dossiers
- Ajout automatique des `-I` nécessaires à la compilation
- Pas besoin de déplacer `libft.h` à la racine

### 🚰 Tests Valgrind intégrés
- Détection des fuites mémoire avec `--leak-check=full` et code retour d’erreur dédié
- Couverture spécifique: `calloc`, `strdup`, `substr`, `strjoin`, `strtrim`, `split`, `itoa`, `strmapi`, et fonctions bonus de listes
- Fallback gracieux si Valgrind est absent (les tests fonctionnent quand même)

### 🛡️ Tests de sur-protection
- Vérifie que certaines fonctions crashent sur `NULL` (comportement attendu par la libft)
- Section séparée des tests normaux pour une lecture claire

### 🎨 Interface lisible
- Affichage hiérarchique avec sous-sections par fonction (📂)
- Codes couleur: PASS ✅, FAIL ❌, LEAK 🚰
- Compteurs de progression et résumés en fin d’exécution

### 🧾 Système de logs
- Tous les résultats sont sauvegardés dans `out/` avec horodatage
- Logs norminette, compilation, exécution et métriques

### 🧩 Compatibilité
- Linux (recommandé) et WSL: support complet; Valgrind disponible via le gestionnaire de paquets
- macOS: fonctionnement OK; Valgrind n’est pas installé par défaut (fallback automatique)
- Windows natif: utilisez WSL pour une expérience optimale

### ❓ FAQ rapide
- Valgrind n’est pas installé ? Les tests s’exécutent quand même, mais sans détection de fuites (fallback). Installez-le via votre gestionnaire de paquets pour activer la section fuites mémoire.
- Où sont les logs ? Dans le dossier `out/`, avec un horodatage par session.
- Faut-il déplacer `libft.h` ? Non. Le testeur détecte automatiquement les répertoires d’en-têtes et ajoute les `-I`.

## 🖥️ Pré-requis

- Python 3.6+ (par défaut sur Linux des machines 42)
- Environnement POSIX (Linux/WSL conseillé). Valgrind est recommandé mais optionnel.

## 🧪 Exemple de sortie (extrait)

```
╔══════════════════════════════════════════════════════════════════╗
║                          Libfterator 2025                        ║
║                   281 tests • 5 sections • color                 ║
╚══════════════════════════════════════════════════════════════════╝

[norm] check ................................................ PASS
🔹 PARTIE 1 — Fonctions de la libc
	📂 strlen
	 [ 1/281] basic ......................................... PASS
	 [ 2/281] empty ......................................... PASS
...
Résumé — 281/281 PASS • 0 LEAK
```

## 🤝 Beta testeurs et support

- Un grand merci aux beta testeurs qui ont aidé à stabiliser ce projet 🙌
- Issues: https://github.com/Blaeste/libfterator/issues
- Discussions: https://github.com/Blaeste/libfterator/discussions

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE.

---

<div align="center">

⭐ Si ce projet vous aide, pensez à lui mettre une étoile ⭐

[🏠 Accueil](https://github.com/Blaeste/libfterator) • [🐛 Issues](https://github.com/Blaeste/libfterator/issues)

</div>

