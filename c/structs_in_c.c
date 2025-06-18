#include <stdio.h>

// straightforward
struct Point1 {
    int x;
    int y;
};

struct Point1 p1;

// anonym
struct 
{
    int x;
    int y;
} p2;

typedef struct 
{
    int x;
    int y;
} Point3;



int main() {
    p1.x = 2;
    p1.y = 3;

    p2.x = 4;
    p2.y = 5;

    printf("size of p2 is %d", sizeof(p2));
}