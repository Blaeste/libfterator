"""Tests pour vérifier que les fonctions ne sont PAS sur-protégées
Ces tests vérifient que certaines fonctions crashent bien avec NULL comme elles le devraient,
selon le comportement des fonctions standard de la libc."""

TESTS = [
    ("overprotection/strlen_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_strlen(NULL) crash comme strlen(NULL)
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        // Premier passage - on teste ft_strlen(NULL)
        ft_strlen(NULL);
        // Si on arrive ici, la fonction est sur-protégée (ne crash pas)
        return 1; // FAIL - ne devrait pas protéger contre NULL
    } else {
        // Deuxième passage - on a attrapé le SIGSEGV
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/strchr_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_strchr(NULL, 'a') crash comme strchr(NULL, 'a')
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_strchr(NULL, 'a');
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/strrchr_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_strrchr(NULL, 'a') crash
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_strrchr(NULL, 'a');
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/strncmp_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_strncmp(NULL, "test", 4) crash
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_strncmp(NULL, "test", 4);
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/memcpy_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_memcpy(NULL, "test", 4) crash
    signal(SIGSEGV, segfault_handler);
    char src[] = "test";

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_memcpy(NULL, src, 4);
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/memset_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_memset(NULL, 'A', 5) crash
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_memset(NULL, 'A', 5);
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/memmove_null_should_crash", '''
#include <string.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_memmove(NULL, "test", 4) crash
    signal(SIGSEGV, segfault_handler);
    char src[] = "test";

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_memmove(NULL, src, 4);
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),

    ("overprotection/atoi_null_should_crash", '''
#include <stdlib.h>
#include <signal.h>
#include <setjmp.h>

static sigjmp_buf jump_buffer;

void segfault_handler(int sig) {
    (void)sig;
    siglongjmp(jump_buffer, 1);
}

int main() {
    // On s'attend à ce que ft_atoi(NULL) crash comme atoi(NULL)
    signal(SIGSEGV, segfault_handler);

    if (sigsetjmp(jump_buffer, 1) == 0) {
        ft_atoi(NULL);
        return 1; // FAIL - sur-protégé
    } else {
        return 0; // PASS - crash attendu
    }
}'''),
]
