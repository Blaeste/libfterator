#!/usr/bin/env python3
"""
Testeur Libft — version colorée et modulaire
Chaque fichier de tests se trouve dans tests/ et expose TESTS = [(nom, code_C), ...]
Usage :
    ./tester.py /chemin/vers/libft [--verbose] [--list] [--run PATTERN] [--no-color]
"""
import os, sys, subprocess, time, importlib.util, shutil, datetime, logging
from pathlib import Path

# ===============================================================
# 🎨 Pretty print (sans dépendances externes)
# ===============================================================
USE_COLOR = sys.stdout.isatty() and "--no-color" not in sys.argv
def C(code): return f"\033[{code}m" if USE_COLOR else ""
CLR = {
    "dim": C("2"),
    "reset": C("0"),
    "cyan": C("36"),
    "green": C("32"),
    "red": C("31"),
    "yellow": C("33"),
    "bold": C("1"),
    "gray": C("90"),
}
def icon(status):
    if status == "PASS": return "✅"
    if status == "FAIL": return "❌"
    if status == "LEAK": return "🚰"  # Icône pour les fuites mémoire
    if status == "TIMEOUT": return "⏰"  # Icône pour les timeouts
    return "💥"
def color_status(s):
    if s == "PASS": return f"{CLR['green']}{s}{CLR['reset']}"
    if s == "FAIL": return f"{CLR['red']}{s}{CLR['reset']}"
    if s == "LEAK": return f"{CLR['red']}{s}{CLR['reset']}"  # Rouge pour les fuites
    if s == "TIMEOUT": return f"{CLR['yellow']}{s}{CLR['reset']}"  # Jaune pour les timeouts
    return f"{CLR['yellow']}{s}{CLR['reset']}"
def human_ms(ms): return f"{ms} ms"

# ===============================================================
# 📝 Système de logging
# ===============================================================
def setup_logging(out_dir):
    """Configure le système de logging pour enregistrer tous les résultats."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = out_dir / f"libfterator_{timestamp}.log"

    # Configuration du logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
        ]
    )

    logger = logging.getLogger('libfterator')
    logger.info("=" * 80)
    logger.info("NOUVELLE SESSION LIBFTERATOR 2025")
    logger.info("=" * 80)

    return log_file, logger

def log_norminette_result(logger, result, output, error):
    """Enregistre les résultats de la norminette."""
    logger.info("NORMINETTE CHECK:")
    if result == 0:
        logger.info("✅ NORMINETTE: PASS")
    else:
        logger.error("❌ NORMINETTE: FAIL")
        if output:
            logger.error(f"Sortie norminette:\n{output}")
        if error:
            logger.error(f"Erreur norminette:\n{error}")

def log_test_result(logger, test_name, status, duration, error_output=None):
    """Enregistre le résultat d'un test."""
    if status == "PASS":
        status_icon = "✅"
    elif status == "TIMEOUT":
        status_icon = "⏰"
    else:
        status_icon = "❌"

    logger.info(f"{status_icon} {test_name}: {status} ({duration} ms)")
    if error_output:
        logger.error(f"Erreur de compilation pour {test_name}:\n{error_output}")
    if status == "TIMEOUT":
        logger.warning(f"⚠️ Test {test_name} interrompu après timeout - possible boucle infinie")

def log_compilation_result(logger, success, output=None, error=None):
    """Enregistre les résultats de compilation."""
    if success:
        logger.info("✅ COMPILATION: SUCCESS")
    else:
        logger.error("❌ COMPILATION: FAILED")
        if output:
            logger.error(f"Sortie compilation:\n{output}")
        if error:
            logger.error(f"Erreur compilation:\n{error}")

