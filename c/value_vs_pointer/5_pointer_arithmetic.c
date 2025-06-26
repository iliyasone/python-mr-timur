#include <stdio.h>


int main() {
    long long array[] = {1, 2, 3};
    
    printf("sizeof(long long) = %d\n", sizeof(long long));
    // sizeof(long long) = 8

    long long *p = array;
    long long a = 1;
    
    printf("p = %d\n", p);      // p = 6291056
    printf("*p = %d\n", *p);    // *p = 1

    printf("%d+2 = %d\n", p, p+2);

    printf("*(p+2) = %d\n", *(p+2));
}