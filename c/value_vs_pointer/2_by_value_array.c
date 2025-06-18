#include <stdio.h>

void change_array(int a[5]) {
    for (int i = 0; i < 5; i++) {
        a[i] = a[i]*2;
    }
}

void change_int(int a) {
    a = a * 2;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    

    change_array(a);
    for (int i = 0; i < 5; i++) {
        printf("a[%d] = %d\n", i, a[i]);
    }


    return 0;
}