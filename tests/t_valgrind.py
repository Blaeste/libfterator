"""Tests Valgrind pour détecter les fuites mémoire"""

TESTS = [
    # Tests pour calloc
    ("valgrind/calloc_basic", '''
#include <stdlib.h>
int main() {
    void *ptr = ft_calloc(10, sizeof(int));
    if (!ptr) return 1;
    free(ptr);
    return 0;
}'''),

    ("valgrind/calloc_zero_count", '''
#include <stdlib.h>
int main() {
    void *ptr = ft_calloc(0, sizeof(int));
    if (ptr) free(ptr);
    return 0;
}'''),

    ("valgrind/calloc_zero_size", '''
#include <stdlib.h>
int main() {
    void *ptr = ft_calloc(10, 0);
    if (ptr) free(ptr);
    return 0;
}'''),

    # Tests pour strdup
    ("valgrind/strdup_basic", '''
#include <stdlib.h>
int main() {
    char *dup = ft_strdup("Hello World");
    if (!dup) return 1;
    free(dup);
    return 0;
}'''),

    ("valgrind/strdup_empty", '''
#include <stdlib.h>
int main() {
    char *dup = ft_strdup("");
    if (!dup) return 1;
    free(dup);
    return 0;
}'''),

    # Tests pour substr
    ("valgrind/substr_basic", '''
#include <stdlib.h>
int main() {
    char *sub = ft_substr("Hello World", 6, 5);
    if (!sub) return 1;
    free(sub);
    return 0;
}'''),

    ("valgrind/substr_beyond_string", '''
#include <stdlib.h>
int main() {
    char *sub = ft_substr("Hello", 10, 5);
    if (!sub) return 1;
    free(sub);
    return 0;
}'''),

    # Tests pour strjoin
    ("valgrind/strjoin_basic", '''
#include <stdlib.h>
int main() {
    char *joined = ft_strjoin("Hello ", "World");
    if (!joined) return 1;
    free(joined);
    return 0;
}'''),

    ("valgrind/strjoin_empty_strings", '''
#include <stdlib.h>
int main() {
    char *joined = ft_strjoin("", "");
    if (!joined) return 1;
    free(joined);
    return 0;
}'''),

    # Tests pour strtrim
    ("valgrind/strtrim_basic", '''
#include <stdlib.h>
int main() {
    char *trimmed = ft_strtrim("   Hello World   ", " ");
    if (!trimmed) return 1;
    free(trimmed);
    return 0;
}'''),

    ("valgrind/strtrim_all_trimmed", '''
#include <stdlib.h>
int main() {
    char *trimmed = ft_strtrim("   ", " ");
    if (!trimmed) return 1;
    free(trimmed);
    return 0;
}'''),

    # Tests pour split
    ("valgrind/split_basic", '''
#include <stdlib.h>
int main() {
    char **result = ft_split("Hello,World,Test", ',');
    if (!result) return 1;

    int i = 0;
    while (result[i]) {
        free(result[i]);
        i++;
    }
    free(result);
    return 0;
}'''),

    ("valgrind/split_empty_string", '''
#include <stdlib.h>
int main() {
    char **result = ft_split("", ',');
    if (!result) return 1;
    free(result);
    return 0;
}'''),

    ("valgrind/split_no_delimiter", '''
#include <stdlib.h>
int main() {
    char **result = ft_split("HelloWorld", ',');
    if (!result) return 1;

    int i = 0;
    while (result[i]) {
        free(result[i]);
        i++;
    }
    free(result);
    return 0;
}'''),

    # Tests pour itoa
    ("valgrind/itoa_positive", '''
#include <stdlib.h>
int main() {
    char *str = ft_itoa(42);
    if (!str) return 1;
    free(str);
    return 0;
}'''),

    ("valgrind/itoa_negative", '''
#include <stdlib.h>
int main() {
    char *str = ft_itoa(-42);
    if (!str) return 1;
    free(str);
    return 0;
}'''),

    ("valgrind/itoa_zero", '''
#include <stdlib.h>
int main() {
    char *str = ft_itoa(0);
    if (!str) return 1;
    free(str);
    return 0;
}'''),

    # Tests pour strmapi
    ("valgrind/strmapi_basic", '''
#include <stdlib.h>
char test_func(unsigned int i, char c) {
    (void)i;  // Éviter l'avertissement unused parameter
    return c + 1;
}
int main() {
    char *result = ft_strmapi("abc", test_func);
    if (!result) return 1;
    free(result);
    return 0;
}'''),

    ("valgrind/strmapi_empty", '''
#include <stdlib.h>
char test_func(unsigned int i, char c) {
    (void)i;  // Éviter l'avertissement unused parameter
    return c;
}
int main() {
    char *result = ft_strmapi("", test_func);
    if (!result) return 1;
    free(result);
    return 0;
}'''),

    # Tests pour les listes (bonus)
    ("valgrind/lstnew_basic", '''
#include <stdlib.h>
int main() {
    int *content = malloc(sizeof(int));
    if (!content) return 1;
    *content = 42;

    t_list *node = ft_lstnew(content);
    if (!node) {
        free(content);
        return 1;
    }

    free(content);
    free(node);
    return 0;
}'''),

    ("valgrind/lstclear_basic", '''
#include <stdlib.h>
void del_content(void *content) {
    free(content);
}
int main() {
    t_list *lst = NULL;

    // Créer une liste avec 3 éléments
    for (int i = 0; i < 3; i++) {
        int *content = malloc(sizeof(int));
        if (!content) return 1;
        *content = i;

        t_list *new_node = ft_lstnew(content);
        if (!new_node) {
            free(content);
            return 1;
        }
        ft_lstadd_front(&lst, new_node);
    }

    // Nettoyer toute la liste
    ft_lstclear(&lst, del_content);

    return 0;
}'''),

    ("valgrind/lstmap_basic", '''
#include <stdlib.h>
void *map_func(void *content) {
    int *new_content = malloc(sizeof(int));
    if (!new_content) return NULL;
    *new_content = (*(int*)content) * 2;
    return new_content;
}
void del_content(void *content) {
    free(content);
}
int main() {
    t_list *lst = NULL;

    // Créer une liste avec 3 éléments
    for (int i = 0; i < 3; i++) {
        int *content = malloc(sizeof(int));
        if (!content) return 1;
        *content = i;

        t_list *new_node = ft_lstnew(content);
        if (!new_node) {
            free(content);
            return 1;
        }
        ft_lstadd_front(&lst, new_node);
    }

    // Mapper la liste
    t_list *mapped = ft_lstmap(lst, map_func, del_content);

    // Nettoyer les deux listes
    ft_lstclear(&lst, del_content);
    if (mapped) ft_lstclear(&mapped, del_content);

    return 0;
}'''),
]
