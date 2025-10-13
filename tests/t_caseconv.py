"""Tests pour ft_toupper et ft_tolower"""

TESTS = [
    ("caseconv/toupper_basic", '''
#include <ctype.h>
int main() {
    if (ft_toupper('a') != toupper('a')) return 1;
    if (ft_toupper('z') != toupper('z')) return 1;
    if (ft_toupper('A') != toupper('A')) return 1;
    if (ft_toupper('Z') != toupper('Z')) return 1;

    if (ft_toupper('a') != 'A') return 1;
    if (ft_toupper('z') != 'Z') return 1;

    return 0;
}'''),

    ("caseconv/toupper_non_alpha", '''
#include <ctype.h>
int main() {
    if (ft_toupper('1') != toupper('1')) return 1;
    if (ft_toupper('!') != toupper('!')) return 1;
    if (ft_toupper(' ') != toupper(' ')) return 1;
    if (ft_toupper('\\n') != toupper('\\n')) return 1;
    if (ft_toupper('@') != toupper('@')) return 1;

    return 0;
}'''),

    ("caseconv/tolower_basic", '''
#include <ctype.h>
int main() {
    if (ft_tolower('A') != tolower('A')) return 1;
    if (ft_tolower('Z') != tolower('Z')) return 1;
    if (ft_tolower('a') != tolower('a')) return 1;
    if (ft_tolower('z') != tolower('z')) return 1;

    if (ft_tolower('A') != 'a') return 1;
    if (ft_tolower('Z') != 'z') return 1;

    return 0;
}'''),

    ("caseconv/tolower_non_alpha", '''
#include <ctype.h>
int main() {
    if (ft_tolower('1') != tolower('1')) return 1;
    if (ft_tolower('!') != tolower('!')) return 1;
    if (ft_tolower(' ') != tolower(' ')) return 1;
    if (ft_tolower('\\n') != tolower('\\n')) return 1;
    if (ft_tolower('[') != tolower('[')) return 1;

    return 0;
}'''),

    ("caseconv/edge_cases", '''
#include <ctype.h>
int main() {
    // Caractères juste avant/après les lettres
    if (ft_toupper('@') != toupper('@')) return 1; // avant 'A'
    if (ft_toupper('[') != toupper('[')) return 1; // après 'Z'
    if (ft_toupper('`') != toupper('`')) return 1; // avant 'a'
    if (ft_toupper('{') != toupper('{')) return 1; // après 'z'

    if (ft_tolower('@') != tolower('@')) return 1;
    if (ft_tolower('[') != tolower('[')) return 1;
    if (ft_tolower('`') != tolower('`')) return 1;
    if (ft_tolower('{') != tolower('{')) return 1;

    return 0;
}'''),

    ("caseconv/numbers_and_special", '''
#include <ctype.h>
int main() {
    char test_chars[] = "0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";

    for (int i = 0; test_chars[i]; i++) {
        if (ft_toupper(test_chars[i]) != toupper(test_chars[i])) return 1;
        if (ft_tolower(test_chars[i]) != tolower(test_chars[i])) return 1;
    }

    return 0;
}'''),

    ("caseconv/all_letters", '''
#include <ctype.h>
int main() {
    // Test toutes les lettres minuscules
    for (char c = 'a'; c <= 'z'; c++) {
        if (ft_toupper(c) != toupper(c)) return 1;
        if (ft_tolower(c) != tolower(c)) return 1;
    }

    // Test toutes les lettres majuscules
    for (char c = 'A'; c <= 'Z'; c++) {
        if (ft_toupper(c) != toupper(c)) return 1;
        if (ft_tolower(c) != tolower(c)) return 1;
    }

    return 0;
}'''),

    ("caseconv/extended_ascii", '''
#include <ctype.h>
int main() {
    // Test des valeurs en dehors de la plage standard
    if (ft_toupper(0) != toupper(0)) return 1;
    if (ft_toupper(127) != toupper(127)) return 1;
    if (ft_tolower(0) != tolower(0)) return 1;
    if (ft_tolower(127) != tolower(127)) return 1;

    return 0;
}'''),
]
