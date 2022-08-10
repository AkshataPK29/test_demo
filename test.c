#include <stdio.h>
int main()
{
    void *p;
    int i=7;
    float f=23.5;
    p=&i;
    printf("i=%d\n"*((int*)p);
    p=&f;
    printf("i=%d\n"*((int*)p); 
    return 0;
}

