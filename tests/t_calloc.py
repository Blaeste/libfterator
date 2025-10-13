"""Tests pour ft_calloc"""

TESTS = [
    ("calloc/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    void *ptr1 = calloc(10, sizeof(int));
    void *ptr2 = ft_calloc(10, sizeof(int));

    if (ptr1 == NULL || ptr2 == NULL) return 1;

    // Vérifier que la mémoire est initialisée à zéro
    int *arr1 = (int *)ptr1;
    int *arr2 = (int *)ptr2;

    for (int i = 0; i < 10; i++) {
        if (arr1[i] != 0 || arr2[i] != 0) {
            free(ptr1);
            free(ptr2);
            return 1;
        }
    }

    free(ptr1);
    free(ptr2);
    return 0;
}'''),

    ("calloc/single_element", '''
#include <stdlib.h>
int main() {
    int *ptr1 = (int *)calloc(1, sizeof(int));
    int *ptr2 = (int *)ft_calloc(1, sizeof(int));

    if (ptr1 == NULL || ptr2 == NULL) return 1;

    if (*ptr1 != 0 || *ptr2 != 0) {
        free(ptr1);
        free(ptr2);
        return 1;
    }

    free(ptr1);
    free(ptr2);
    return 0;
}'''),

    ("calloc/zero_count", '''
#include <stdlib.h>
int main() {
    void *ptr1 = calloc(0, sizeof(int));
    void *ptr2 = ft_calloc(0, sizeof(int));

    // Comportement peut varier, mais doit être cohérent
    if (ptr1 == NULL && ptr2 != NULL) return 1;
    if (ptr1 != NULL && ptr2 == NULL) return 1;

    if (ptr1) free(ptr1);
    if (ptr2) free(ptr2);
    return 0;
}'''),

    ("calloc/zero_size", '''
#include <stdlib.h>
int main() {
    void *ptr1 = calloc(10, 0);
    void *ptr2 = ft_calloc(10, 0);

    // Comportement peut varier, mais doit être cohérent
    if (ptr1 == NULL && ptr2 != NULL) return 1;
    if (ptr1 != NULL && ptr2 == NULL) return 1;

    if (ptr1) free(ptr1);
    if (ptr2) free(ptr2);
    return 0;
}'''),

    ("calloc/char_array", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *ptr1 = (char *)calloc(100, sizeof(char));
    char *ptr2 = (char *)ft_calloc(100, sizeof(char));

    if (ptr1 == NULL || ptr2 == NULL) return 1;

    for (int i = 0; i < 100; i++) {
        if (ptr1[i] != 0 || ptr2[i] != 0) {
            free(ptr1);
            free(ptr2);
            return 1;
        }
    }

    free(ptr1);
    free(ptr2);
    return 0;
}'''),

    ("calloc/large_allocation", '''
#include <stdlib.h>
int main() {
    void *ptr1 = calloc(1000, sizeof(int));
    void *ptr2 = ft_calloc(1000, sizeof(int));

    if (ptr1 == NULL || ptr2 == NULL) return 1;

    int *arr1 = (int *)ptr1;
    int *arr2 = (int *)ptr2;

    // Vérifier quelques éléments au hasard
    if (arr1[0] != 0 || arr2[0] != 0) {
        free(ptr1);
        free(ptr2);
        return 1;
    }
    if (arr1[500] != 0 || arr2[500] != 0) {
        free(ptr1);
        free(ptr2);
        return 1;
    }
    if (arr1[999] != 0 || arr2[999] != 0) {
        free(ptr1);
        free(ptr2);
        return 1;
    }

    free(ptr1);
    free(ptr2);
    return 0;
}'''),

    ("calloc/struct_allocation", '''
#include <stdlib.h>
typedef struct {
    int x;
    char y;
    double z;
} test_struct;

int main() {
    test_struct *ptr1 = (test_struct *)calloc(5, sizeof(test_struct));
    test_struct *ptr2 = (test_struct *)ft_calloc(5, sizeof(test_struct));

    if (ptr1 == NULL || ptr2 == NULL) return 1;

    for (int i = 0; i < 5; i++) {
        if (ptr1[i].x != 0 || ptr2[i].x != 0) {
            free(ptr1);
            free(ptr2);
            return 1;
        }
        if (ptr1[i].y != 0 || ptr2[i].y != 0) {
            free(ptr1);
            free(ptr2);
            return 1;
        }
    }

    free(ptr1);
    free(ptr2);
    return 0;
}'''),

    ("calloc/write_and_read", '''
#include <stdlib.h>
int main() {
    int *ptr = (int *)ft_calloc(10, sizeof(int));

    if (ptr == NULL) return 1;

    // Vérifier qu'on peut écrire et lire
    for (int i = 0; i < 10; i++) {
        ptr[i] = i * 2;
    }

    for (int i = 0; i < 10; i++) {
        if (ptr[i] != i * 2) {
            free(ptr);
            return 1;
        }
    }

    free(ptr);
    return 0;
}'''),
]
