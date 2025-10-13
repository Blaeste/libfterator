"""Tests pour ft_strdup"""

TESTS = [
    ("strdup/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "Hello World";
    char *dup1 = strdup(src);
    char *dup2 = ft_strdup(src);

    if (dup1 == NULL || dup2 == NULL) return 1;

    if (strcmp(dup1, dup2) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    if (strcmp(dup2, "Hello World") != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    free(dup1);
    free(dup2);
    return 0;
}'''),

    ("strdup/empty_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "";
    char *dup1 = strdup(src);
    char *dup2 = ft_strdup(src);

    if (dup1 == NULL || dup2 == NULL) return 1;

    if (strcmp(dup1, dup2) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    if (strcmp(dup2, "") != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    free(dup1);
    free(dup2);
    return 0;
}'''),

    ("strdup/single_char", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "A";
    char *dup1 = strdup(src);
    char *dup2 = ft_strdup(src);

    if (dup1 == NULL || dup2 == NULL) return 1;

    if (strcmp(dup1, dup2) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    if (strcmp(dup2, "A") != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    free(dup1);
    free(dup2);
    return 0;
}'''),

    ("strdup/long_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "This is a very long string to test the strdup function implementation with various characters and spaces";
    char *dup1 = strdup(src);
    char *dup2 = ft_strdup(src);

    if (dup1 == NULL || dup2 == NULL) return 1;

    if (strcmp(dup1, dup2) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    if (strcmp(dup2, src) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    free(dup1);
    free(dup2);
    return 0;
}'''),

    ("strdup/special_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "Hello\\tWorld\\n!@#$%^&*()";
    char *dup1 = strdup(src);
    char *dup2 = ft_strdup(src);

    if (dup1 == NULL || dup2 == NULL) return 1;

    if (strcmp(dup1, dup2) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    if (strcmp(dup2, src) != 0) {
        free(dup1);
        free(dup2);
        return 1;
    }

    free(dup1);
    free(dup2);
    return 0;
}'''),

    ("strdup/independent_copy", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char src[] = "Hello World";
    char *dup = ft_strdup(src);

    if (dup == NULL) return 1;
    if (dup == src) return 1; // Doit être une copie indépendante

    // Modifier la source ne doit pas affecter la copie
    src[0] = 'X';

    if (dup[0] != 'H') {
        free(dup);
        return 1;
    }

    // Modifier la copie ne doit pas affecter la source
    dup[6] = 'X';

    if (src[6] != 'W') {
        free(dup);
        return 1;
    }

    free(dup);
    return 0;
}'''),

    ("strdup/null_terminator", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "Hello";
    char *dup = ft_strdup(src);

    if (dup == NULL) return 1;

    // Vérifier que le null terminator est copié
    if (strlen(dup) != 5) {
        free(dup);
        return 1;
    }

    if (dup[5] != '\\0') {
        free(dup);
        return 1;
    }

    free(dup);
    return 0;
}'''),

    ("strdup/numbers_and_symbols", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *src = "123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
    char *dup = ft_strdup(src);

    if (dup == NULL) return 1;

    if (strcmp(dup, src) != 0) {
        free(dup);
        return 1;
    }

    free(dup);
    return 0;
}'''),
]
