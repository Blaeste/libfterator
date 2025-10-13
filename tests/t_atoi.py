"""Tests pour ft_atoi"""

TESTS = [
    ("atoi/basic_positive", '''
#include <stdlib.h>
int main() {
    char *str = "123";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 123) return 1;

    return 0;
}'''),

    ("atoi/basic_negative", '''
#include <stdlib.h>
int main() {
    char *str = "-123";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != -123) return 1;

    return 0;
}'''),

    ("atoi/with_plus", '''
#include <stdlib.h>
int main() {
    char *str = "+42";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 42) return 1;

    return 0;
}'''),

    ("atoi/zero", '''
#include <stdlib.h>
int main() {
    char *str = "0";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("atoi/leading_whitespace", '''
#include <stdlib.h>
int main() {
    char *str = "   \\t\\n  42";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 42) return 1;

    return 0;
}'''),

    ("atoi/trailing_chars", '''
#include <stdlib.h>
int main() {
    char *str = "123abc";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 123) return 1;

    return 0;
}'''),

    ("atoi/no_digits", '''
#include <stdlib.h>
int main() {
    char *str = "abc";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("atoi/empty_string", '''
#include <stdlib.h>
int main() {
    char *str = "";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("atoi/only_whitespace", '''
#include <stdlib.h>
int main() {
    char *str = "   \\t\\n  ";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("atoi/multiple_signs", '''
#include <stdlib.h>
int main() {
    char *str = "+-42";
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;
    // Comportement dépendant de l'implémentation, mais doit être cohérent

    return 0;
}'''),

    ("atoi/large_number", '''
#include <stdlib.h>
int main() {
    char *str = "2147483647"; // INT_MAX
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;

    return 0;
}'''),

    ("atoi/negative_large", '''
#include <stdlib.h>
int main() {
    char *str = "-2147483648"; // INT_MIN (approximatif)
    int result1 = atoi(str);
    int result2 = ft_atoi(str);

    if (result1 != result2) return 1;

    return 0;
}'''),
]
