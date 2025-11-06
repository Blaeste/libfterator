"""Tests pour ft_memcmp"""

TESTS = [
    ("memcmp/basic_equal", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "Hello";

    int result1 = memcmp(s1, s2, 5);
    int result2 = ft_memcmp(s1, s2, 5);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    return 0;
}'''),

    ("memcmp/basic_different", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "World";

    int result1 = memcmp(s1, s2, 5);
    int result2 = ft_memcmp(s1, s2, 5);

    // Les deux doivent avoir le même signe
    if ((result1 > 0) != (result2 > 0)) return 1;
    if ((result1 < 0) != (result2 < 0)) return 1;

    return 0;
}'''),

    ("memcmp/partial_equal", '''
#include <string.h>
int main() {
    char s1[] = "Hello World";
    char s2[] = "Hello Universe";

    int result1 = memcmp(s1, s2, 5);
    int result2 = ft_memcmp(s1, s2, 5);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1; // Les 5 premiers bytes sont identiques

    return 0;
}'''),

    ("memcmp/zero_length", '''
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = "World";

    int result1 = memcmp(s1, s2, 0);
    int result2 = ft_memcmp(s1, s2, 0);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1; // Comparaison de 0 bytes = égal

    return 0;
}'''),

    ("memcmp/binary_data", '''
#include <string.h>
int main() {
    unsigned char s1[] = {0, 1, 2, 255, 254};
    unsigned char s2[] = {0, 1, 2, 255, 253};

    int result1 = memcmp(s1, s2, 5);
    int result2 = ft_memcmp(s1, s2, 5);

    // s1[4] (254) > s2[4] (253)
    if ((result1 > 0) != (result2 > 0)) return 1;

    return 0;
}'''),

    ("memcmp/with_null_bytes", '''
#include <string.h>
int main() {
    char s1[] = "Hello\\0World";
    char s2[] = "Hello\\0Universe";

    int result1 = memcmp(s1, s2, 12);
    int result2 = ft_memcmp(s1, s2, 12);

    // memcmp ne s'arrête pas aux null bytes
    if ((result1 < 0) != (result2 < 0)) return 1; // 'W' < 'U'

    return 0;
}'''),

    ("memcmp/negative_bytes", '''
#include <string.h>
int main() {
    char s1[] = {-1, 0};
    char s2[] = {1, 0};

    int result1 = memcmp(s1, s2, 2);
    int result2 = ft_memcmp(s1, s2, 2);

    // Doit traiter les bytes comme unsigned
    // -1 (255) > 1
    if ((result1 > 0) != (result2 > 0)) return 1;

    return 0;
}'''),

    ("memcmp/struct_data", '''
#include <string.h>
typedef struct {
    int x;
    char y;
} test_struct;

int main() {
    test_struct s1 = {42, 'A'};
    test_struct s2 = {42, 'B'};

    int result1 = memcmp(&s1, &s2, sizeof(test_struct));
    int result2 = ft_memcmp(&s1, &s2, sizeof(test_struct));

    // Doit être différent à cause du champ 'y'
    if ((result1 < 0) != (result2 < 0)) return 1; // 'A' < 'B'

    return 0;
}'''),

    ("memcmp/large_data", '''
#include <string.h>
int main() {
    char s1[1000];
    char s2[1000];

    // Remplir avec des données identiques
    memset(s1, 'A', 1000);
    memset(s2, 'A', 1000);

    int result1 = memcmp(s1, s2, 1000);
    int result2 = ft_memcmp(s1, s2, 1000);

    if (result1 != result2) return 1;
    if (result2 != 0) return 1;

    // Changer un seul byte au milieu
    s1[500] = 'B';

    result1 = memcmp(s1, s2, 1000);
    result2 = ft_memcmp(s1, s2, 1000);

    if ((result1 > 0) != (result2 > 0)) return 1; // 'B' > 'A'

    return 0;
}'''),

    ("memcmp/null_bytes_beyond_string", '''
#include <string.h>
int main() {
    char s1[20] = "teste";
    char s2[20] = "test";

    // Teste au-delà du null byte
    int result1 = memcmp(s1, s2, 10);
    int result2 = ft_memcmp(s1, s2, 10);

    // s1[4] = 'e', s2[4] = '\\0' donc s1 > s2
    if ((result1 > 0) != (result2 > 0)) return 1;

    return 0;
}'''),

    ("memcmp/signed_char_edge", '''
#include <string.h>
int main() {
    char s1[10] = "abcdef";
    char s2[10] = "abc\\xfdxx";

    int result1 = memcmp(s1, s2, 5);
    int result2 = ft_memcmp(s1, s2, 5);

    // 'd' (0x64) vs 0xfd : doit traiter comme unsigned
    if ((result1 < 0) != (result2 < 0)) return 1;

    return 0;
}'''),

    ("memcmp/continues_after_null", '''
#include <string.h>
int main() {
    char s1[20] = "abc";
    char s2[20] = "abc";

    // Mettre null au même endroit
    s1[3] = 0;
    s2[3] = 0;

    // Mais différences après
    s1[4] = 'x';
    s2[4] = 'y';

    int result1 = memcmp(s1, s2, 7);
    int result2 = ft_memcmp(s1, s2, 7);

    // memcmp continue après le null byte
    if ((result1 < 0) != (result2 < 0)) return 1; // 'x' < 'y'

    return 0;
}'''),
]
