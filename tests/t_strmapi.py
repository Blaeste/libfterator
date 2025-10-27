"""Tests pour ft_strmapi"""

TESTS = [
    ("strmapi/basic", '''
#include <stdlib.h>
#include <string.h>
char test_func(unsigned int i, char c) {
    (void)i;
    return c + 1; // Décale chaque caractère de 1
}

int main() {
    char *s = "abc";
    char *result = ft_strmapi(s, test_func);

    if (result == NULL) return 1;
    if (strcmp(result, "bcd") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/with_index", '''
#include <stdlib.h>
#include <string.h>
char add_index(unsigned int i, char c) {
    return c + i; // Ajoute l'index au caractère
}

int main() {
    char *s = "aaaa";
    char *result = ft_strmapi(s, add_index);

    if (result == NULL) return 1;
    if (strcmp(result, "abcd") != 0) { // a+0, a+1, a+2, a+3
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/toupper_func", '''
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char to_upper(unsigned int i, char c) {
    (void)i; // Ignore l'index
    return toupper(c);
}

int main() {
    char *s = "hello world";
    char *result = ft_strmapi(s, to_upper);

    if (result == NULL) return 1;
    if (strcmp(result, "HELLO WORLD") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/empty_string", '''
#include <stdlib.h>
#include <string.h>
char dummy_func(unsigned int i, char c) {
    (void)i;
    return c;
}

int main() {
    char *s = "";
    char *result = ft_strmapi(s, dummy_func);

    if (result == NULL) return 1;
    if (strcmp(result, "") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/null_string", '''
char dummy_func(unsigned int i, char c) {
    (void)i;
    return c;
}

int main() {
    char *result = ft_strmapi(NULL, dummy_func);

    if (result != NULL) return 1;

    return 0;
}'''),



    ("strmapi/alternating_case", '''
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char alternate_case(unsigned int i, char c) {
    if (i % 2 == 0) {
        return toupper(c);
    } else {
        return tolower(c);
    }
}

int main() {
    char *s = "hello world";
    char *result = ft_strmapi(s, alternate_case);

    if (result == NULL) return 1;
    if (strcmp(result, "HeLlO WoRlD") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/numbers_to_letters", '''
#include <stdlib.h>
#include <string.h>
char num_to_letter(unsigned int i, char c) {
    (void)i;
    if (c >= '0' && c <= '9') {
        return 'a' + (c - '0');
    }
    return c;
}

int main() {
    char *s = "123abc";
    char *result = ft_strmapi(s, num_to_letter);

    if (result == NULL) return 1;
    if (strcmp(result, "bcdabc") != 0) { // 1->b, 2->c, 3->d, a->a, b->b, c->c
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/single_char", '''
#include <stdlib.h>
#include <string.h>
char increment(unsigned int i, char c) {
    (void)i;
    return c + 1;
}

int main() {
    char *s = "a";
    char *result = ft_strmapi(s, increment);

    if (result == NULL) return 1;
    if (strcmp(result, "b") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/preserve_non_alpha", '''
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char process_alpha_only(unsigned int i, char c) {
    (void)i;
    if (isalpha(c)) {
        return c + 1;
    }
    return c;
}

int main() {
    char *s = "a1b2c!";
    char *result = ft_strmapi(s, process_alpha_only);

    if (result == NULL) return 1;
    if (strcmp(result, "b1c2d!") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strmapi/null_function", '''
#include <stdlib.h>
int main() {
    char *s = "hello";
    char *result = ft_strmapi(s, NULL);

    // ft_strmapi avec une fonction NULL doit retourner NULL
    if (result != NULL) return 1;

    return 0;
}'''),
]
