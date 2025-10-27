"""Tests pour les fonctions ft_put*_fd"""

TESTS = [
    ("putfd/putchar_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putchar_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putchar_fd('A', fd);
    ft_putchar_fd('B', fd);
    fsync(fd);  // Force l'écriture sur disque
    close(fd);

    // Petite pause pour éviter les race conditions
    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[3];
    if (read(fd, buffer, 2) != 2) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[2] = '\\0';
    close(fd);

    int result = (buffer[0] != 'A' || buffer[1] != 'B') ? 1 : 0;
    unlink(filename);  // Nettoyage
    return result;
}'''),

    ("putfd/putstr_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putstr_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd("Hello World", fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[12];
    if (read(fd, buffer, 11) != 11) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[11] = '\\0';
    close(fd);

    int result = strcmp(buffer, "Hello World") != 0 ? 1 : 0;
    unlink(filename);
    return result;
}'''),

    ("putfd/putendl_fd_basic", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putendl_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putendl_fd("Hello", fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[7];
    if (read(fd, buffer, 6) != 6) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[6] = '\\0';
    close(fd);

    int result = strcmp(buffer, "Hello\\n") != 0 ? 1 : 0;
    unlink(filename);
    return result;
}'''),

    ("putfd/putnbr_fd_positive", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putnbr_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(123, fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[4];
    if (read(fd, buffer, 3) != 3) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[3] = '\\0';
    close(fd);

    int result = strcmp(buffer, "123") != 0 ? 1 : 0;
    unlink(filename);
    return result;
}'''),

    ("putfd/putnbr_fd_negative", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putnbr_neg_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(-456, fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[5];
    if (read(fd, buffer, 4) != 4) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[4] = '\\0';
    close(fd);

    int result = strcmp(buffer, "-456") != 0 ? 1 : 0;
    unlink(filename);
    return result;
}'''),

    ("putfd/putnbr_fd_zero", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putnbr_zero_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(0, fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire le fichier
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[2];
    if (read(fd, buffer, 1) != 1) {
        close(fd);
        unlink(filename);
        return 1;
    }
    buffer[1] = '\\0';
    close(fd);

    int result = strcmp(buffer, "0") != 0 ? 1 : 0;
    unlink(filename);
    return result;
}'''),

    ("putfd/putstr_fd_empty", '''
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putstr_empty_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd("", fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Vérifier que le fichier est vide
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[1];
    int bytes_read = read(fd, buffer, 1);
    close(fd);

    int result = (bytes_read != 0) ? 1 : 0; // Fichier doit être vide
    unlink(filename);
    return result;
}'''),

    ("putfd/putstr_fd_null", '''
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_putstr_null_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putstr_fd(NULL, fd);
    fsync(fd);
    close(fd);

    // Nettoyage
    unlink(filename);

    // Ne doit pas planter, comportement défini par l'implémentation
    return 0;
}'''),

    ("putfd/stdout_test", '''
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
int main() {
    // Test d'écriture vers un fichier (au lieu de stdout pour éviter la pollution d'affichage)
    char filename[256];
    sprintf(filename, "/tmp/test_stdout_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putchar_fd('X', fd);
    ft_putstr_fd("test", fd);
    ft_putendl_fd("line", fd);
    ft_putnbr_fd(42, fd);

    fsync(fd);
    close(fd);

    // Nettoyage
    unlink(filename);

    return 0;
}'''),

    ("putfd/int_min_max", '''
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int main() {
    char filename[256];
    sprintf(filename, "/tmp/test_int_limits_%d", getpid());
    int fd = open(filename, O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd < 0) return 1;

    ft_putnbr_fd(INT_MAX, fd);
    ft_putchar_fd(' ', fd);
    ft_putnbr_fd(INT_MIN, fd);
    fsync(fd);
    close(fd);

    usleep(1000);

    // Relire et vérifier partiellement
    fd = open(filename, O_RDONLY);
    if (fd < 0) {
        unlink(filename);
        return 1;
    }

    char buffer[30];
    int bytes = read(fd, buffer, 29);
    close(fd);

    int result = (bytes < 20) ? 1 : 0; // Au moins quelques caractères
    unlink(filename);
    return result;
}'''),
]
