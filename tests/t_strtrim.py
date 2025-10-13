"""Tests pour ft_strtrim"""

TESTS = [
    ("strtrim/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "   Hello World   ";
    char *set = " ";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/multiple_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "abcHello Worldcba";
    char *set = "abc";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/no_trim_needed", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "Hello World";
    char *set = "xyz";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/all_trimmed", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "aaabbbccc";
    char *set = "abc";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/empty_string", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "";
    char *set = " ";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/empty_set", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "  Hello World  ";
    char *set = "";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "  Hello World  ") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/null_string", '''
int main() {
    char *set = " ";
    char *result = ft_strtrim(NULL, set);

    if (result != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("strtrim/null_set", '''
int main() {
    char *s1 = "  Hello  ";
    char *result = ft_strtrim(s1, NULL);

    if (result != NULL) return 1; // Doit retourner NULL

    return 0;
}'''),

    ("strtrim/whitespace_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = " \\t\\n Hello World \\n\\t ";
    char *set = " \\t\\n";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/only_beginning", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "abcHello World";
    char *set = "abc";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/only_end", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "Hello Worldabc";
    char *set = "abc";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "Hello World") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("strtrim/single_char", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s1 = "aHa";
    char *set = "a";
    char *result = ft_strtrim(s1, set);

    if (result == NULL) return 1;
    if (strcmp(result, "H") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),
]
