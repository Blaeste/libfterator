"""Tests pour ft_memmove"""

TESTS = [
    ("memmove/basic", '''
#include <string.h>
int main() {
    char src[] = "Hello World";
    char dest1[20];
    char dest2[20];

    memmove(dest1, src, strlen(src) + 1);
    ft_memmove(dest2, src, strlen(src) + 1);

    if (strcmp(dest1, dest2) != 0) return 1;
    if (strcmp(dest2, "Hello World") != 0) return 1;

    return 0;
}'''),

    ("memmove/overlap_forward", '''
#include <string.h>
int main() {
    char buffer1[] = "abcdefghijklmnop";
    char buffer2[] = "abcdefghijklmnop";

    // Décalage vers la droite (overlap)
    memmove(buffer1 + 2, buffer1, 10);
    ft_memmove(buffer2 + 2, buffer2, 10);

    if (strcmp(buffer1, buffer2) != 0) return 1;

    return 0;
}'''),

    ("memmove/overlap_backward", '''
#include <string.h>
int main() {
    char buffer1[] = "abcdefghijklmnop";
    char buffer2[] = "abcdefghijklmnop";

    // Décalage vers la gauche (overlap)
    memmove(buffer1, buffer1 + 2, 10);
    ft_memmove(buffer2, buffer2 + 2, 10);

    if (strcmp(buffer1, buffer2) != 0) return 1;

    return 0;
}'''),

    ("memmove/no_overlap", '''
#include <string.h>
int main() {
    char src[] = "Hello World";
    char dest1[20];
    char dest2[20];

    memset(dest1, 'X', 20);
    memset(dest2, 'X', 20);

    memmove(dest1, src, strlen(src) + 1);
    ft_memmove(dest2, src, strlen(src) + 1);

    if (memcmp(dest1, dest2, 20) != 0) return 1;

    return 0;
}'''),

    ("memmove/zero_size", '''
#include <string.h>
int main() {
    char buffer1[10] = "original";
    char buffer2[10] = "original";
    void *result1, *result2;

    result1 = memmove(buffer1, "test", 0);
    result2 = ft_memmove(buffer2, "test", 0);

    if (strcmp(buffer1, "original") != 0) return 1;
    if (strcmp(buffer2, "original") != 0) return 1;
    if (result1 != buffer1 || result2 != buffer2) return 1;

    return 0;
}'''),

    ("memmove/same_pointer", '''
#include <string.h>
int main() {
    char buffer1[] = "test string";
    char buffer2[] = "test string";

    memmove(buffer1, buffer1, strlen(buffer1));
    ft_memmove(buffer2, buffer2, strlen(buffer2));

    if (strcmp(buffer1, buffer2) != 0) return 1;
    if (strcmp(buffer2, "test string") != 0) return 1;

    return 0;
}'''),

    ("memmove/binary_overlap", '''
#include <string.h>
int main() {
    unsigned char buffer1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    unsigned char buffer2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    memmove(buffer1 + 3, buffer1, 5);
    ft_memmove(buffer2 + 3, buffer2, 5);

    for (int i = 0; i < 10; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }

    return 0;
}'''),

    ("memmove/large_overlap", '''
#include <string.h>
int main() {
    char buffer1[1000];
    char buffer2[1000];

    // Initialiser avec un pattern
    for (int i = 0; i < 1000; i++) {
        buffer1[i] = buffer2[i] = 'A' + (i % 26);
    }

    memmove(buffer1 + 100, buffer1, 800);
    ft_memmove(buffer2 + 100, buffer2, 800);

    if (memcmp(buffer1, buffer2, 1000) != 0) return 1;

    return 0;
}'''),

    ("memmove/exact_overlap", '''
#include <string.h>
int main() {
    char buffer1[] = "Hello World";
    char buffer2[] = "Hello World";

    // Overlap exact (même pointeur)
    memmove(buffer1, buffer1, strlen(buffer1));
    ft_memmove(buffer2, buffer2, strlen(buffer2));

    if (strcmp(buffer1, buffer2) != 0) return 1;
    if (strcmp(buffer2, "Hello World") != 0) return 1;

    return 0;
}'''),

    ("memmove/single_byte_overlap", '''
#include <string.h>
int main() {
    char buffer1[] = "abcdefgh";
    char buffer2[] = "abcdefgh";

    // Overlap d'un seul byte
    memmove(buffer1 + 1, buffer1, 1);
    ft_memmove(buffer2 + 1, buffer2, 1);

    if (strcmp(buffer1, buffer2) != 0) return 1;

    return 0;
}'''),
]
