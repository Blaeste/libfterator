"""Tests pour ft_split"""

TESTS = [
    ("split/basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello World Test";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "Hello") != 0) return 1;
    if (strcmp(result[1], "World") != 0) return 1;
    if (strcmp(result[2], "Test") != 0) return 1;
    if (result[3] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/multiple_delimiters", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello  World   Test";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "Hello") != 0) return 1;
    if (strcmp(result[1], "World") != 0) return 1;
    if (strcmp(result[2], "Test") != 0) return 1;
    if (result[3] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/leading_trailing_delim", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = " Hello World ";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "Hello") != 0) return 1;
    if (strcmp(result[1], "World") != 0) return 1;
    if (result[2] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/empty_string", '''
#include <stdlib.h>
int main() {
    char *s = "";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (result[0] != NULL) return 1;

    free(result);
    return 0;
}'''),

    ("split/only_delimiters", '''
#include <stdlib.h>
int main() {
    char *s = "   ";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (result[0] != NULL) return 1;

    free(result);
    return 0;
}'''),

    ("split/single_word", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "Hello";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "Hello") != 0) return 1;
    if (result[1] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/no_delimiter_found", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "HelloWorld";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "HelloWorld") != 0) return 1;
    if (result[1] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/null_string", '''
int main() {
    char **result = ft_split(NULL, ' ');

    if (result != NULL) return 1;

    return 0;
}'''),

    ("split/different_delimiter", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "one,two,three,four";
    char **result = ft_split(s, ',');

    if (result == NULL) return 1;
    if (strcmp(result[0], "one") != 0) return 1;
    if (strcmp(result[1], "two") != 0) return 1;
    if (strcmp(result[2], "three") != 0) return 1;
    if (strcmp(result[3], "four") != 0) return 1;
    if (result[4] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/single_char_words", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "a b c d";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "a") != 0) return 1;
    if (strcmp(result[1], "b") != 0) return 1;
    if (strcmp(result[2], "c") != 0) return 1;
    if (strcmp(result[3], "d") != 0) return 1;
    if (result[4] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/complex_example", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "::Hello::World::Test::";
    char **result = ft_split(s, ':');

    if (result == NULL) return 1;
    if (strcmp(result[0], "Hello") != 0) return 1;
    if (strcmp(result[1], "World") != 0) return 1;
    if (strcmp(result[2], "Test") != 0) return 1;
    if (result[3] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/single_char", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "a";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "a") != 0) return 1;
    if (result[1] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/delimiter_not_found", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "HelloWorld";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "HelloWorld") != 0) return 1;
    if (result[1] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/mixed_delimiters", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "a,b,c,d,e";
    char **result = ft_split(s, ',');

    if (result == NULL) return 1;
    if (strcmp(result[0], "a") != 0) return 1;
    if (strcmp(result[1], "b") != 0) return 1;
    if (strcmp(result[2], "c") != 0) return 1;
    if (strcmp(result[3], "d") != 0) return 1;
    if (strcmp(result[4], "e") != 0) return 1;
    if (result[5] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/consecutive_delimiters_start", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "   hello world";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "hello") != 0) return 1;
    if (strcmp(result[1], "world") != 0) return 1;
    if (result[2] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/consecutive_delimiters_end", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "hello world   ";
    char **result = ft_split(s, ' ');

    if (result == NULL) return 1;
    if (strcmp(result[0], "hello") != 0) return 1;
    if (strcmp(result[1], "world") != 0) return 1;
    if (result[2] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),

    ("split/null_input", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char **result = ft_split(NULL, ' ');

    if (result != NULL) return 1; // Doit retourner NULL pour entrée NULL

    return 0;
}'''),

    ("split/special_chars", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *s = "hello\\nworld\\ttest";
    char **result = ft_split(s, '\\n');

    if (result == NULL) return 1;
    if (strcmp(result[0], "hello") != 0) return 1;
    if (strcmp(result[1], "world\\ttest") != 0) return 1;
    if (result[2] != NULL) return 1;

    for (int i = 0; result[i]; i++) free(result[i]);
    free(result);
    return 0;
}'''),
]
