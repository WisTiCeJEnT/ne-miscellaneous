#include <stdio.h>
int f(int a)
{
    printf("a= %u\n",&a);
    int b = 1;
    printf("b= %u\n",&b);
    return b;
}
int main()
{
    int m = -1;
    printf("m= %u\n",&m);
    f(0);
    int n = -1;
    printf("n= %u\n",&n);
    f(0);
     
    return 0;
}