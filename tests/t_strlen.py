"""Tests pour ft_strlen"""

TESTS = [
    ("strlen/basic", '''
#include <string.h>
int main() {
    char *str = "Hello";
    if (ft_strlen(str) != strlen(str)) return 1;
    if (ft_strlen(str) != 5) return 1;
    return 0;
}'''),

    ("strlen/empty", '''
#include <string.h>
int main() {
    char *str = "";
    if (ft_strlen(str) != strlen(str)) return 1;
    if (ft_strlen(str) != 0) return 1;
    return 0;
}'''),

    ("strlen/single_char", '''
#include <string.h>
int main() {
    char *str = "a";
    if (ft_strlen(str) != strlen(str)) return 1;
    if (ft_strlen(str) != 1) return 1;
    return 0;
}'''),

    ("strlen/long_string", '''
#include <string.h>
int main() {
    char *str = "This is a very long string to test strlen implementation";
    if (ft_strlen(str) != strlen(str)) return 1;
    return 0;
}'''),

    ("strlen/with_numbers", '''
#include <string.h>
int main() {
    char *str = "abc123def456";
    if (ft_strlen(str) != strlen(str)) return 1;
    if (ft_strlen(str) != 12) return 1;
    return 0;
}'''),

    ("strlen/special_chars", '''
#include <string.h>
int main() {
    char *str = "!@#$%^&*()_+-=[]{}|;:,.<>?";
    if (ft_strlen(str) != strlen(str)) return 1;
    return 0;
}'''),

    ("strlen/spaces", '''
#include <string.h>
int main() {
    char *str = "   hello   world   ";
    if (ft_strlen(str) != strlen(str)) return 1;
    if (ft_strlen(str) != 19) return 1;
    return 0;
}'''),
]