# ===============================================================
# 🎨 En-tête du programme
# ===============================================================
def print_header():
    """Affiche l'en-tête stylisé du programme."""
    print(f"{CLR['red']}╔═════════════════════════════════════════════════════════════════════════════════╗{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}{CLR['bold']}                                Libfterator 2025{CLR['reset']}{CLR['red']}                                 ║{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}                          Testeur complet pour la libft                          {CLR['red']}║{CLR['reset']}")
    print(f"{CLR['red']}║{CLR['reset']}{CLR['dim']}                            329 tests • 4 sections{CLR['reset']}{CLR['red']}                               ║{CLR['reset']}")
    print(f"{CLR['red']}╚═════════════════════════════════════════════════════════════════════════════════╝{CLR['reset']}")
    print()

    # Guide des commandes disponibles
    print(f"{CLR['dim']}Commandes disponibles :{CLR['reset']}")
    print(f"  {CLR['cyan']}./tester.py /path/libft{CLR['reset']}                - Exécuter tous les tests")
    print(f"  {CLR['cyan']}./tester.py /path/libft --list{CLR['reset']}         - Lister tous les tests disponibles")
    print(f"  {CLR['cyan']}./tester.py /path/libft --run PATTERN{CLR['reset']}  - Exécuter les tests contenant PATTERN")
    print(f"  {CLR['cyan']}./tester.py /path/libft --verbose{CLR['reset']}      - Mode verbose (plus de détails)")
    print(f"  {CLR['cyan']}./tester.py /path/libft --no-color{CLR['reset']}     - Désactiver les couleurs")
    print(f"  {CLR['cyan']}./tester.py /path/libft --timeout N{CLR['reset']}    - Timeout de N secondes (défaut: 10s)")
    print(f"")
    print(f"{CLR['dim']}Exemples :{CLR['reset']}")
    print(f"  {CLR['yellow']}./tester.py ./libft --run strlen{CLR['reset']}       - Tester seulement strlen")
    print(f"  {CLR['yellow']}./tester.py ./libft --run memcpy{CLR['reset']}       - Tester seulement memcpy")
    print(f"  {CLR['yellow']}./tester.py ./libft --run list{CLR['reset']}         - Tester les fonctions bonus")
    print(f"  {CLR['yellow']}./tester.py ./libft --timeout 5{CLR['reset']}        - Timeout de 5 secondes par test")
    print()

    # Informations GitHub
    print(f"{CLR['dim']}─────────────────────────────────────────────────────────────────────────────────{CLR['reset']}")
    print(f"{CLR['dim']}Développé par{CLR['reset']} {CLR['bold']}Blaeste{CLR['reset']}")
    print(f"{CLR['dim']}GitHub:{CLR['reset']} {CLR['cyan']}https://github.com/Blaeste{CLR['reset']}")
    print(f"{CLR['dim']}Projet:{CLR['reset']} {CLR['cyan']}https://github.com/Blaeste/libfterator{CLR['reset']}")
    print()

# ===============================================================
# ⚙️ Args
# ===============================================================
VERBOSE = "--verbose" in sys.argv
RUN_FILTER = None
LIST_ONLY = False
SAFE_MODE = False
TIMEOUT = 5  # Timeout par défaut en secondes (augmenté pour éviter les problèmes de timing)

argv = []
i = 1
while i < len(sys.argv):
    a = sys.argv[i]
    if a == "--verbose":
        VERBOSE = True
    elif a == "--list":
        LIST_ONLY = True
    elif a == "--run" and i + 1 < len(sys.argv):
        RUN_FILTER = sys.argv[i + 1]
        i += 1
    elif a == "--safe":
        SAFE_MODE = True
    elif a == "--timeout" and i + 1 < len(sys.argv):
        try:
            TIMEOUT = int(sys.argv[i + 1])
            if TIMEOUT <= 0:
                print("Erreur: Le timeout doit être un nombre positif")
                sys.exit(1)
        except ValueError:
            print("Erreur: Le timeout doit être un nombre entier")
            sys.exit(1)
        i += 1
    else:
        argv.append(a)
    i += 1

if len(argv) < 1:
    print("Usage: ./tester.py /chemin/vers/libft [--verbose] [--list] [--run PATTERN] [--no-color] [--safe] [--timeout SECONDS]")
    sys.exit(1)

libft = Path(argv[0]).resolve()

# ===============================================================
# 🧹 Norminette — config
# ===============================================================
# Laisse None pour auto-détection (privilégie ./normiette s'il existe).
NORM_CMD = "./normiette"   # ex: "./normiette" ou "./norminette"
NORM_FLAGS = "-R CheckForbiddenSourceHeader"   # ex: '-R CheckForbiddenSourceHeader'


# ===============================================================
# 🧰 Utils
# ===============================================================
def sh(cmd, silent=not VERBOSE):
    try:
        if silent:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n{CLR['red']}[ERREUR] Commande échouée:{CLR['reset']} {' '.join(cmd)}")
        if e.stdout:
            print(e.stdout.decode(errors="ignore"))
        raise

