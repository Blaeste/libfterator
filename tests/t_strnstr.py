"""Tests pour ft_strnstr"""

TESTS = [
    ("strnstr/basic_found", '''
#include <string.h>
int main() {
    char haystack[] = "Hello World";
    char needle[] = "World";
    char *result;

    result = ft_strnstr(haystack, needle, strlen(haystack));

    if (result != &haystack[6]) return 1;
    if (strncmp(result, "World", 5) != 0) return 1;

    return 0;
}'''),

    ("strnstr/basic_not_found", '''
int main() {
    char haystack[] = "Hello World";
    char needle[] = "Universe";
    char *result;

    result = ft_strnstr(haystack, needle, 11);

    if (result != NULL) return 1;

    return 0;
}'''),

    ("strnstr/empty_needle", '''
#include <string.h>
int main() {
    char haystack[] = "Hello World";
    char needle[] = "";
    char *result;

    result = ft_strnstr(haystack, needle, strlen(haystack));

    if (result != haystack) return 1; // Needle vide = début de haystack

    return 0;
}'''),

    ("strnstr/needle_longer_than_len", '''
int main() {
    char haystack[] = "Hello World";
    char needle[] = "World";
    char *result;

    result = ft_strnstr(haystack, needle, 3); // Trop court pour contenir needle

    if (result != NULL) return 1;

    return 0;
}'''),

    ("strnstr/exact_match", '''
#include <string.h>
int main() {
    char haystack[] = "Hello";
    char needle[] = "Hello";
    char *result;

    result = ft_strnstr(haystack, needle, strlen(haystack));

    if (result != haystack) return 1;

    return 0;
}'''),

    ("strnstr/partial_len", '''
int main() {
    char haystack[] = "Hello World Program";
    char needle[] = "World";
    char *result;

    // Chercher seulement dans "Hello Wo"
    result = ft_strnstr(haystack, needle, 8);

    if (result != NULL) return 1; // Pas assez long pour "World"

    // Chercher dans "Hello World"
    result = ft_strnstr(haystack, needle, 11);

    if (result != &haystack[6]) return 1;

    return 0;
}'''),

    ("strnstr/at_beginning", '''
int main() {
    char haystack[] = "HelloWorld";
    char needle[] = "Hello";
    char *result;

    result = ft_strnstr(haystack, needle, 10);

    if (result != haystack) return 1;

    return 0;
}'''),

    ("strnstr/at_end", '''
int main() {
    char haystack[] = "HelloWorld";
    char needle[] = "World";
    char *result;

    result = ft_strnstr(haystack, needle, 10);

    if (result != &haystack[5]) return 1;

    return 0;
}'''),

    ("strnstr/single_char", '''
int main() {
    char haystack[] = "Hello World";
    char needle[] = "W";
    char *result;

    result = ft_strnstr(haystack, needle, 11);

    if (result != &haystack[6]) return 1;

    return 0;
}'''),

    ("strnstr/multiple_occurrences", '''
int main() {
    char haystack[] = "Hello Hello World";
    char needle[] = "Hello";
    char *result;

    result = ft_strnstr(haystack, needle, 17);

    if (result != haystack) return 1; // Doit retourner la première occurrence

    return 0;
}'''),

    ("strnstr/zero_len", '''
int main() {
    char haystack[] = "Hello World";
    char needle[] = "Hello";
    char *result;

    result = ft_strnstr(haystack, needle, 0);

    if (result != NULL) return 1;

    return 0;
}'''),

    ("strnstr/empty_needle_empty_haystack", '''
int main() {
    char haystack[] = "";
    char needle[] = "";
    char *result;

    result = ft_strnstr(haystack, needle, 0);
    if (result != haystack) return 1;

    result = ft_strnstr(haystack, needle, 1);
    if (result != haystack) return 1;

    result = ft_strnstr(haystack, needle, 2);
    if (result != haystack) return 1;

    return 0;
}'''),

    ("strnstr/empty_haystack_with_needle", '''
int main() {
    char haystack[] = "";
    char needle[] = "teste";
    char *result;

    result = ft_strnstr(haystack, needle, 0);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 1);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 2);
    if (result != NULL) return 1;

    return 0;
}'''),

    ("strnstr/haystack_empty_needle", '''
int main() {
    char haystack[] = "teste";
    char needle[] = "";
    char *result;

    result = ft_strnstr(haystack, needle, 0);
    if (result != haystack) return 1;

    result = ft_strnstr(haystack, needle, 1);
    if (result != haystack) return 1;

    result = ft_strnstr(haystack, needle, 2);
    if (result != haystack) return 1;

    return 0;
}'''),

    ("strnstr/partial_match_boundary", '''
int main() {
    char haystack[] = "abcdefgh";
    char needle[] = "abc";
    char *result;

    // Limite exacte pour ne pas contenir le needle complet
    result = ft_strnstr(haystack, needle, 2);
    if (result != NULL) return 1;

    // Limite exacte pour contenir le needle
    result = ft_strnstr(haystack, needle, 3);
    if (result != haystack) return 1;

    // Plus long que nécessaire
    result = ft_strnstr(haystack, needle, 4);
    if (result != haystack) return 1;

    return 0;
}'''),

    ("strnstr/needle_longer_than_haystack", '''
int main() {
    char haystack[] = "abc";
    char needle[] = "abcdef";
    char *result;

    result = ft_strnstr(haystack, needle, 2);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 3);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 4);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 5);
    if (result != NULL) return 1;

    return 0;
}'''),

    ("strnstr/overlapping_pattern", '''
int main() {
    char haystack[] = "aaxx";
    char needle[] = "xx";
    char *result;

    result = ft_strnstr(haystack, needle, 2);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 3);
    if (result != NULL) return 1;

    result = ft_strnstr(haystack, needle, 4);
    if (result != &haystack[2]) return 1;

    result = ft_strnstr(haystack, needle, 5);
    if (result != &haystack[2]) return 1;

    result = ft_strnstr(haystack, needle, 6);
    if (result != &haystack[2]) return 1;

    return 0;
}'''),

    ("strnstr/signed_chars", '''
int main() {
    unsigned char s1[10] = "abcdef";
    unsigned char s2[10] = "abc\\xfdxx";
    char *result;

    result = ft_strnstr((char*)s1, (char*)s2, 0xffffffff);
    if (result != NULL) return 1;

    return 0;
}'''),
]
