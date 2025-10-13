"""Tests pour les fonctions bonus des listes chaînées"""

TESTS = [
    ("list/lstnew_basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    char *content = "Hello";
    t_list *node = ft_lstnew(content);

    if (node == NULL) return 1;
    if (node->content != content) return 1;
    if (node->next != NULL) return 1;

    free(node);
    return 0;
}'''),

    ("list/lstnew_null", '''
#include <stdlib.h>
int main() {
    t_list *node = ft_lstnew(NULL);

    if (node == NULL) return 1;
    if (node->content != NULL) return 1;
    if (node->next != NULL) return 1;

    free(node);
    return 0;
}'''),

    ("list/lstadd_front_basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = ft_lstnew("World");
    t_list *new_node = ft_lstnew("Hello");

    ft_lstadd_front(&lst, new_node);

    if (lst != new_node) return 1;
    if (strcmp((char *)lst->content, "Hello") != 0) return 1;
    if (strcmp((char *)lst->next->content, "World") != 0) return 1;

    free(lst->next);
    free(lst);
    return 0;
}'''),

    ("list/lstadd_front_empty", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = NULL;
    t_list *new_node = ft_lstnew("First");

    ft_lstadd_front(&lst, new_node);

    if (lst != new_node) return 1;
    if (strcmp((char *)lst->content, "First") != 0) return 1;
    if (lst->next != NULL) return 1;

    free(lst);
    return 0;
}'''),

    ("list/lstsize_basic", '''
#include <stdlib.h>
int main() {
    t_list *lst = ft_lstnew("1");
    lst->next = ft_lstnew("2");
    lst->next->next = ft_lstnew("3");

    int size = ft_lstsize(lst);

    if (size != 3) return 1;

    free(lst->next->next);
    free(lst->next);
    free(lst);
    return 0;
}'''),

    ("list/lstsize_empty", '''
#include <stdlib.h>
int main() {
    int size = ft_lstsize(NULL);

    if (size != 0) return 1;

    return 0;
}'''),

    ("list/lstsize_single", '''
#include <stdlib.h>
int main() {
    t_list *lst = ft_lstnew("single");

    int size = ft_lstsize(lst);

    if (size != 1) return 1;

    free(lst);
    return 0;
}'''),

    ("list/lstlast_basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = ft_lstnew("1");
    lst->next = ft_lstnew("2");
    lst->next->next = ft_lstnew("last");

    t_list *last = ft_lstlast(lst);

    if (last != lst->next->next) return 1;
    if (strcmp((char *)last->content, "last") != 0) return 1;
    if (last->next != NULL) return 1;

    free(lst->next->next);
    free(lst->next);
    free(lst);
    return 0;
}'''),

    ("list/lstlast_single", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = ft_lstnew("only");

    t_list *last = ft_lstlast(lst);

    if (last != lst) return 1;
    if (strcmp((char *)last->content, "only") != 0) return 1;

    free(lst);
    return 0;
}'''),

    ("list/lstlast_null", '''
