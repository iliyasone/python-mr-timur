#include <stdio.h>

typedef struct {
    int array[5]; // 4 * 5
} StructArray;

typedef struct {
    int *array; // 8 - one ponter
} DynamicArray;

void change_array(StructArray a) {
    for (int i = 0; i < 5; i++) {
        a.array[i] = a.array[i] * 2;
    }
}

int main() {
    StructArray a = {{1, 2, 3, 4, 5}};    
    change_array(a);
    for (int i = 0; i < 5; i++) {
        printf("a[%d] = %d\n", i, a.array[i]);
    }

    return 0;
}
