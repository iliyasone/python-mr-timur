#include <stdio.h>

typedef struct {
    int *array;
    long long size;
    long long capacity;
} PyIntList;

BASE_LENGTH = 8;

// create new list
PyIntList list() {
    PyIntList list;
    
    list.size = 0;
    list.array = malloc(BASE_LENGTH * sizeof(int));
    list.capacity = BASE_LENGTH;

    return list;
}
