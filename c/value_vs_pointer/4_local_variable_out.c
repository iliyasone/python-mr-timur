#include <stdio.h>

int* bad_generate_array() {
    int array[5] = {0, 0, 0, 0, 0};

    printf("inner %d\n", array);
    return array;
}

int* good_generate_array() {
    int* inner_array = malloc(sizeof(int) * 5);
    printf("inner %d\n", inner_array);
    return inner_array;
}


int main() {
    int* array = generate_array();

    printf("outer %d\n", array);
    return 0;
}