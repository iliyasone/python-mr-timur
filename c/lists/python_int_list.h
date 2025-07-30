#include <stdio.h>
#include <stdlib.h>

#define BASE_LENGTH 8
#define LIST_TYPE int

typedef struct {
    int *array;
    long long size;     // number of elements
    long long capacity; // allocated capacity
} PyIntList;

void init_list(PyIntList *list) {
    list->size = 0;
    // lise
}

void resize_list(PyIntList *list, long long new_size) {
    //...
    free(list->array);
}

void append_list(PyIntList *list, int el);

int pop_list(PyIntList *list);

void clear_list(PyIntList *list);

int get_list(PyIntList *list, long long index) {
    if (index > (*list).size)
    {
        fprintf(stderr, "IndexError");
        exit(EXIT_FAILURE); 
    }
    return (*list).array[index];
}
// a[i]   get_list(&a, i)

void print_list(PyIntList *list);


int main() {
    PyIntList my_list;
    init_list(&my_list);
    append_list(&my_list, 1);
    append_list(&my_list, 2);
    append_list(&my_list, 3);
    append_list(&my_list, 4);
    append_list(&my_list, 5);

    print_list(&my_list); // [1, 2, 3, 4, 5]

    printf("%d\n", pop_list(&my_list)); // 5         
    // [1, 2, 3, 4, 5]

    

    printf("5 element\n", my_list.array[100]); // *(array + 0)
    append_list(&my_list, 1);
    // printf("len - %d\n",);
    
    return 0;
}

/*-------------------------------------------------------------*/
int main(void)
{
    /* create an empty list */
    PyIntList lst;
    init_list(&lst);
    printf("new list → ");
    print_list(&lst);           // []

    /* append five numbers */
    for (int i = 1; i <= 5; ++i) {
        append_list(&lst, i);
        printf("after append(%d) → ", i);
        print_list(&lst);
    }

    /* pop the last element */
    int last = pop_list(&lst);
    printf("pop() returned %d\n", last);
    printf("list after pop      → ");
    print_list(&lst);

    /* grow the list to force at least one resize */
    for (int i = 6; i <= 20; ++i)
        append_list(&lst, i);
    printf("after adding up to 20 → ");
    print_list(&lst);
    printf("(size=%lld  capacity=%lld)\n", lst.size, lst.capacity);

    /* clear everything */
    clear_list(&lst);
    printf("after clear() → size=%lld  capacity=%lld\n",
           lst.size, lst.capacity);

    return 0;
}


        