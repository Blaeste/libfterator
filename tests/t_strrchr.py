"""Tests pour ft_strrchr"""

TESTS = [
    ("strrchr/basic", '''
#include <string.h>
int main() {
    char str[] = "Hello World";
    char *result1, *result2;

    result1 = strrchr(str, 'o');
    result2 = ft_strrchr(str, 'o');

    if (result1 != result2) return 1;
    if (result2 != &str[7]) return 1; // Dernière 'o'

    return 0;
}'''),

    ("strrchr/first_char", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strrchr(str, 'H');
    result2 = ft_strrchr(str, 'H');

    if (result1 != result2) return 1;
    if (result2 != &str[0]) return 1;

    return 0;
}'''),

    ("strrchr/last_char", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strrchr(str, 'o');
    result2 = ft_strrchr(str, 'o');

    if (result1 != result2) return 1;
    if (result2 != &str[4]) return 1;

    return 0;
}'''),

    ("strrchr/null_terminator", '''
#include <string.h>
int main() {
    char str[] = "Hello";
    char *result1, *result2;

    result1 = strrchr(str, '\\0');
    result2 = ft_strrchr(str, '\\0');

    if (result1 != result2) return 1;
    if (result2 != &str[5]) return 1;

    return 0;
}'''),

    ("strrchr/not_found", '''
#include <string.h>
int main() {
    char str[] = "Hello World";
    char *result1, *result2;

    result1 = strrchr(str, 'X');
    result2 = ft_strrchr(str, 'X');

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    return 0;
}'''),

    ("strrchr/empty_string", '''
#include <string.h>
int main() {
    char str[] = "";
    char *result1, *result2;

    // Chercher un caractère dans une chaîne vide
    result1 = strrchr(str, 'a');
    result2 = ft_strrchr(str, 'a');

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    // Chercher le null terminator dans une chaîne vide
    result1 = strrchr(str, '\\0');
    result2 = ft_strrchr(str, '\\0');

    if (result1 != result2) return 1;
    if (result2 != str) return 1;

    return 0;
}'''),

    ("strrchr/multiple_occurrences", '''
#include <string.h>
int main() {
    char str[] = "Hello Hello Hello";
    char *result1, *result2;

    // Doit retourner la dernière occurrence
    result1 = strrchr(str, 'l');
    result2 = ft_strrchr(str, 'l');

    if (result1 != result2) return 1;
    if (result2 != &str[15]) return 1; // Dernière 'l'

    return 0;
}'''),

    ("strrchr/same_as_strchr", '''
#include <string.h>
int main() {
    char str[] = "Hello World";
    char *result1, *result2;
    char *strchr_result1, *strchr_result2;

    // Pour un caractère unique, strrchr et strchr doivent donner le même résultat
    result1 = strrchr(str, 'W');
    result2 = ft_strrchr(str, 'W');
    strchr_result1 = strchr(str, 'W');
    strchr_result2 = ft_strchr(str, 'W');

    if (result1 != result2) return 1;
    if (result1 != strchr_result1) return 1;
    if (result2 != strchr_result2) return 1;

    return 0;
}'''),

    ("strrchr/repeated_char", '''
#include <string.h>
int main() {
    char str[] = "aaaaaaa";
    char *result1, *result2;

    result1 = strrchr(str, 'a');
    result2 = ft_strrchr(str, 'a');

    if (result1 != result2) return 1;
    if (result2 != &str[6]) return 1; // Dernière 'a'

    return 0;
}'''),
]
