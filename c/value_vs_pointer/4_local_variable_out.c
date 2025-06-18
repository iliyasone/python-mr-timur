#include <stdio.h>

int* generate_array(int **out) {
    int array[5] = {0, 0, 0, 0, 0};

    *out = array;

    printf("inner %d\n", array);
    return array;
}

int main() {
    int* loophole;
    int* array = generate_array(&loophole);

    printf("loophole: %d\n", loophole);
    printf("outer %d\n", array);
    return 0;
}