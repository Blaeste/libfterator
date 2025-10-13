"""Tests pour ft_strjoin"""

TESTS = [
    ("strjoin/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "Hello ";
    char *s2 = "World";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/empty_first", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "";
    char *s2 = "World";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/empty_second", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "Hello";
    char *s2 = "";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/both_empty", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "";
    char *s2 = "";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/null_first", '''
int main() {
    char *s2 = "World";
    char *result = ft_strjoin(NULL, s2);

    if (result != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("strjoin/null_second", '''
int main() {
    char *s1 = "Hello";
    char *result = ft_strjoin(s1, NULL);

    if (result != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("strjoin/both_null", '''
int main() {
    char *result = ft_strjoin(NULL, NULL);

    if (result != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("strjoin/long_strings", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "This is a very long first string that contains many characters and spaces";
    char *s2 = " and this is the second part that will be concatenated to form an even longer string";
    char *result = ft_strjoin(s1, s2);
    char expected[] = "This is a very long first string that contains many characters and spaces and this is the second part that will be concatenated to form an even longer string";

    if (result == NULL) return 1;
    if (strcmp(result, expected) != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/special_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "Hello\\tWorld\\n";
    char *s2 = "!@#$%^&*()";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello\\tWorld\\n!@#$%^&*()") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strjoin/single_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "A";
    char *s2 = "B";
    char *result = ft_strjoin(s1, s2);

    if (result == NULL) return 1;
    if (strcmp(result, "AB") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),
]