def ensure_path(p: Path, kind: str):
    if not p.exists():
        print(f"{CLR['red']}Erreur:{CLR['reset']} {kind} introuvable: {p}")
        sys.exit(2)

def check_makefile_rules():
    """Vérifie les règles du Makefile et affiche un rapport formaté."""
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}|{' '*30}COMPILING LIBFT{' '*35}|{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")

    rules = ["all", "$(NAME)", "fclean", "re", "clean", "bonus", "libft.a"]
    statuses = []

    for rule in rules:
        if rule == "$(NAME)":
            # $(NAME) est généralement un alias pour libft.a
            rule_to_test = "libft.a"
        elif rule == "libft.a":
            # Vérifier si libft.a existe déjà ou peut être créé
            rule_to_test = rule
        else:
            rule_to_test = rule

        try:
            if rule_to_test in ["libft.a", "all"]:
                # Tester la compilation
                result = subprocess.run(
                    ["make", "-C", str(libft), rule_to_test],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la compilation
                )
                if result.returncode == 0 and (libft / "libft.a").exists():
                    statuses.append("ok")
                else:
                    statuses.append("error")
            elif rule_to_test == "clean":
                # Créer un fichier temporaire .o pour tester clean
                subprocess.run(["make", "-C", str(libft), "all"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                result = subprocess.run(
                    ["make", "-C", str(libft), "clean"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT
                )
                statuses.append("ok" if result.returncode == 0 else "error")
            elif rule_to_test == "fclean":
                result = subprocess.run(
                    ["make", "-C", str(libft), "fclean"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT
                )
                statuses.append("ok" if result.returncode == 0 else "error")
            elif rule_to_test == "re":
                result = subprocess.run(
                    ["make", "-C", str(libft), "re"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la recompilation
                )
                if result.returncode == 0 and (libft / "libft.a").exists():
                    statuses.append("ok")
                else:
                    statuses.append("error")
            elif rule_to_test == "bonus":
                result = subprocess.run(
                    ["make", "-C", str(libft), "bonus"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=TIMEOUT * 3  # Plus de temps pour la compilation bonus
                )
                if result.returncode == 0:
                    statuses.append("ok")
                else:
                    statuses.append("missing")
            else:
                statuses.append("unknown")

        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            statuses.append("error")

    # Affichage du rapport
    print("rules:")

    # Ligne des noms de règles
    rule_line = ""
    for rule in rules:
        if len(rule) <= 10:
            rule_line += f"{rule:<10} "
        else:
            rule_line += f"{rule:<15} "
    print(rule_line.rstrip())

    # Ligne des statuts avec couleurs
    status_line = ""
    for i, status in enumerate(statuses):
        rule = rules[i]
        if status == "ok":
            colored_status = f"{CLR['green']}ok{CLR['reset']}"
        elif status == "missing":
            colored_status = f"{CLR['yellow']}missing{CLR['reset']}"
        elif status == "found":
            colored_status = f"{CLR['cyan']}found{CLR['reset']}"
        else:
            colored_status = f"{CLR['red']}error{CLR['reset']}"

        if len(rule) <= 10:
            status_line += f"{colored_status:<19} "  # 19 pour compenser les codes couleur
        else:
            status_line += f"{colored_status:<24} "

    print(status_line.rstrip())
    print()

def build_libft():
    print(f"{CLR['cyan']}→ Build libft…{CLR['reset']}", end="", flush=True)
    # Compiler d'abord la partie obligatoire
    subprocess.run(["make", "-C", str(libft), "re"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    ensure_path(libft / "libft.a", "libft.a")

    # Essayer de compiler les bonus aussi (si ils existent)
    try:
        subprocess.run(["make", "-C", str(libft), "bonus"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        # Les bonus ne sont peut-être pas disponibles, ce n'est pas grave
        pass

    print(f" {CLR['green']}OK{CLR['reset']}")

# ===============================================================
# 🎯 Détection des sections du sujet
# ===============================================================
def get_section_info(test_name, previous_test_name=None):
    """Détermine si un test marque le début d'une nouvelle section."""

    # Mapping des fonctions vers les sections
    part1_functions = [
        'charclass', 'strlen', 'memset', 'bzero', 'memcpy', 'memmove',
        'strlcpy', 'strlcat', 'caseconv', 'strchr', 'strrchr', 'strncmp',
        'strnstr', 'memchr', 'memcmp', 'atoi', 'calloc', 'strdup'
    ]

    part2_functions = [
        'substr', 'strjoin', 'strtrim', 'itoa', 'split', 'strmapi',
        'striteri', 'putfd'
    ]

    bonus_functions = ['list']

    valgrind_functions = ['valgrind']

    overprotection_functions = ['overprotection']

    def get_function_from_test(name):
        return name.split('/')[0]

    current_func = get_function_from_test(test_name)

    # Déterminer la section actuelle
    if current_func in part1_functions:
        section = "PARTIE 1"
        desc = "Fonctions de la libc"
    elif current_func in part2_functions:
        section = "PARTIE 2"
        desc = "Fonctions supplémentaires"
    elif current_func in bonus_functions:
        section = "BONUS"
        desc = "Listes chaînées"
    elif current_func in valgrind_functions:
        section = "VALGRIND"
        desc = "Tests de fuites mémoire"
    elif current_func in overprotection_functions:
        section = "VALIDATION"
        desc = "Tests de sur-protection"
    else:
        return None, None, None

    # Vérifier si c'est un changement de section
    if previous_test_name:
        prev_func = get_function_from_test(previous_test_name)
        # Changements de section dans l'ordre logique
        if (prev_func in part1_functions and current_func in part2_functions) or \
           (prev_func in part2_functions and current_func in bonus_functions) or \
           (prev_func in bonus_functions and current_func in valgrind_functions) or \
           (prev_func in valgrind_functions and current_func in overprotection_functions) or \
           (prev_func in part2_functions and current_func in valgrind_functions) or \
           (prev_func in part2_functions and current_func in overprotection_functions):
            return section, desc, True
        # Retour vers PARTIE 1 seulement si on n'est pas déjà dans une section ultérieure
        elif (prev_func not in part1_functions and prev_func not in part2_functions and
              prev_func not in bonus_functions and prev_func not in valgrind_functions and prev_func not in overprotection_functions and
              current_func in part1_functions):
            return "PARTIE 1", "Fonctions de la libc", True
    else:
        # Premier test
        return section, desc, True

    return section, desc, False

def print_section_header(section, description):
    """Affiche un en-tête de section."""
    print()
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}🔹 {section} — {description}{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print()

def print_subsection_header(subsection, description):
    """Affiche un en-tête de sous-section."""
    print()
    print(f"{CLR['dim']}{'─'*60}{CLR['reset']}")
    print(f"{CLR['cyan']}📂 {subsection} — {description}{CLR['reset']}")
    print(f"{CLR['dim']}{'─'*60}{CLR['reset']}")
    print()

def get_subsection_info(test_name, previous_test_name):
    """Détermine si on doit afficher une nouvelle sous-section."""
    subsection_descriptions = {
        # PARTIE 1
        'charclass': 'Tests de classification de caractères',
        'caseconv': 'Conversion de casse',
        'strlen': 'Longueur de chaîne',
        'memset': 'Remplissage mémoire',
        'bzero': 'Mise à zéro mémoire',
        'memcpy': 'Copie mémoire',
        'memmove': 'Copie mémoire avec chevauchement',
        'strlcpy': 'Copie sécurisée de chaîne',
        'strlcat': 'Concaténation sécurisée',
        'strchr': 'Recherche de caractère',
        'strrchr': 'Recherche inverse de caractère',
        'strncmp': 'Comparaison de chaînes',
        'memchr': 'Recherche en mémoire',
        'memcmp': 'Comparaison mémoire',
        'strnstr': 'Recherche de sous-chaîne',
        'atoi': 'Conversion ASCII vers entier',
        'calloc': 'Allocation mémoire initialisée',
        'strdup': 'Duplication de chaîne',

        # PARTIE 2
        'substr': 'Extraction de sous-chaîne',
        'strjoin': 'Jointure de chaînes',
        'strtrim': 'Suppression d\'espaces',
        'split': 'Division de chaîne',
        'itoa': 'Conversion entier vers ASCII',
        'strmapi': 'Application de fonction avec index',
        'striteri': 'Itération avec modification',
        'putfd': 'Écriture sur descripteur de fichier',

        # BONUS
        'list': 'Manipulation de listes chaînées',

        # VALGRIND
        'valgrind': 'Tests de fuites mémoire',

        # VALIDATION
        'overprotection': 'Tests de sur-protection'
    }

    current_subsection = test_name.split('/')[0]

    if previous_test_name:
        previous_subsection = previous_test_name.split('/')[0]
        if current_subsection != previous_subsection:
            description = subsection_descriptions.get(current_subsection, current_subsection)
            return current_subsection, description, True
    else:
        # Premier test
        description = subsection_descriptions.get(current_subsection, current_subsection)
        return current_subsection, description, True

    return current_subsection, None, False

# ===============================================================
# 🧱 Compilation et exécution
# ===============================================================
def compile_harness(root: Path, name: str, source: str, logger=None) -> Path:
    src = root / "build" / f"{name}.c"
    exe = root / "build" / name

    # préambule minimal: stdio pour fprintf et libft.h si absent
    prelude = '#include <stdio.h>\n'
    if '#include "libft.h"' not in source:
        prelude += '#include "libft.h"\n'
    source = prelude + source

    src.write_text(source)

    # Discover include directories: prefer standard locations and any folder containing libft.h
    include_dirs = [str(libft)]  # Always include the libft root directory first

    # Check for common include directory names
    common_inc_names = ["inc", "include", "includes", "headers"]
    for inc_name in common_inc_names:
        p = libft / inc_name
        if p.is_dir():
            include_dirs.append(str(p))

    # Also scan all subdirectories for libft.h and add their parent dir
    try:
        for header_file in libft.rglob("libft.h"):
            parent = header_file.parent
            parent_str = str(parent)
            if parent_str not in include_dirs:
                include_dirs.append(parent_str)
    except Exception:
        pass

    inc_flags = [f"-I{p}" for p in include_dirs]
    lib = "-L" + str(libft)
    cmd = [os.environ.get("CC", "cc"), "-Wall", "-Wextra", "-Werror"] + inc_flags + [str(src), lib, "-lft", "-o", str(exe)]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            if logger:
                log_compilation_result(logger, True)
        else:
            if logger:
                log_compilation_result(logger, False, result.stdout, result.stderr)
            sh(cmd)  # Original behavior for errors
    except Exception as e:
        if logger:
            log_compilation_result(logger, False, error=str(e))
        sh(cmd)  # Fallback to original behavior

    return exe

# ===============================================================
# 🧩 Chargement des fichiers de tests
# ===============================================================
def load_tests(tests_dir: Path):
    # Ordre logique selon le sujet de la libft
    test_order = [
        # PARTIE 1 - Fonctions de la libc
        't_charclass.py',    # isalpha, isdigit, isalnum, isascii, isprint
        't_caseconv.py',     # toupper, tolower
        't_strlen.py',       # strlen
        't_memset.py',       # memset
        't_bzero.py',        # bzero
        't_memcpy.py',       # memcpy
        't_memmove.py',      # memmove
        't_strlcpy.py',      # strlcpy
        't_strlcat.py',      # strlcat
        't_strchr.py',       # strchr
        't_strrchr.py',      # strrchr
        't_strncmp.py',      # strncmp
        't_memchr.py',       # memchr
        't_memcmp.py',       # memcmp
        't_strnstr.py',      # strnstr
        't_atoi.py',         # atoi
        't_calloc.py',       # calloc
        't_strdup.py',       # strdup

        # PARTIE 2 - Fonctions supplémentaires
        't_substr.py',       # ft_substr
        't_strjoin.py',      # ft_strjoin
        't_strtrim.py',      # ft_strtrim
        't_split.py',        # ft_split
        't_itoa.py',         # ft_itoa
        't_strmapi.py',      # ft_strmapi
        't_striteri.py',     # ft_striteri
        't_putfd.py',        # ft_putchar_fd, ft_putstr_fd, ft_putendl_fd, ft_putnbr_fd

        # BONUS - Listes chaînées
        't_list.py',         # ft_lstnew, ft_lstadd_front, ft_lstsize, etc.

        # VALGRIND - Tests de fuites mémoire
        't_valgrind.py',     # Tests avec valgrind pour détecter les memory leaks

        # VALIDATION - Tests de sur-protection (à la fin)
        't_overprotection.py'
    ]

    all_tests = []

    # Charger les tests dans l'ordre défini
    for filename in test_order:
        file_path = tests_dir / filename
        if file_path.exists():
            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "TESTS"):
                all_tests.extend(mod.TESTS)

    # Charger les fichiers manquants (au cas où)
    loaded_files = set(test_order)
    for file in sorted(tests_dir.glob("t_*.py")):
        if file.name not in loaded_files:
            spec = importlib.util.spec_from_file_location(file.stem, file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "TESTS"):
                all_tests.extend(mod.TESTS)

    return all_tests

# ===============================================================
# 🚴‍♂️ Exécution d'un binaire de test
# ===============================================================
def run_exec(exe: Path, test_name=""):
    t0 = time.time()

    # Utiliser le timeout configuré globalement, avec des valeurs spéciales pour certains tests
    default_timeout = TIMEOUT
    valgrind_timeout = TIMEOUT * 3  # Plus long timeout pour valgrind
    crash_timeout = min(2, TIMEOUT)  # Timeout court pour les tests de crash (max 2s)

    # Pour les tests valgrind, lancer avec valgrind pour détecter les fuites mémoire
    if "valgrind" in test_name:
        # Vérifier si valgrind est disponible
        try:
            subprocess.run(["valgrind", "--version"], capture_output=True, check=True)
            valgrind_available = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            valgrind_available = False

        if valgrind_available:
            # Lancer avec valgrind
            valgrind_cmd = [
                "valgrind",
                "--tool=memcheck",
                "--leak-check=full",
                "--show-leak-kinds=all",
                "--track-origins=yes",
                "--error-exitcode=42",  # Code de sortie spécial en cas de fuite
                "--quiet",  # Réduire le bruit
                str(exe)
            ]
            try:
                res = subprocess.run(valgrind_cmd, timeout=valgrind_timeout)
                ms = int((time.time() - t0) * 1000)
                # Code 42 = fuite détectée, Code 0 = pas de fuite
                return res.returncode, ms
            except subprocess.TimeoutExpired:
                ms = int((time.time() - t0) * 1000)
                return -999, ms  # Code spécial pour timeout
        else:
            # Valgrind non disponible, exécuter normalement avec timeout
            try:
                res = subprocess.run([str(exe)], timeout=default_timeout)
                ms = int((time.time() - t0) * 1000)
                return res.returncode, ms
            except subprocess.TimeoutExpired:
                ms = int((time.time() - t0) * 1000)
                return -999, ms  # Code spécial pour timeout

    # Pour les tests d'overprotection, on s'attend à un crash (SIGSEGV)
    elif "overprotection" in test_name and "should_crash" in test_name:
        # Timeout plus court pour les tests de crash
        try:
            res = subprocess.run([str(exe)], timeout=crash_timeout)
            ms = int((time.time() - t0) * 1000)
            return res.returncode, ms
        except subprocess.TimeoutExpired:
            # Si le test timeout, c'est probablement parce qu'il attend un signal
            ms = int((time.time() - t0) * 1000)
            return 1, ms  # FAIL - le test n'a pas crashé comme attendu
    else:
        # Tests normaux avec timeout de protection
        try:
            res = subprocess.run([str(exe)], timeout=default_timeout)
            ms = int((time.time() - t0) * 1000)
            return res.returncode, ms
        except subprocess.TimeoutExpired:
            ms = int((time.time() - t0) * 1000)
            return -999, ms  # Code spécial pour timeout

# ===============================================================
# 🧹 Norminette — détection + exécution
# ===============================================================
def _detect_norm_cmd():
    # Ordre de préférence : ./normiette, ./norminette, binaire système
    candidates = []
    if NORM_CMD:
        candidates.append(NORM_CMD)
    candidates += ["./normiette", "./norminette", "./norminette.py",
                   "norminette", "python3 -m norminette", "pipx run norminette"]
    for cand in candidates:
        if " " in cand:
            prog = cand.split()[0]
        else:
            prog = cand
        if "/" in prog:
            p = Path(prog)
            if p.exists() and os.access(p, os.X_OK):
                return cand.split(), cand
        else:
            found = shutil.which(prog)
            if found:
                return cand.split(), cand
    return None, None

def run_norminette(log_path: Path, logger=None):
    cmd_list, printable = _detect_norm_cmd()
    start = time.time()
    if not cmd_list:
        # Pas trouvé → on marque SKIP mais on n'arrête rien
        result = {"status":"SKIP","ms":int((time.time()-start)*1000),"detail":"norminette introuvable"}
        if logger:
            logger.warning("⚠️ NORMINETTE: SKIP - norminette introuvable")
        return result

    args = cmd_list[:]
    if NORM_FLAGS:
        args.extend(NORM_FLAGS.split())

    # Au lieu d'analyser tout le dossier, analyser seulement les fichiers .c et .h
    # pour éviter les fichiers de test comme tester.py
    c_files = list(libft.glob("*.c"))
    h_files = list(libft.glob("*.h"))

    # Aussi chercher dans les sous-dossiers standards (src/, include/, etc.)
    for subdir in ["src", "srcs", "sources", "include", "includes", "inc", "headers"]:
        subdir_path = libft / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            c_files.extend(subdir_path.glob("*.c"))
            h_files.extend(subdir_path.glob("*.h"))

    all_files = c_files + h_files

    if not all_files:
        # Aucun fichier .c/.h trouvé, fallback vers le dossier complet
        # mais avec exclusions explicites pour les dossiers de test
        args.append(str(libft))

        # Ajouter des exclusions explicites si la norminette les supporte
        test_dirs_to_exclude = ["libfterator", "tests", "test", ".git", "__pycache__", "out"]
        test_files_to_exclude = ["tester.py", "*.py", "*.pyc"]

        # Essayer d'ajouter --exclude pour chaque pattern (certaines versions de norminette le supportent)
        for exclude in test_dirs_to_exclude + test_files_to_exclude:
            exclude_path = libft / exclude.rstrip('*')
            if exclude_path.exists() or exclude in ["*.py", "*.pyc", "tester.py"]:
                # Ajouter l'exclusion (silencieusement - certaines norminettes ne supportent pas --exclude)
                try:
                    if '--exclude' not in args:  # Éviter les doublons
                        args.extend(['--exclude', exclude])
                except:
                    pass  # Ignorer si --exclude n'est pas supporté
    else:
        # Ajouter tous les fichiers .c et .h trouvés
        for file in all_files:
            args.append(str(file))

    try:
        proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, text=True)
        out = proc.stdout or ""
        error = ""
    except Exception as e:
        out = f"Erreur de lancement: {e}\n"
        error = str(e)
        proc = type("X", (), {"returncode":1})()

    # Écrit le log complet
    log_path.write_text(out)

    # Heuristique simple pour l'état
    text = (out or "").lower()
    failed = ("error" in text) or ("ko" in text) or (proc.returncode != 0)
    status = "FAIL" if failed else "PASS"
    ms = int((time.time()-start)*1000)

    # Log des résultats de la norminette
    if logger:
        log_norminette_result(logger, proc.returncode, out, error)

    return {"status": status, "ms": ms, "detail": out}


# ===============================================================
# 🚀 Main
# ===============================================================
def main():
    print_header()

    root = Path(__file__).resolve().parent
    tests_dir = root / "tests"
    ensure_path(libft / "Makefile", "Makefile libft")

    (root / "build").mkdir(exist_ok=True)
    (root / "out").mkdir(exist_ok=True)

    # Configuration du logging dans le dossier out/
    log_file, logger = setup_logging(root / "out")

    # --- Norminette obligatoire, non bloquante ---
    norm_log = (root / "out" / "norminette.txt")

    # Affichage formaté de la Norminette
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")
    print(f"{CLR['cyan']}|{' '*29}NORMINETTE CHECK{' '*36}|{CLR['reset']}")
    print(f"{CLR['cyan']}{'='*82}{CLR['reset']}")

    left = " [norm] check "
    dots = "." * max(1, 75 - len(left) - 10)
    print(f"{CLR['dim']}{left}{dots}{CLR['reset']}", end="", flush=True)

    norm = run_norminette(norm_log, logger)
    print(f" {icon(norm['status'])} {color_status(norm['status'])} " +
          f"{CLR['gray']}({human_ms(norm['ms'])}){CLR['reset']}")
    print()


    tests = load_tests(tests_dir)
    if not tests:
        print("Aucun test trouvé dans tests/")
        return

    # Filtre optionnel
    if RUN_FILTER:
        tests = [t for t in tests if RUN_FILTER in t[0]]
        if not tests:
            print(f"Aucun test ne correspond au filtre: {RUN_FILTER}")
            return

    if LIST_ONLY:
        for name, _ in tests:
            print(name)
        return

    check_makefile_rules()
    build_libft()

    # -----------------------------------------------------------
    # RUN + affichage joli
    # -----------------------------------------------------------
    total = len(tests)
    rows = []
    print()
    print(f"{CLR['bold']}Running {total} test(s){CLR['reset']} {CLR['dim']}(timeout: {TIMEOUT}s){CLR['reset']}")

    previous_test_name = None
    for idx, (name, src) in enumerate(tests, 1):
        # Vérifier si on doit afficher un nouveau header de section
        section, desc, is_new_section = get_section_info(name, previous_test_name)
        if is_new_section and section:
            print_section_header(section, desc)

        # Vérifier si on doit afficher un nouveau header de sous-section
        subsection, subsec_desc, is_new_subsection = get_subsection_info(name, previous_test_name)
        if is_new_subsection and subsection and subsec_desc:
            print_subsection_header(subsection, subsec_desc)

        safe = name.replace('/', '_')
        left = f" [{idx:>2}/{total}] {name} "
        dots = "." * max(1, 77 - len(left) - 10)
        print(f"{CLR['dim']}{left}{dots}{CLR['reset']}", end="", flush=True)

        exe = compile_harness(root, safe, src, logger)
        code, ms = run_exec(exe, name)

        # Vérifier d'abord si c'est un timeout
        if code == -999:
            status = "TIMEOUT"
        # Logique spéciale pour les tests valgrind
        elif "valgrind" in name:
            # Code 0 = pas de fuite (PASS), Code 42 = fuite détectée (FAIL), autres = erreur d'exécution
            if code == 0:
                status = "PASS"
            elif code == 42:
                status = "LEAK"  # Fuite mémoire détectée
            else:
                status = "FAIL"  # Erreur d'exécution
        # Logique spéciale pour les tests d'overprotection
        elif "overprotection" in name and "should_crash" in name:
            # Pour ces tests, on s'attend à un code de retour 0 (PASS = a crashé comme attendu)
            # Code 1 = FAIL (sur-protégé, n'a pas crashé)
            status = "PASS" if code == 0 else "FAIL"
        else:
            status = "PASS" if code == 0 else ("CRASH" if code not in (0, 1) else "FAIL")

        # Log du résultat du test
        error_output = None
        if status != "PASS":
            # Capturer l'erreur si le test a échoué
            if exe.exists():
                try:
                    error_result = subprocess.run([str(exe)], capture_output=True, text=True, timeout=TIMEOUT)
                    if error_result.stdout or error_result.stderr:
                        error_output = f"stdout: {error_result.stdout}\nstderr: {error_result.stderr}"
                except:
                    pass

        log_test_result(logger, name, status, ms, error_output)

        print(f" {icon(status)} {color_status(status)} {CLR['gray']}({human_ms(ms)}){CLR['reset']}")
        rows.append((name, status, ms))

        previous_test_name = name

    # -----------------------------------------------------------
    # Résumé final
    # -----------------------------------------------------------
    ok = sum(1 for _, s, _ in rows if s == "PASS")
    fails = [(n, s, m) for n, s, m in rows if s != "PASS"]

    print()
    print(f"{CLR['bold']}Résumé{CLR['reset']} — {CLR['green']}{ok}{CLR['reset']}/{total} PASS")
    if fails:
        print(f"{CLR['red']}Échecs / Crashs:{CLR['reset']}")
        for n, s, m in fails:
            print(f"  - {n:<25} {color_status(s)} {CLR['gray']}({human_ms(m)}){CLR['reset']}")
    else:
        print(f"{CLR['green']}Tous les tests passent.{CLR['reset']}")

    # Log du résumé final
    logger.info("="*50)
    logger.info(f"RÉSUMÉ FINAL: {ok}/{total} tests réussis")
    if fails:
        logger.error("TESTS ÉCHOUÉS:")
        for n, s, m in fails:
            logger.error(f"  - {n}: {s} ({m} ms)")
    logger.info("="*50)

    # Information sur le fichier de log
    print()
    print(f"{CLR['cyan']}📝 Log détaillé sauvegardé dans:{CLR['reset']} {log_file}")
    print(f"{CLR['dim']}   Contient tous les résultats, erreurs et sorties complètes{CLR['reset']}")

# ===============================================================
# 🧠 Entry point
# ===============================================================
if __name__ == "__main__":
    main()
