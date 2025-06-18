#include <stdio.h>

typedef struct
{
    int x;
    int y;
} Point;

void x2Point(Point *a) {
    (*a).x = (*a).x*2;
    a->y = a->y*2;
}


int main(void) {
    Point a = {3, 4}; // a.x = 3; a.y = 4;

    x2Point(&a);
    printf("a.x %d a.y %d\n", a.x, a.y);

    return 0;
}

