"""Tests pour ft_strchr"""

TESTS = [
    ("strchr/basic", '''
#include <string.h>
int main() {
    char str[] = "Hello World";
    char *result1, *result2;

    result1 = strchr(str, 'W');
    result2 = ft_strchr(str, 'W');

    if (result1 != result2) return 1;
    if (result2 != &str[6]) return 1;

    return 0;
}'''),

    ("strchr/first_char", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strchr(str, 'H');
    result2 = ft_strchr(str, 'H');

    if (result1 != result2) return 1;
    if (result2 != &str[0]) return 1;

    return 0;
}'''),

    ("strchr/last_char", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strchr(str, 'o');
    result2 = ft_strchr(str, 'o');

    if (result1 != result2) return 1;
    if (result2 != &str[4]) return 1;

    return 0;
}'''),

    ("strchr/null_terminator", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strchr(str, '\\0');
    result2 = ft_strchr(str, '\\0');

    if (result1 != result2) return 1;
    if (result2 != &str[5]) return 1;

    return 0;
}'''),

    ("strchr/not_found", '''
#include <string.h>
int main() {
    char str[] = "Hello World";
    char *result1, *result2;

    result1 = strchr(str, 'X');
    result2 = ft_strchr(str, 'X');

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    return 0;
}'''),

    ("strchr/empty_string", '''
#include <string.h>
int main() {
    char str[] = "";
    char *result1, *result2;

    // Chercher un caractère dans une chaîne vide
    result1 = strchr(str, 'a');
    result2 = ft_strchr(str, 'a');

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    // Chercher le null terminator dans une chaîne vide
    result1 = strchr(str, '\\0');
    result2 = ft_strchr(str, '\\0');

    if (result1 != result2) return 1;
    if (result2 != str) return 1;

    return 0;
}'''),

    ("strchr/multiple_occurrences", '''
#include <string.h>
int main() {
    char str[] = "Hello Hello";
    char *result1, *result2;

    // Doit retourner la première occurrence
    result1 = strchr(str, 'l');
    result2 = ft_strchr(str, 'l');

    if (result1 != result2) return 1;
    if (result2 != &str[2]) return 1; // Première 'l'

    return 0;
}'''),

    ("strchr/special_chars", '''
#include <string.h>
int main() {
    char str[] = "Hello\\tWorld\\n!";
    char *result1, *result2;

    result1 = strchr(str, '\\t');
    result2 = ft_strchr(str, '\\t');

    if (result1 != result2) return 1;

    result1 = strchr(str, '\\n');
    result2 = ft_strchr(str, '\\n');

    if (result1 != result2) return 1;

    return 0;
}'''),
]
