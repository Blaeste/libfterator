# � Libfterator 2025

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/Tests-251%2F251-brightgreen)](https://github.com/Blaeste/libfterator)
[![Norminette](https://img.shields.io/badge/Norminette-100%25-blue)](https://github.com/42School/norminette)
[![42 School](https://img.shields.io/badge/42-School-000000)](https://42.fr)

> **Testeur complet et professionnel pour la libft de l'École 42**

Un framework de test moderne, robuste et exhaustif avec **251 tests** couvrant toutes les fonctions de la libft, incluant les parties obligatoires et bonus.

## ✨ Caractéristiques

### 🎯 Couverture complète
- **📚 Partie 1** : 18 fonctions de la libc (181 tests)
- **🔧 Partie 2** : 11 fonctions supplémentaires (51 tests)
- **🎁 Bonus** : 9 fonctions de listes chaînées (19 tests)

### 🛡️ Validation rigoureuse
- ✅ **Norminette** intégrée avec vérification automatique
- � **Compilation** stricte (`-Wall -Wextra -Werror`)
- 🧪 **Tests exhaustifs** avec cas limites et edge cases
- 📊 **Métriques** détaillées avec temps d'exécution

### 🎨 Interface moderne
- 🌈 **Interface colorée** et intuitive
- 📈 **Progression en temps réel** avec compteurs
- � **Logs détaillés** automatiquement sauvegardés
- 🎛️ **Options flexibles** pour filtrer et personnaliser

## 🚀 Installation et utilisation

### Installation rapide
```bash
git clone https://github.com/Blaeste/libfterator.git
cd libfterator
```

### Utilisation basique
```bash
# Tester toute votre libft
./tester.py /chemin/vers/votre/libft

# Avec progression détaillée
./tester.py /chemin/vers/libft --verbose

# Tester une fonction spécifique
./tester.py /chemin/vers/libft --run strlen
./tester.py /chemin/vers/libft --run memcpy
./tester.py /chemin/vers/libft --run list
```

### Recherche automatique des headers

Le testeur détecte automatiquement les dossiers d'en-têtes courants (par ex. `inc/`, `include/`, `includes/`, `headers/`) ainsi que n'importe quel répertoire contenant `libft.h` sous le dossier fourni. Vous n'avez donc pas besoin de déplacer `libft.h` à la racine — placez-le simplement dans un dossier `inc/` et le testeur l'ajoutera à la ligne de compilation (`-I`).


### Options disponibles
```bash
# Afficher tous les tests disponibles
./tester.py /chemin/vers/libft --list

# Désactiver les couleurs
./tester.py /chemin/vers/libft --no-color

# Mode sécurisé (sans modifications temporaires)
./tester.py /chemin/vers/libft --safe
```

## 📊 Exemple de sortie

```
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                Libfterator 2025                                 ║
║                          Testeur complet pour la libft                          ║
║                            251 tests • 3 sections                               ║
╚═════════════════════════════════════════════════════════════════════════════════╝

==================================================================================
|                             NORMINETTE CHECK                                    |
==================================================================================
 [norm] check ................................................... ✅ PASS (547 ms)

==================================================================================
|                              COMPILING LIBFT                                   |
==================================================================================
→ Build libft… OK

Running 251 test(s)

==================================================================================
🔹 PARTIE 1 — Fonctions de la libc
==================================================================================

 [ 1/251] atoi/basic_positive ..................................... ✅ PASS (0 ms)
 [ 2/251] atoi/basic_negative ..................................... ✅ PASS (0 ms)
 [ 3/251] atoi/with_plus .......................................... ✅ PASS (0 ms)
 [...]

Résumé — 251/251 PASS
Tous les tests passent.
```

## 🧪 Tests inclus

<details>
<summary><strong>📚 Partie 1 - Fonctions de la libc (181 tests)</strong></summary>

- `ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`
- `ft_strlen`, `ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`
- `ft_strlcpy`, `ft_strlcat`, `ft_toupper`, `ft_tolower`
- `ft_strchr`, `ft_strrchr`, `ft_strncmp`, `ft_memchr`, `ft_memcmp`
- `ft_strnstr`, `ft_atoi`, `ft_calloc`, `ft_strdup`

</details>

<details>
<summary><strong>🔧 Partie 2 - Fonctions supplémentaires (51 tests)</strong></summary>

- `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`
- `ft_itoa`, `ft_strmapi`, `ft_striteri`
- `ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`

</details>

<details>
<summary><strong>🎁 Bonus - Listes chaînées (19 tests)</strong></summary>

- `ft_lstnew`, `ft_lstadd_front`, `ft_lstsize`, `ft_lstlast`
- `ft_lstadd_back`, `ft_lstdelone`, `ft_lstclear`
- `ft_lstiter`, `ft_lstmap`

</details>

## 📋 Fonctionnalités avancées

### 📝 Système de logs automatique
Chaque exécution génère un log détaillé dans `out/` :
- ✅ Résultats de norminette avec sorties complètes
- 🔧 Logs de compilation avec messages d'erreur
- 🧪 Résultats des tests avec durées d'exécution
- 📊 Statistiques complètes et résumés

### 🎯 Tests intelligents
- **Cas limites** : Pointeurs NULL, chaînes vides, débordements
- **Edge cases** : Valeurs min/max, caractères spéciaux
- **Comparaison libc** : Validation contre les fonctions standard
- **Gestion mémoire** : Tests d'allocation/libération

### 🔧 Compilation rigoureuse
- Flags stricts : `-Wall -Wextra -Werror`
- Support des différents compileurs
- Vérification du Makefile
- Tests de toutes les règles (`all`, `clean`, `fclean`, `re`, `bonus`)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. **Fork** le projet
2. Créer une **branch** pour votre feature
3. **Commit** vos changements
4. **Push** vers votre branch
5. Ouvrir une **Pull Request**

## 📞 Support

- � **Issues** : [GitHub Issues](https://github.com/Blaeste/libfterator/issues)
- 💬 **Discussions** : [GitHub Discussions](https://github.com/Blaeste/libfterator/discussions)
- � **Contact** : Via GitHub

## 📄 License

Ce projet est sous license [MIT](LICENSE).

## 🙏 Remerciements

- **École 42** pour le projet libft
- La **communauté 42** pour les retours et améliorations
- Tous les **contributeurs** du projet

---

<div align="center">

**⭐ N'oubliez pas de mettre une étoile si ce projet vous aide ! ⭐**

[🏠 Accueil](https://github.com/Blaeste/libfterator) • [📖 Documentation](https://github.com/Blaeste/libfterator/wiki) • [🐛 Issues](https://github.com/Blaeste/libfterator/issues)

</div>
