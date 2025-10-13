"""Tests pour ft_itoa"""

TESTS = [
    ("itoa/positive", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(123);

    if (result == NULL) return 1;
    if (strcmp(result, "123") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/negative", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(-123);

    if (result == NULL) return 1;
    if (strcmp(result, "-123") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/zero", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(0);

    if (result == NULL) return 1;
    if (strcmp(result, "0") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/int_max", '''
#include <stdlib.h>
#include <string.h>
#include <limits.h>
int main() {
    char *result = ft_itoa(INT_MAX);

    if (result == NULL) return 1;
    if (strcmp(result, "2147483647") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/int_min", '''
#include <stdlib.h>
#include <string.h>
#include <limits.h>
int main() {
    char *result = ft_itoa(INT_MIN);

    if (result == NULL) return 1;
    if (strcmp(result, "-2147483648") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/single_digit_positive", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(7);

    if (result == NULL) return 1;
    if (strcmp(result, "7") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/single_digit_negative", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(-7);

    if (result == NULL) return 1;
    if (strcmp(result, "-7") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/large_positive", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(987654321);

    if (result == NULL) return 1;
    if (strcmp(result, "987654321") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/large_negative", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result = ft_itoa(-987654321);

    if (result == NULL) return 1;
    if (strcmp(result, "-987654321") != 0) {
        free(result);
        return 1;
    }

    free(result);
    return 0;
}'''),

    ("itoa/powers_of_ten", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *result;

    result = ft_itoa(10);
    if (result == NULL || strcmp(result, "10") != 0) return 1;
    free(result);

    result = ft_itoa(100);
    if (result == NULL || strcmp(result, "100") != 0) return 1;
    free(result);

    result = ft_itoa(1000);
    if (result == NULL || strcmp(result, "1000") != 0) return 1;
    free(result);

    result = ft_itoa(-10);
    if (result == NULL || strcmp(result, "-10") != 0) return 1;
    free(result);

    return 0;
}'''),
]
