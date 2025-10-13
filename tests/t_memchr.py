"""Tests pour ft_memchr"""

TESTS = [
    ("memchr/basic_found", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    result1 = memchr(data, 'W', 11);
    result2 = ft_memchr(data, 'W', 11);

    if (result1 != result2) return 1;
    if (result2 != &data[6]) return 1;

    return 0;
}'''),

    ("memchr/not_found", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    result1 = memchr(data, 'X', 11);
    result2 = ft_memchr(data, 'X', 11);

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    return 0;
}'''),

    ("memchr/zero_byte", '''
#include <string.h>
int main() {
    char data[] = "Hello";
    void *result1, *result2;

    result1 = memchr(data, '\\0', 6);
    result2 = ft_memchr(data, '\\0', 6);

    if (result1 != result2) return 1;
    if (result2 != &data[5]) return 1;

    return 0;
}'''),

    ("memchr/binary_data", '''
#include <string.h>
int main() {
    unsigned char data[] = {0, 1, 2, 255, 254, 128, 127};
    void *result1, *result2;

    result1 = memchr(data, 255, 7);
    result2 = ft_memchr(data, 255, 7);

    if (result1 != result2) return 1;
    if (result2 != &data[3]) return 1;

    return 0;
}'''),

    ("memchr/first_byte", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    result1 = memchr(data, 'H', 11);
    result2 = ft_memchr(data, 'H', 11);

    if (result1 != result2) return 1;
    if (result2 != &data[0]) return 1;

    return 0;
}'''),

    ("memchr/last_byte", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    result1 = memchr(data, 'd', 11);
    result2 = ft_memchr(data, 'd', 11);

    if (result1 != result2) return 1;
    if (result2 != &data[10]) return 1;

    return 0;
}'''),

    ("memchr/partial_search", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    // Chercher 'W' seulement dans les 5 premiers bytes
    result1 = memchr(data, 'W', 5);
    result2 = ft_memchr(data, 'W', 5);

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1; // 'W' n'est pas dans les 5 premiers

    return 0;
}'''),

    ("memchr/zero_length", '''
#include <string.h>
int main() {
    char data[] = "Hello World";
    void *result1, *result2;

    result1 = memchr(data, 'H', 0);
    result2 = ft_memchr(data, 'H', 0);

    if (result1 != result2) return 1;
    if (result2 != NULL) return 1;

    return 0;
}'''),

    ("memchr/negative_char", '''
#include <string.h>
int main() {
    char data[] = {-1, -128, 127, 0};
    void *result1, *result2;

    result1 = memchr(data, -1, 4);
    result2 = ft_memchr(data, -1, 4);

    if (result1 != result2) return 1;
    if (result2 != &data[0]) return 1;

    return 0;
}'''),

    ("memchr/struct_data", '''
#include <string.h>
typedef struct {
    int a;
    char b;
    short c;
} test_struct;

int main() {
    test_struct data = {0x41424344, 'X', 0x5959};
    void *result1, *result2;

    // Chercher le byte 'X'
    result1 = memchr(&data, 'X', sizeof(test_struct));
    result2 = ft_memchr(&data, 'X', sizeof(test_struct));

    if (result1 != result2) return 1;

    return 0;
}'''),
]
