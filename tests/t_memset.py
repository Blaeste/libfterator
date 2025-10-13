"""Tests pour ft_memset"""

TESTS = [
    ("memset/basic", '''
#include <string.h>
int main() {
    char buffer1[10];
    char buffer2[10];

    memset(buffer1, 'A', 10);
    ft_memset(buffer2, 'A', 10);

    for (int i = 0; i < 10; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }
    return 0;
}'''),

    ("memset/zero", '''
#include <string.h>
int main() {
    char buffer1[5] = {1, 2, 3, 4, 5};
    char buffer2[5] = {1, 2, 3, 4, 5};

    memset(buffer1, 0, 5);
    ft_memset(buffer2, 0, 5);

    for (int i = 0; i < 5; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
        if (buffer1[i] != 0) return 1;
    }
    return 0;
}'''),

    ("memset/partial", '''
#include <string.h>
int main() {
    char buffer1[10] = "abcdefghij";
    char buffer2[10] = "abcdefghij";

    memset(buffer1 + 2, 'X', 5);
    ft_memset(buffer2 + 2, 'X', 5);

    for (int i = 0; i < 10; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }
    return 0;
}'''),

    ("memset/size_zero", '''
#include <string.h>
int main() {
    char buffer1[5] = "test";
    char buffer2[5] = "test";
    char *result1, *result2;
    size_t zero_size = 0;

    result1 = memset(buffer1, 'X', zero_size);
    result2 = ft_memset(buffer2, 'X', zero_size);

    // Vérifier que rien n'a changé
    if (strcmp(buffer1, "test") != 0) return 1;
    if (strcmp(buffer2, "test") != 0) return 1;

    // Vérifier la valeur de retour
    if (result1 != buffer1 || result2 != buffer2) return 1;

    return 0;
}'''),

    ("memset/return_value", '''
#include <string.h>
int main() {
    char buffer[10];

    if (ft_memset(buffer, 'A', 10) != buffer) return 1;

    return 0;
}'''),

    ("memset/large", '''
#include <string.h>
int main() {
    char buffer1[1000];
    char buffer2[1000];

    memset(buffer1, 42, 1000);
    ft_memset(buffer2, 42, 1000);

    for (int i = 0; i < 1000; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }
    return 0;
}'''),

    ("memset/negative_char", '''
#include <string.h>
int main() {
    char buffer1[5];
    char buffer2[5];

    memset(buffer1, -1, 5);
    ft_memset(buffer2, -1, 5);

    for (int i = 0; i < 5; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }
    return 0;
}'''),
]
