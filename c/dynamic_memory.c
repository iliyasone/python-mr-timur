#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter your number, len: ");
    scanf("%d", &n);
    
    int *a = malloc(n * sizeof(int));
        // M emory ALLOC ation
    printf("%d %d\n", a, &n);
    for (int i = 0; i<n; i++) {
        printf("a[i] = %d\n", a[i]);
    }
}

