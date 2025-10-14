"""Tests pour les fonctions ft_put*_fd"""

TESTS = [
    ("putfd/putchar_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
int main() {
    int fd = open("/tmp/test_putchar", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putchar_fd('A', fd);
    ft_putchar_fd('B', fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putchar", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[3];
    if (read(fd, buffer, 2) != 2) {
        close(fd);
        return 1;
    }
    buffer[2] = '\\0';
    close(fd);

    if (buffer[0] != 'A' || buffer[1] != 'B') return 1;

    return 0;
}'''),

    ("putfd/putstr_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main() {
    int fd = open("/tmp/test_putstr", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd("Hello World", fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putstr", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[12];
    if (read(fd, buffer, 11) != 11) {
        close(fd);
        return 1;
    }
    buffer[11] = '\\0';
    close(fd);

    if (strcmp(buffer, "Hello World") != 0) return 1;

    return 0;
}'''),

    ("putfd/putendl_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main() {
    int fd = open("/tmp/test_putendl", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putendl_fd("Hello", fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putendl", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[7];
    if (read(fd, buffer, 6) != 6) {
        close(fd);
        return 1;
    }
    buffer[6] = '\\0';
    close(fd);

    if (strcmp(buffer, "Hello\\n") != 0) return 1;

    return 0;
}'''),

    ("putfd/putnbr_fd_positive", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main() {
    int fd = open("/tmp/test_putnbr", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(123, fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putnbr", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[4];
    if (read(fd, buffer, 3) != 3) {
        close(fd);
        return 1;
    }
    buffer[3] = '\\0';
    close(fd);

    if (strcmp(buffer, "123") != 0) return 1;

    return 0;
}'''),

    ("putfd/putnbr_fd_negative", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main() {
    int fd = open("/tmp/test_putnbr_neg", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(-456, fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putnbr_neg", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[5];
    if (read(fd, buffer, 4) != 4) {
        close(fd);
        return 1;
    }
    buffer[4] = '\\0';
    close(fd);

    if (strcmp(buffer, "-456") != 0) return 1;

    return 0;
}'''),

    ("putfd/putnbr_fd_zero", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
int main() {
    int fd = open("/tmp/test_putnbr_zero", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(0, fd);
    close(fd);

    // Relire le fichier
    fd = open("/tmp/test_putnbr_zero", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[2];
    if (read(fd, buffer, 1) != 1) {
        close(fd);
        return 1;
    }
    buffer[1] = '\\0';
    close(fd);

    if (strcmp(buffer, "0") != 0) return 1;

    return 0;
}'''),

    ("putfd/putstr_fd_empty", '''
#include <unistd.h>
#include <fcntl.h>
int main() {
    int fd = open("/tmp/test_putstr_empty", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd("", fd);
    close(fd);

    // Vérifier que le fichier est vide
    fd = open("/tmp/test_putstr_empty", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[1];
    int bytes_read = read(fd, buffer, 1);
    close(fd);

    if (bytes_read != 0) return 1; // Fichier doit être vide

    return 0;
}'''),

    ("putfd/putstr_fd_null", '''
#include <unistd.h>
#include <fcntl.h>
int main() {
    int fd = open("/tmp/test_putstr_null", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd(NULL, fd);
    close(fd);

    // Ne doit pas planter, comportement défini par l'implémentation
    return 0;
}'''),

    ("putfd/stdout_test", '''
#include <unistd.h>
#include <fcntl.h>
int main() {
    // Test d'écriture vers un fichier (au lieu de stdout pour éviter la pollution d'affichage)
    int fd = open("/tmp/test_stdout", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putchar_fd('X', fd);
    ft_putstr_fd("test", fd);
    ft_putendl_fd("line", fd);
    ft_putnbr_fd(42, fd);

    close(fd);

    return 0;
}'''),

    ("putfd/int_min_max", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <limits.h>
int main() {
    int fd = open("/tmp/test_int_limits", O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(INT_MAX, fd);
    ft_putchar_fd(' ', fd);
    ft_putnbr_fd(INT_MIN, fd);
    close(fd);

    // Relire et vérifier partiellement
    fd = open("/tmp/test_int_limits", O_RDONLY);
    if (fd < 0) return 1;

    char buffer[30];
    int bytes = read(fd, buffer, 29);
    close(fd);

    if (bytes < 20) return 1; // Au moins quelques caractères

    return 0;
}'''),
]
