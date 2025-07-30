#include <stdio.h>
#include <stdlib.h>

#define BASE_LENGTH 1
#define GROW_FACTOR 2

typedef struct {
    int *array;
    long long size;     // number of elements
    long long capacity; // allocated capacity
} PyIntList;

void resize_list(PyIntList *list, long long new_size) {
    int *new_location = malloc(new_size * sizeof(int));
    for (int i = 0; i < list->size; i++) {
        new_location[i] = list->array[i];
    }
    free(list->array);
    list->array = new_location;
    list->capacity = new_size;
}


void append_list(PyIntList *list, int el) {
    if (list->size == list->capacity) {
        int new_capacity = list->capacity * GROW_FACTOR;
        if (new_capacity == 0) {
            new_capacity = BASE_LENGTH;
        }
        resize_list(list, new_capacity);
    }
    list->array[list->size] = el;
    list->size += 1;
}

int pop_list(PyIntList *list) {
    if (list->size == 0) {
        fprintf(stderr, "IndexError: pop from empty list");
        exit(EXIT_FAILURE);
        return -1;
    }
    list->size--;
    return list->array[list->size];
}


void clear_list(PyIntList *list) {
    if (list->capacity > 0) {
        free(list->array);
        list->size = 0;
        list->capacity = 0;
    }
}

int get_list(PyIntList *list, long long index) {
    if (index > list->size) {
        fprintf(stderr, "List index out of range");
        exit(EXIT_FAILURE);
        return -1;
    }
    return list->array[index];
}

void print_list(PyIntList *list) {
    printf("[");
    for (int i = 0; i < list->size; i++) {
        if (i == list->size-1) {
            printf("%d", list->array[i]);
        } else {
            printf("%d, ", list->array[i]);
        }
    }
    printf("]\n");
}

// create new list
PyIntList list() {
    PyIntList list;
    
    list.size = 0;
    list.array = malloc(BASE_LENGTH * sizeof(int));
    list.capacity = BASE_LENGTH;

    return list;
}

int main() {
    PyIntList a = list();
    PyIntList b = list();

    print_list(&a);
    append_list(&a, 1);
    append_list(&a, 3);
    append_list(&a, 2);
    append_list(&a, 4);
    append_list(&a, 5);
    pop_list(&a);
    pop_list(&a);
    print_list(&a);
    return 0;
}
