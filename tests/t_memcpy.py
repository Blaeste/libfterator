"""Tests pour ft_memcpy"""

TESTS = [
    ("memcpy/basic", '''
#include <string.h>
int main() {
    char src[] = "Hello World";
    char dest1[20];
    char dest2[20];

    memcpy(dest1, src, strlen(src) + 1);
    ft_memcpy(dest2, src, strlen(src) + 1);

    if (strcmp(dest1, dest2) != 0) return 1;
    if (strcmp(dest2, "Hello World") != 0) return 1;

    return 0;
}'''),

    ("memcpy/partial", '''
#include <string.h>
int main() {
    char src[] = "abcdefghij";
    char dest1[20];
    char dest2[20];

    memset(dest1, 'X', 20);
    memset(dest2, 'X', 20);

    memcpy(dest1, src, 5);
    ft_memcpy(dest2, src, 5);

    if (memcmp(dest1, dest2, 20) != 0) return 1;

    return 0;
}'''),

    ("memcpy/zero_size", '''
#include <string.h>
int main() {
    char src[] = "test";
    char dest1[10] = "original";
    char dest2[10] = "original";
    void *result1, *result2;

    result1 = memcpy(dest1, src, 0);
    result2 = ft_memcpy(dest2, src, 0);

    if (strcmp(dest1, "original") != 0) return 1;
    if (strcmp(dest2, "original") != 0) return 1;
    if (result1 != dest1 || result2 != dest2) return 1;

    return 0;
}'''),

    ("memcpy/return_value", '''
#include <string.h>
int main() {
    char src[] = "test";
    char dest[10];

    if (ft_memcpy(dest, src, 5) != dest) return 1;

    return 0;
}'''),

    ("memcpy/binary_data", '''
#include <string.h>
int main() {
    unsigned char src[] = {0, 1, 2, 255, 254, 128, 127};
    unsigned char dest1[10];
    unsigned char dest2[10];

    memcpy(dest1, src, 7);
    ft_memcpy(dest2, src, 7);

    for (int i = 0; i < 7; i++) {
        if (dest1[i] != dest2[i]) return 1;
    }

    return 0;
}'''),

    ("memcpy/large", '''
#include <string.h>
int main() {
    char src[1000];
    char dest1[1000];
    char dest2[1000];

    // Remplir src avec un pattern
    for (int i = 0; i < 1000; i++) {
        src[i] = i % 256;
    }

    memcpy(dest1, src, 1000);
    ft_memcpy(dest2, src, 1000);

    if (memcmp(dest1, dest2, 1000) != 0) return 1;

    return 0;
}'''),

    ("memcpy/struct", '''
#include <string.h>
typedef struct {
    int x;
    char y;
    double z;
} test_t;

int main() {
    test_t src = {42, 'A', 3.14159};
    test_t dest1, dest2;

    memcpy(&dest1, &src, sizeof(test_t));
    ft_memcpy(&dest2, &src, sizeof(test_t));

    if (memcmp(&dest1, &dest2, sizeof(test_t)) != 0) return 1;
    if (dest2.x != 42 || dest2.y != 'A') return 1;

    return 0;
}'''),
]
