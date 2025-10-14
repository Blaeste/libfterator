# 🚀 Libfterator 2025# � Libfterator 2025



[![Tests](https://img.shields.io/badge/Tests-251%2F251-brightgreen)](https://github.com/Blaeste/libfterator)

[![Norminette](https://img.shields.io/badge/Norminette-100%25-blue)](https://github.com/42School/norminette)

[![42 School](https://img.shields.io/badge/42-School-000000)](https://42.fr)



> **Testeur complet et professionnel pour la libft de l'École 42**> **Testeur complet et professionnel pour la libft de l'École 42**



Framework de test moderne, robuste et exhaustif avec **281 tests** couvrant toutes les fonctions de la libft, incluant validation Valgrind et tests de sur-protection.Un framework de test moderne, robuste et exhaustif avec **251 tests** couvrant toutes les fonctions de la libft, incluant les parties obligatoires et bonus.



## 🚀 Installation rapide## ✨ Caractéristiques



```bash### 🎯 Couverture complète

git clone https://github.com/Blaeste/libfterator.git- **📚 Partie 1** : 18 fonctions de la libc (181 tests)

cd libfterator- **🔧 Partie 2** : 11 fonctions supplémentaires (51 tests)

```- **🎁 Bonus** : 9 fonctions de listes chaînées (19 tests)



**C'est tout ! Aucune dépendance requise** - fonctionne avec Python 3.6+ (déjà installé sur les machines 42).### 🛡️ Validation rigoureuse

- ✅ **Norminette** intégrée avec vérification automatique

## 💡 Utilisation- � **Compilation** stricte (`-Wall -Wextra -Werror`)

- 🧪 **Tests exhaustifs** avec cas limites et edge cases

### Commandes essentielles- 📊 **Métriques** détaillées avec temps d'exécution

```bash

# Tester toute votre libft### 🎨 Interface moderne

./tester.py /chemin/vers/votre/libft- 🌈 **Interface colorée** et intuitive

- 📈 **Progression en temps réel** avec compteurs

# Tester une fonction spécifique- � **Logs détaillés** automatiquement sauvegardés

./tester.py /chemin/vers/libft --run strlen- 🎛️ **Options flexibles** pour filtrer et personnaliser

./tester.py /chemin/vers/libft --run memcpy

./tester.py /chemin/vers/libft --run list## 🚀 Installation et utilisation



# Mode détaillé avec logs complets### Installation rapide

./tester.py /chemin/vers/libft --verbose```bash

```git clone https://github.com/Blaeste/libfterator.git

cd libfterator

### Options avancées```

```bash

# Voir tous les tests disponibles### Utilisation basique

./tester.py /chemin/vers/libft --list```bash

# Tester toute votre libft

# Désactiver les couleurs (pour les logs)./tester.py /chemin/vers/votre/libft

./tester.py /chemin/vers/libft --no-color

```# Avec progression détaillée

./tester.py /chemin/vers/libft --verbose

## ✨ Caractéristiques

# Tester une fonction spécifique

### 🎯 Couverture exhaustive - 281 tests./tester.py /chemin/vers/libft --run strlen

- **📚 Partie 1** : 18 fonctions de la libc (149 tests)./tester.py /chemin/vers/libft --run memcpy

- **🔧 Partie 2** : 11 fonctions supplémentaires (80 tests)./tester.py /chemin/vers/libft --run list

- **🎁 Bonus** : 9 fonctions de listes chaînées (19 tests)```

- **🚰 Valgrind** : Tests de fuites mémoire (22 tests)

- **🛡️ Validation** : Tests de sur-protection (8 tests)### Recherche automatique des headers

- **✅ Norminette** : Vérification automatique de la norme

Le testeur détecte automatiquement les dossiers d'en-têtes courants (par ex. `inc/`, `include/`, `includes/`, `headers/`) ainsi que n'importe quel répertoire contenant `libft.h` sous le dossier fourni. Vous n'avez donc pas besoin de déplacer `libft.h` à la racine — placez-le simplement dans un dossier `inc/` et le testeur l'ajoutera à la ligne de compilation (`-I`).

### 🌟 Fonctionnalités avancées



#### 🔍 **Détection automatique des headers**### Options disponibles

- Recherche `libft.h` dans `inc/`, `include/`, `includes/`, `headers/````bash

- Détection récursive dans tout le projet# Afficher tous les tests disponibles

- Ajout automatique des flags `-I` appropriés./tester.py /chemin/vers/libft --list

- **Plus besoin de déplacer libft.h à la racine !**

# Désactiver les couleurs

#### 🚰 **Tests Valgrind intégrés**./tester.py /chemin/vers/libft --no-color

- Détection automatique des fuites mémoire

- Tests spécialisés pour `calloc`, `strdup`, `split`, `itoa`, `strmapi`# Mode sécurisé (sans modifications temporaires)

- Tests des fonctions bonus de listes./tester.py /chemin/vers/libft --safe

- Fallback gracieux si Valgrind n'est pas installé```



#### 🛡️ **Tests de sur-protection**## 📊 Exemple de sortie

- Vérification que les fonctions crashent avec des pointeurs NULL

- Tests de `strlen`, `strchr`, `strrchr`, `strncmp`, `memcpy`, etc.```

- Détection des implémentations trop protégées╔═════════════════════════════════════════════════════════════════════════════════╗

- Section dédiée séparée des tests normaux║                                Libfterator 2025                                 ║

║                          Testeur complet pour la libft                          ║

#### 🎨 **Interface moderne**║                            251 tests • 3 sections                               ║

- Sections organisées avec sous-sections par fonction╚═════════════════════════════════════════════════════════════════════════════════╝

- Progression en temps réel avec compteurs détaillés

- Codes couleur pour les statuts (PASS ✅, FAIL ❌, LEAK 🚰)==================================================================================

- Logs automatiques sauvegardés avec horodatage|                             NORMINETTE CHECK                                    |

==================================================================================

## 📊 Exemple de sortie [norm] check ................................................... ✅ PASS (547 ms)



```==================================================================================

╔═════════════════════════════════════════════════════════════════════════════════╗|                              COMPILING LIBFT                                   |

║                                Libfterator 2025                                 ║==================================================================================

║                          Testeur complet pour la libft                          ║→ Build libft… OK

║                            281 tests • 5 sections                               ║

╚═════════════════════════════════════════════════════════════════════════════════╝Running 251 test(s)



====================================================================================================================================================================

|                             NORMINETTE CHECK                                    |🔹 PARTIE 1 — Fonctions de la libc

====================================================================================================================================================================

 [norm] check ................................................... ✅ PASS (376 ms)

 [ 1/251] atoi/basic_positive ..................................... ✅ PASS (0 ms)

================================================================================== [ 2/251] atoi/basic_negative ..................................... ✅ PASS (0 ms)

🔹 PARTIE 1 — Fonctions de la libc [ 3/251] atoi/with_plus .......................................... ✅ PASS (0 ms)

================================================================================== [...]



────────────────────────────────────────────────────────────Résumé — 251/251 PASS

📂 strlen — Longueur de chaîneTous les tests passent.

────────────────────────────────────────────────────────────```



 [ 1/281] strlen/basic ............................................. ✅ PASS (0 ms)## 🧪 Tests inclus

 [ 2/281] strlen/empty ............................................. ✅ PASS (0 ms)

 [...]<details>

<summary><strong>📚 Partie 1 - Fonctions de la libc (181 tests)</strong></summary>

==================================================================================

🔹 VALGRIND — Tests de fuites mémoire- `ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`

==================================================================================- `ft_strlen`, `ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`

- `ft_strlcpy`, `ft_strlcat`, `ft_toupper`, `ft_tolower`

────────────────────────────────────────────────────────────- `ft_strchr`, `ft_strrchr`, `ft_strncmp`, `ft_memchr`, `ft_memcmp`

📂 valgrind — Tests de fuites mémoire- `ft_strnstr`, `ft_atoi`, `ft_calloc`, `ft_strdup`

────────────────────────────────────────────────────────────

</details>

 [252/281] valgrind/calloc_basic ................................... ✅ PASS (460 ms)

 [253/281] valgrind/itoa_positive .................................. 🚰 LEAK (455 ms)<details>

 [...]<summary><strong>🔧 Partie 2 - Fonctions supplémentaires (51 tests)</strong></summary>



Résumé — 278/281 PASS • 3 LEAK- `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`

```- `ft_itoa`, `ft_strmapi`, `ft_striteri`

- `ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`

## 🧪 Tests inclus

</details>

<details>

<summary><strong>📚 Partie 1 - Fonctions de la libc (149 tests)</strong></summary><details>

<summary><strong>🎁 Bonus - Listes chaînées (19 tests)</strong></summary>

- **Classification** : `ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`

- **Conversion** : `ft_toupper`, `ft_tolower`- `ft_lstnew`, `ft_lstadd_front`, `ft_lstsize`, `ft_lstlast`

- **Chaînes** : `ft_strlen`, `ft_strchr`, `ft_strrchr`, `ft_strncmp`, `ft_strnstr`- `ft_lstadd_back`, `ft_lstdelone`, `ft_lstclear`

- **Mémoire** : `ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`, `ft_memchr`, `ft_memcmp`- `ft_lstiter`, `ft_lstmap`

- **Copie sécurisée** : `ft_strlcpy`, `ft_strlcat`

- **Conversion** : `ft_atoi`</details>

- **Allocation** : `ft_calloc`, `ft_strdup`

## 📋 Fonctionnalités avancées

</details>

### 📝 Système de logs automatique

<details>Chaque exécution génère un log détaillé dans `out/` :

<summary><strong>🔧 Partie 2 - Fonctions supplémentaires (80 tests)</strong></summary>- ✅ Résultats de norminette avec sorties complètes

- 🔧 Logs de compilation avec messages d'erreur

- **Manipulation** : `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`- 🧪 Résultats des tests avec durées d'exécution

- **Conversion** : `ft_itoa`- 📊 Statistiques complètes et résumés

- **Application** : `ft_strmapi`, `ft_striteri`

- **Écriture** : `ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`### 🎯 Tests intelligents

- **Cas limites** : Pointeurs NULL, chaînes vides, débordements

</details>- **Edge cases** : Valeurs min/max, caractères spéciaux

- **Comparaison libc** : Validation contre les fonctions standard

<details>- **Gestion mémoire** : Tests d'allocation/libération

<summary><strong>🎁 Bonus - Listes chaînées (19 tests)</strong></summary>

### 🔧 Compilation rigoureuse

- **Création** : `ft_lstnew`, `ft_lstadd_front`, `ft_lstadd_back`- Flags stricts : `-Wall -Wextra -Werror`

- **Navigation** : `ft_lstsize`, `ft_lstlast`- Support des différents compileurs

- **Suppression** : `ft_lstdelone`, `ft_lstclear`- Vérification du Makefile

- **Manipulation** : `ft_lstiter`, `ft_lstmap`- Tests de toutes les règles (`all`, `clean`, `fclean`, `re`, `bonus`)



</details>## 🤝 Contribution



<details>Les contributions sont les bienvenues ! N'hésitez pas à :

<summary><strong>🚰 Valgrind - Tests de fuites mémoire (22 tests)</strong></summary>

1. **Fork** le projet

- **Allocation simple** : `calloc`, `strdup`, `substr`, `strjoin`, `strtrim`2. Créer une **branch** pour votre feature

- **Allocation complexe** : `split`, `itoa`, `strmapi`3. **Commit** vos changements

- **Listes chaînées** : `lstnew`, `lstclear`, `lstmap`4. **Push** vers votre branch

- **Cas limites** : Allocations vides, échecs d'allocation5. Ouvrir une **Pull Request**



</details>## 📞 Support



<details>- � **Issues** : [GitHub Issues](https://github.com/Blaeste/libfterator/issues)

<summary><strong>🛡️ Validation - Tests de sur-protection (8 tests)</strong></summary>- 💬 **Discussions** : [GitHub Discussions](https://github.com/Blaeste/libfterator/discussions)

- � **Contact** : Via GitHub

- **Crash attendus** : `strlen`, `strchr`, `strrchr`, `strncmp`

- **Pointeurs NULL** : `memcpy`, `memset`, `memmove`, `atoi`## 📄 License

- **Détection** : Fonctions trop protégées qui ne crashent pas

Ce projet est sous license [MIT](LICENSE).

</details>

## 🙏 Remerciements

## 🛠️ Fonctionnalités techniques

- **École 42** pour le projet libft

### 📝 Système de logs automatique- La **communauté 42** pour les retours et améliorations

- **Horodatage** : Chaque session avec timestamp unique- Tous les **contributeurs** du projet

- **Norminette** : Sortie complète des vérifications

- **Compilation** : Messages d'erreur détaillés---

- **Tests** : Résultats avec temps d'exécution

- **Statistiques** : Résumés et métriques complètes<div align="center">



### 🔧 Compilation intelligente**⭐ N'oubliez pas de mettre une étoile si ce projet vous aide ! ⭐**

- **Détection automatique** des répertoires d'en-têtes

- **Flags stricts** : `-Wall -Wextra -Werror`[🏠 Accueil](https://github.com/Blaeste/libfterator) • [📖 Documentation](https://github.com/Blaeste/libfterator/wiki) • [🐛 Issues](https://github.com/Blaeste/libfterator/issues)

- **Makefile** : Vérification de toutes les règles

- **Bonus** : Compilation automatique si détectée</div>

- **Fallback** : Gestion gracieuse des erreurs

### 🚫 Protection contre les fichiers de test
- **Norminette** : Ignore automatiquement `tester.py`, `tests/`, etc.
- **Analyse ciblée** : Seulement les fichiers `.c` et `.h`
- **Compatibilité** : Fonctionne même si le testeur est dans le dossier libft

## 🤝 Contribution et support

### 🧪 Beta testeurs
Un grand merci aux beta testeurs qui ont contribué à améliorer ce projet !

### 💡 Contribuer
1. **Fork** le projet
2. Créer une **branche** pour votre fonctionnalité
3. **Commit** vos changements
4. **Push** et ouvrir une **Pull Request**

### 📞 Support
- 🐛 **Issues** : [GitHub Issues](https://github.com/Blaeste/libfterator/issues)
- 💬 **Discussions** : [GitHub Discussions](https://github.com/Blaeste/libfterator/discussions)

## 📄 License

Ce projet est sous licence [MIT](LICENSE).

---

<div align="center">

**⭐ N'oubliez pas de mettre une étoile si ce projet vous aide ! ⭐**

[🏠 Accueil](https://github.com/Blaeste/libfterator) • [📖 Wiki](https://github.com/Blaeste/libfterator/wiki) • [🐛 Issues](https://github.com/Blaeste/libfterator/issues)

</div>
