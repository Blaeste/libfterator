"""Tests pour ft_striteri"""

TESTS = [
    ("striteri/basic", '''
#include <string.h>
void increment_char(unsigned int i, char *c) {
    (void)i;
    *c = *c + 1;
}

int main() {
    char s[] = "abc";
    ft_striteri(s, increment_char);

    if (strcmp(s, "bcd") != 0) return 1;

    return 0;
}'''),

    ("striteri/with_index", '''
#include <string.h>
void add_index_to_char(unsigned int i, char *c) {
    *c = *c + i;
}

int main() {
    char s[] = "aaaa";
    ft_striteri(s, add_index_to_char);

    if (strcmp(s, "abcd") != 0) return 1; // a+0, a+1, a+2, a+3

    return 0;
}'''),

    ("striteri/toupper_func", '''
#include <string.h>
#include <ctype.h>
void to_upper_void(unsigned int i, char *c) {
    (void)i;
    *c = toupper(*c);
}

int main() {
    char s[] = "hello world";
    ft_striteri(s, to_upper_void);

    if (strcmp(s, "HELLO WORLD") != 0) return 1;

    return 0;
}'''),

    ("striteri/empty_string", '''
void dummy_func(unsigned int i, char *c) {
    (void)i;
    *c = *c + 1;
}

int main() {
    char s[] = "";
    ft_striteri(s, dummy_func);

    // Ne doit pas planter, string reste vide
    if (s[0] != '\\0') return 1;

    return 0;
}'''),

    ("striteri/null_string", '''
void dummy_func(unsigned int i, char *c) {
    (void)i;
    *c = *c + 1;
}

int main() {
    ft_striteri(NULL, dummy_func);

    // Ne doit pas planter
    return 0;
}'''),



    ("striteri/alternating_case", '''
#include <string.h>
#include <ctype.h>
void alternate_case_void(unsigned int i, char *c) {
    if (i % 2 == 0) {
        *c = toupper(*c);
    } else {
        *c = tolower(*c);
    }
}

int main() {
    char s[] = "hello world";
    ft_striteri(s, alternate_case_void);

    if (strcmp(s, "HeLlO WoRlD") != 0) return 1;

    return 0;
}'''),

    ("striteri/set_to_index", '''
#include <string.h>
void set_to_index(unsigned int i, char *c) {
    *c = '0' + (i % 10); // Convertit l'index en caractère
}

int main() {
    char s[] = "abcdef";
    ft_striteri(s, set_to_index);

    if (strcmp(s, "012345") != 0) return 1;

    return 0;
}'''),

    ("striteri/single_char", '''
#include <string.h>
void increment(unsigned int i, char *c) {
    (void)i;
    *c = *c + 1;
}

int main() {
    char s[] = "a";
    ft_striteri(s, increment);

    if (strcmp(s, "b") != 0) return 1;

    return 0;
}'''),

    ("striteri/preserve_non_alpha", '''
#include <string.h>
#include <ctype.h>
void process_alpha_only_void(unsigned int i, char *c) {
    (void)i;
    if (isalpha(*c)) {
        *c = *c + 1;
    }
}

int main() {
    char s[] = "a1b2c!";
    ft_striteri(s, process_alpha_only_void);

    if (strcmp(s, "b1c2d!") != 0) return 1;

    return 0;
}'''),

    ("striteri/long_string", '''
#include <string.h>
void increment_by_position(unsigned int i, char *c) {
    *c = 'a' + (i % 26); // Cycle through alphabet
}

int main() {
    char s[] = "xxxxxxxxxx"; // 10 chars
    ft_striteri(s, increment_by_position);

    if (strcmp(s, "abcdefghij") != 0) return 1;

    return 0;
}'''),

    ("striteri/null_function", '''
#include <string.h>
int main() {
    char s[] = "hello";

    // ft_striteri avec une fonction NULL ne doit pas planter
    ft_striteri(s, NULL);

    // La chaîne ne doit pas être modifiée
    if (strcmp(s, "hello") != 0) return 1;

    return 0;
}'''),
]