#include <stdlib.h>
int main() {
    t_list *last = ft_lstlast(NULL);

    if (last != NULL) return 1;

    return 0;
}'''),

    ("list/lstadd_back_basic", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = ft_lstnew("First");
    t_list *new_node = ft_lstnew("Last");

    ft_lstadd_back(&lst, new_node);

    if (strcmp((char *)lst->content, "First") != 0) return 1;
    if (lst->next != new_node) return 1;
    if (strcmp((char *)lst->next->content, "Last") != 0) return 1;

    free(lst->next);
    free(lst);
    return 0;
}'''),

    ("list/lstadd_back_empty", '''
#include <stdlib.h>
#include <string.h>
int main() {
    t_list *lst = NULL;
    t_list *new_node = ft_lstnew("First");

    ft_lstadd_back(&lst, new_node);

    if (lst != new_node) return 1;
    if (strcmp((char *)lst->content, "First") != 0) return 1;
    if (lst->next != NULL) return 1;

    free(lst);
    return 0;
}'''),

    ("list/lstdelone_basic", '''
#include <stdlib.h>
#include <string.h>
void del_content(void *content) {
    free(content);
}

int main() {
    char *content = malloc(6);
    strcpy(content, "Hello");
    t_list *node = ft_lstnew(content);

    ft_lstdelone(node, del_content);

    // Node est libéré, ne peut pas tester directement
    // Le test passe s'il n'y a pas de segfault
    return 0;
}'''),

    ("list/lstclear_basic", '''
#include <stdlib.h>
#include <string.h>
void del_content(void *content) {
    // Pour ce test, le contenu n'est pas alloué dynamiquement
    (void)content;
}

int main() {
    t_list *lst = ft_lstnew("1");
    lst->next = ft_lstnew("2");
    lst->next->next = ft_lstnew("3");

    ft_lstclear(&lst, del_content);

    if (lst != NULL) return 1;

    return 0;
}'''),

    ("list/lstiter_basic", '''
#include <stdlib.h>
#include <string.h>
static int iter_count = 0;

void count_iter(void *content) {
    (void)content;
    iter_count++;
}

int main() {
    iter_count = 0;

    t_list *lst = ft_lstnew("1");
    lst->next = ft_lstnew("2");
    lst->next->next = ft_lstnew("3");

    ft_lstiter(lst, count_iter);

    if (iter_count != 3) return 1;

    free(lst->next->next);
    free(lst->next);
    free(lst);
    return 0;
}'''),

    ("list/lstiter_empty", '''
#include <stdlib.h>
static int iter_count = 0;

void count_iter(void *content) {
    (void)content;
    iter_count++;
}

int main() {
    iter_count = 0;

    ft_lstiter(NULL, count_iter);

    if (iter_count != 0) return 1;

    return 0;
}'''),

    ("list/lstmap_basic", '''
#include <stdlib.h>
#include <string.h>
void *duplicate_content(void *content) {
    char *str = (char *)content;
    char *dup = malloc(strlen(str) + 1);
    strcpy(dup, str);
    return dup;
}

void del_content(void *content) {
    free(content);
}

int main() {
    t_list *lst = ft_lstnew("Hello");
    lst->next = ft_lstnew("World");

    t_list *mapped = ft_lstmap(lst, duplicate_content, del_content);

    if (mapped == NULL) return 1;
    if (strcmp((char *)mapped->content, "Hello") != 0) return 1;
    if (strcmp((char *)mapped->next->content, "World") != 0) return 1;

    // Clean up original list
    free(lst->next);
    free(lst);

    // Clean up mapped list
    ft_lstclear(&mapped, del_content);

    return 0;
}'''),

    ("list/lstmap_empty", '''
#include <stdlib.h>
void *dummy_f(void *content) {
    return content;
}

void dummy_del(void *content) {
    (void)content;
}

int main() {
    t_list *mapped = ft_lstmap(NULL, dummy_f, dummy_del);

    if (mapped != NULL) return 1;

    return 0;
}'''),

    ("list/complex_operations", '''
#include <stdlib.h>
#include <string.h>
void del_content(void *content) {
    free(content);
}

int main() {
    // Créer une liste de 5 éléments
    t_list *lst = NULL;

    for (int i = 0; i < 5; i++) {
        char *content = malloc(2);
        content[0] = '0' + i;
        content[1] = '\\0';
        t_list *new_node = ft_lstnew(content);
        ft_lstadd_back(&lst, new_node);
    }

    // Vérifier la taille
    if (ft_lstsize(lst) != 5) return 1;

    // Vérifier le dernier élément
    t_list *last = ft_lstlast(lst);
    if (strcmp((char *)last->content, "4") != 0) return 1;

    // Ajouter au début
    char *first_content = malloc(2);
    strcpy(first_content, "X");
    t_list *first_node = ft_lstnew(first_content);
    ft_lstadd_front(&lst, first_node);

    if (ft_lstsize(lst) != 6) return 1;
    if (strcmp((char *)lst->content, "X") != 0) return 1;

    // Nettoyer
    ft_lstclear(&lst, del_content);

    if (lst != NULL) return 1;

    return 0;
}'''),
]
