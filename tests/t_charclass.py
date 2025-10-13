"""Tests pour les fonctions de classification de caractères (isalpha, isdigit, isalnum, isascii, isprint)"""

TESTS = [
    ("charclass/isalpha_basic", '''
int main() {
    // Tests basiques
    if (ft_isalpha('a') == 0) return 1;
    if (ft_isalpha('Z') == 0) return 1;
    if (ft_isalpha('m') == 0) return 1;
    if (ft_isalpha('1') != 0) return 1;
    if (ft_isalpha(' ') != 0) return 1;
    if (ft_isalpha('\\n') != 0) return 1;
    return 0;
}'''),

    ("charclass/isalpha_edge", '''
int main() {
    // Tests limites
    if (ft_isalpha('@') != 0) return 1; // avant 'A'
    if (ft_isalpha('[') != 0) return 1; // après 'Z'
    if (ft_isalpha('`') != 0) return 1; // avant 'a'
    if (ft_isalpha('{') != 0) return 1; // après 'z'
    if (ft_isalpha(0) != 0) return 1;
    if (ft_isalpha(127) != 0) return 1;
    return 0;
}'''),

    ("charclass/isdigit_basic", '''
int main() {
    // Tests basiques
    if (ft_isdigit('0') == 0) return 1;
    if (ft_isdigit('5') == 0) return 1;
    if (ft_isdigit('9') == 0) return 1;
    if (ft_isdigit('a') != 0) return 1;
    if (ft_isdigit(' ') != 0) return 1;
    if (ft_isdigit('/') != 0) return 1; // avant '0'
    if (ft_isdigit(':') != 0) return 1; // après '9'
    return 0;
}'''),

    ("charclass/isalnum_basic", '''
int main() {
    // Tests basiques
    if (ft_isalnum('a') == 0) return 1;
    if (ft_isalnum('Z') == 0) return 1;
    if (ft_isalnum('5') == 0) return 1;
    if (ft_isalnum(' ') != 0) return 1;
    if (ft_isalnum('!') != 0) return 1;
    if (ft_isalnum('@') != 0) return 1;
    return 0;
}'''),

    ("charclass/isascii_basic", '''
int main() {
    // Tests basiques
    if (ft_isascii(0) == 0) return 1;
    if (ft_isascii(127) == 0) return 1;
    if (ft_isascii('A') == 0) return 1;
    if (ft_isascii(128) != 0) return 1;
    if (ft_isascii(-1) != 0) return 1;
    if (ft_isascii(200) != 0) return 1;
    return 0;
}'''),

    ("charclass/isprint_basic", '''
int main() {
    // Tests basiques
    if (ft_isprint(' ') == 0) return 1; // 32, premier imprimable
    if (ft_isprint('~') == 0) return 1; // 126, dernier imprimable
    if (ft_isprint('A') == 0) return 1;
    if (ft_isprint(31) != 0) return 1; // avant espace
    if (ft_isprint(127) != 0) return 1; // DEL
    if (ft_isprint('\\n') != 0) return 1;
    if (ft_isprint('\\t') != 0) return 1;
    return 0;
}'''),

    ("charclass/comprehensive", '''
int main() {
    // Test complet sur plusieurs caractères
    char str[] = "Hello123!\\n\\t";
    int i = 0;

    // H - alpha, alnum, ascii, print
    if (!ft_isalpha(str[i]) || !ft_isalnum(str[i]) ||
        !ft_isascii(str[i]) || !ft_isprint(str[i])) return 1;
    i++;

    // 1 - digit, alnum, ascii, print
    if (ft_isalpha(str[5]) || !ft_isdigit(str[5]) ||
        !ft_isalnum(str[5]) || !ft_isascii(str[5]) || !ft_isprint(str[5])) return 1;

    // ! - ni alpha ni digit, mais ascii et print
    if (ft_isalpha(str[8]) || ft_isdigit(str[8]) || ft_isalnum(str[8]) ||
        !ft_isascii(str[8]) || !ft_isprint(str[8])) return 1;

    // \\n - ni print
    if (ft_isprint(str[9])) return 1;

    return 0;
}'''),
]
