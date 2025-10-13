"""Tests pour ft_strncmp"""

TESTS = [
    ("strncmp/basic_equal", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "Hello";

    int result1 = strncmp(s1, s2, 5);
    int result2 = ft_strncmp(s1, s2, 5);

    if ((result1 == 0) != (result2 == 0)) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("strncmp/basic_different", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "World";

    int result1 = strncmp(s1, s2, 5);
    int result2 = ft_strncmp(s1, s2, 5);

    // Les deux doivent avoir le même signe
    if ((result1 > 0) != (result2 > 0)) return 1;
    if ((result1 < 0) != (result2 < 0)) return 1;

    return 0;
}'''),

    ("strncmp/partial_compare", '''
#include <string.h>
int main() {
    char s1[] = "Hello World";
    char s2[] = "Hello Universe";

    int result1 = strncmp(s1, s2, 5);
    int result2 = ft_strncmp(s1, s2, 5);

    if ((result1 == 0) != (result2 == 0)) return 1;
    if (result2 != 0) return 1; // Les 5 premiers caractères sont identiques

    return 0;
}'''),

    ("strncmp/zero_length", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "World";

    int result1 = strncmp(s1, s2, 0);
    int result2 = ft_strncmp(s1, s2, 0);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1; // Comparaison de 0 caractères = égal

    return 0;
}'''),

    ("strncmp/empty_strings", '''
#include <string.h>
int main() {
    char s1[] = "";
    char s2[] = "";

    int result1 = strncmp(s1, s2, 1);
    int result2 = ft_strncmp(s1, s2, 1);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("strncmp/one_empty", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "";

    int result1 = strncmp(s1, s2, 3);
    int result2 = ft_strncmp(s1, s2, 3);

    // s1 > s2
    if ((result1 > 0) != (result2 > 0)) return 1;

    return 0;
}'''),

    ("strncmp/different_lengths", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "Hello World";

    int result1 = strncmp(s1, s2, 5);
    int result2 = ft_strncmp(s1, s2, 5);

    if ((result1 == 0) != (result2 == 0)) return 1;

    // Maintenant comparer plus de caractères
    result1 = strncmp(s1, s2, 10);
    result2 = ft_strncmp(s1, s2, 10);

    // s1 < s2 (à cause du null terminator vs space)
    if ((result1 < 0) != (result2 < 0)) return 1;

    return 0;
}'''),

    ("strncmp/case_sensitive", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "hello";

    int result1 = strncmp(s1, s2, 5);
    int result2 = ft_strncmp(s1, s2, 5);

    // 'H' < 'h' en ASCII
    if ((result1 < 0) != (result2 < 0)) return 1;

    return 0;
}'''),

    ("strncmp/unsigned_char", '''
#include <string.h>
int main() {
    char s1[] = {-1, 0}; // 255 en unsigned
    char s2[] = {1, 0};

    int result1 = strncmp(s1, s2, 1);
    int result2 = ft_strncmp(s1, s2, 1);

    // Doit traiter les caractères comme unsigned
    if ((result1 > 0) != (result2 > 0)) return 1;

    return 0;
}'''),
]
