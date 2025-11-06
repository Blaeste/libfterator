"""Tests pour ft_substr"""

TESTS = [
    ("substr/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello World";
    char *sub = ft_substr(s, 6, 5);

    if (sub == NULL) return 1;
    if (strcmp(sub, "World") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/full_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello";
    char *sub = ft_substr(s, 0, 5);

    if (sub == NULL) return 1;
    if (strcmp(sub, "Hello") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/start_beyond_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello";
    char *sub = ft_substr(s, 10, 3);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/len_beyond_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello";
    char *sub = ft_substr(s, 2, 10); // Plus long que la chaîne

    if (sub == NULL) return 1;
    if (strcmp(sub, "llo") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/zero_length", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello";
    char *sub = ft_substr(s, 2, 0);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/empty_source", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "";
    char *sub = ft_substr(s, 0, 5);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/null_source", '''
int main() {
    char *sub = ft_substr(NULL, 0, 5);

    if (sub != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("substr/single_char", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello World";
    char *sub = ft_substr(s, 6, 1);

    if (sub == NULL) return 1;
    if (strcmp(sub, "W") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/middle_section", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "0123456789";
    char *sub = ft_substr(s, 3, 4);

    if (sub == NULL) return 1;
    if (strcmp(sub, "3456") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/at_end", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello World";
    char *sub = ft_substr(s, 10, 1);

    if (sub == NULL) return 1;
    if (strcmp(sub, "d") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/empty_string_zero_len", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "";
    char *sub = ft_substr(s, 0, 0);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/empty_string_with_len", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "";
    char *sub = ft_substr(s, 0, 1);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/start_beyond_empty", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "";
    char *sub = ft_substr(s, 1, 1);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/max_len", '''
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int main() {
    char *s = "hola";
    char *sub = ft_substr(s, 0, SIZE_MAX);

    if (sub == NULL) return 1;
    if (strcmp(sub, "hola") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/large_start_max_len", '''
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <limits.h>
int main() {
    char *s = "hola";
    char *sub = ft_substr(s, UINT_MAX, SIZE_MAX);

    if (sub == NULL) return 1;
    if (strcmp(sub, "") != 0) {
        free(sub);
        return 1;
    }

    free(sub);
    return 0;
}'''),

    ("substr/exact_boundaries", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "hola";
    char *sub;

    // Test exactement à la limite
    sub = ft_substr(s, 4, 0);
    if (sub == NULL || strcmp(sub, "") != 0) {
        if (sub) free(sub);
        return 1;
    }
    free(sub);

    sub = ft_substr(s, 4, 1);
    if (sub == NULL || strcmp(sub, "") != 0) {
        if (sub) free(sub);
        return 1;
    }
    free(sub);

    sub = ft_substr(s, 3, 1);
    if (sub == NULL || strcmp(sub, "a") != 0) {
        if (sub) free(sub);
        return 1;
    }
    free(sub);

    return 0;
}'''),
]
