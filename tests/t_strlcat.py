"""Tests pour ft_strlcat"""

TESTS = [
    ("strlcat/basic", '''
#include <string.h>
int main() {
    char dest[20] = "Hello ";
    char src[] = "World";
    size_t result;

    result = ft_strlcat(dest, src, 20);

    if (strcmp(dest, "Hello World") != 0) return 1;
    if (result != 11) return 1; // len("Hello ") + len("World")

    return 0;
}'''),

    ("strlcat/truncate", '''
#include <string.h>
int main() {
    char dest[10] = "Hello ";
    char src[] = "World!";
    size_t result;

    result = ft_strlcat(dest, src, 10);

    if (strcmp(dest, "Hello Wor") != 0) return 1; // Tronqué
    if (result != 12) return 1; // len("Hello ") + len("World!")

    return 0;
}'''),

    ("strlcat/size_zero", '''
#include <string.h>
int main() {
    char dest[10] = "Hello";
    char src[] = " World";
    size_t result;

    result = ft_strlcat(dest, src, 0);

    if (strcmp(dest, "Hello") != 0) return 1; // Ne doit pas changer
    if (result != strlen(src)) return 1; // 0 + len(src)

    return 0;
}'''),

    ("strlcat/empty_src", '''
#include <string.h>
int main() {
    char dest[20] = "Hello";
    char src[] = "";
    size_t result;

    result = ft_strlcat(dest, src, 20);

    if (strcmp(dest, "Hello") != 0) return 1;
    if (result != 5) return 1; // len("Hello") + len("")

    return 0;
}'''),

    ("strlcat/empty_dest", '''
#include <string.h>
int main() {
    char dest[20] = "";
    char src[] = "Hello";
    size_t result;

    result = ft_strlcat(dest, src, 20);

    if (strcmp(dest, "Hello") != 0) return 1;
    if (result != 5) return 1; // len("") + len("Hello")

    return 0;
}'''),

    ("strlcat/size_equal_dest", '''
#include <string.h>
int main() {
    char dest[10] = "Hello";
    char src[] = " World";
    size_t result;

    result = ft_strlcat(dest, src, 5); // size == strlen(dest)

    if (strcmp(dest, "Hello") != 0) return 1; // Ne doit pas changer
    if (result != 11) return 1; // size + len(src)

    return 0;
}'''),

    ("strlcat/size_less_than_dest", '''
#include <string.h>
int main() {
    char dest[10] = "Hello";
    char src[] = " World";
    size_t result;

    result = ft_strlcat(dest, src, 3); // size < strlen(dest)

    if (strcmp(dest, "Hello") != 0) return 1; // Ne doit pas changer
    if (result != 9) return 1; // size + len(src)

    return 0;
}'''),

    ("strlcat/multiple_concat", '''
#include <string.h>
int main() {
    char dest[50] = "Hello";
    size_t result;

    result = ft_strlcat(dest, " ", 50);
    if (strcmp(dest, "Hello ") != 0) return 1;

    result = ft_strlcat(dest, "World", 50);
    if (strcmp(dest, "Hello World") != 0) return 1;

    result = ft_strlcat(dest, "!", 50);
    if (strcmp(dest, "Hello World!") != 0) return 1;
    if (result != 12) return 1;

    return 0;
}'''),
]
