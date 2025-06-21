#include <stdio.h>
#include <stdlib.h>

#define BASE_LENGTH 8

typedef struct {
    int *array;
    long long size;     // number of elements
    long long capacity; // allocated capacity
} PyIntList;

void init_list(PyIntList *list);

void resize_list(PyIntList *list, long long new_size);

void append_list(PyIntList *list, int el);

int pop_list(PyIntList *list);

void clear_list(PyIntList *list);

int get_list(PyIntList *list, long long index);

void print_list(PyIntList *list);


int main() {
    PyIntList my_list;
    init_list(&my_list);
}

// a = list()