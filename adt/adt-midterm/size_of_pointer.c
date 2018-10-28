#include <stdio.h>
int main()
{
    //unsigned char *cptr;
    int *iptr;
    long *lptr;
    int x = 10;
    long y = 20;
    iptr = &x;
    lptr = &y;
    printf("Size of int = %lu\n",sizeof(x));
    printf("Size of int pointer = %lu\n",sizeof(iptr));
    printf("Size of long = %lu\n",sizeof(y));
    printf("Size of long pointer = %lu\n",sizeof(lptr));
    
    
    //cptr = 300;
    //printf("At 0x0...0300 = %x\n",*cptr);
    return 0;
}
