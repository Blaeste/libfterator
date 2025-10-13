"""Tests pour ft_bzero"""

TESTS = [
    ("bzero/basic", '''
#include <string.h>
int main() {
    char buffer1[10] = "abcdefghi";
    char buffer2[10] = "abcdefghi";

    bzero(buffer1, 10);
    ft_bzero(buffer2, 10);

    for (int i = 0; i < 10; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
        if (buffer1[i] != 0) return 1;
    }
    return 0;
}'''),

    ("bzero/partial", '''
#include <string.h>
int main() {
    char buffer1[10] = "abcdefghi";
    char buffer2[10] = "abcdefghi";

    bzero(buffer1 + 3, 4);
    ft_bzero(buffer2 + 3, 4);

    for (int i = 0; i < 10; i++) {
        if (buffer1[i] != buffer2[i]) return 1;
    }
    return 0;
}'''),

    ("bzero/size_zero", '''
#include <string.h>
int main() {
    char buffer1[5] = "test";
    char buffer2[5] = "test";
    size_t zero_size = 0;

    bzero(buffer1, zero_size);
    ft_bzero(buffer2, zero_size);

    // Rien ne doit changer
    if (strcmp(buffer1, "test") != 0) return 1;
    if (strcmp(buffer2, "test") != 0) return 1;

    return 0;
}'''),

    ("bzero/single_byte", '''
#include <string.h>
int main() {
    char buffer1[5] = "test";
    char buffer2[5] = "test";

    bzero(buffer1, 1);
    ft_bzero(buffer2, 1);

    if (buffer1[0] != 0 || buffer2[0] != 0) return 1;
    if (buffer1[1] != 'e' || buffer2[1] != 'e') return 1;

    return 0;
}'''),

    ("bzero/large", '''
#include <string.h>
int main() {
    char buffer1[1000];
    char buffer2[1000];

    // Remplir avec des données
    memset(buffer1, 'A', 1000);
    memset(buffer2, 'A', 1000);

    bzero(buffer1, 1000);
    ft_bzero(buffer2, 1000);

    for (int i = 0; i < 1000; i++) {
        if (buffer1[i] != 0 || buffer2[i] != 0) return 1;
    }
    return 0;
}'''),

    ("bzero/struct", '''
#include <string.h>
typedef struct {
    int a;
    char b;
    double c;
} test_struct;

int main() {
    test_struct s1 = {42, 'X', 3.14};
    test_struct s2 = {42, 'X', 3.14};

    bzero(&s1, sizeof(test_struct));
    ft_bzero(&s2, sizeof(test_struct));

    if (memcmp(&s1, &s2, sizeof(test_struct)) != 0) return 1;

    return 0;
}'''),
]
