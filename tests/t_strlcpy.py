"""Tests pour ft_strlcpy"""

TESTS = [
    ("strlcpy/basic", '''
#include <string.h>
int main() {
    char src[] = "Hello World";
    char dest[20];
    size_t result;

    result = ft_strlcpy(dest, src, 20);

    if (strcmp(dest, "Hello World") != 0) return 1;
    if (result != strlen(src)) return 1;

    return 0;
}'''),

    ("strlcpy/truncate", '''
#include <string.h>
int main() {
    char src[] = "Hello World";
    char dest[6]; // Taille insuffisante
    size_t result;

    result = ft_strlcpy(dest, src, 6);

    if (strcmp(dest, "Hello") != 0) return 1;
    if (result != strlen(src)) return 1; // Doit retourner la longueur de src

    return 0;
}'''),

    ("strlcpy/size_zero", '''
#include <string.h>
int main() {
    char src[] = "Hello";
    char dest[10] = "original";
    size_t result;

    result = ft_strlcpy(dest, src, 0);

    if (strcmp(dest, "original") != 0) return 1; // Ne doit pas modifier dest
    if (result != strlen(src)) return 1;

    return 0;
}'''),

    ("strlcpy/size_one", '''
#include <string.h>
int main() {
    char src[] = "Hello";
    char dest[10];
    size_t result;

    dest[0] = 'X'; // Initialiser
    result = ft_strlcpy(dest, src, 1);

    if (dest[0] != '\\0') return 1; // Seul le null terminator
    if (result != strlen(src)) return 1;

    return 0;
}'''),

    ("strlcpy/empty_src", '''
#include <string.h>
int main() {
    char src[] = "";
    char dest[10] = "original";
    size_t result;

    result = ft_strlcpy(dest, src, 10);

    if (strcmp(dest, "") != 0) return 1;
    if (result != 0) return 1;

    return 0;
}'''),

    ("strlcpy/exact_size", '''
#include <string.h>
int main() {
    char src[] = "test";
    char dest[5]; // Exactement la bonne taille
    size_t result;

    result = ft_strlcpy(dest, src, 5);

    if (strcmp(dest, "test") != 0) return 1;
    if (result != 4) return 1;

    return 0;
}'''),

    ("strlcpy/long_string", '''
#include <string.h>
int main() {
    char src[] = "This is a very long string to test strlcpy behavior";
    char dest[20];
    size_t result;

    result = ft_strlcpy(dest, src, 20);

    if (strlen(dest) != 19) return 1; // 19 chars + null terminator
    if (strncmp(dest, src, 19) != 0) return 1;
    if (result != strlen(src)) return 1;

    return 0;
}'''),

    ("strlcpy/special_chars", '''
#include <string.h>
int main() {
    char src[] = "Hello\\tWorld\\n!";
    char dest[20];
    size_t result;

    result = ft_strlcpy(dest, src, 20);

    if (strcmp(dest, src) != 0) return 1;
    if (result != strlen(src)) return 1;

    return 0;
}'''),
]
